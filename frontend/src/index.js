import io from 'socket.io-client';
import $ from "jquery";

require('./mystyles.scss');

const socket = io('/', {transports: ['websocket']});
let current_room = {};
let current_screen = "#login-page";
let hits = 0;
let round_started_time = null;

socket.on('connect', function () {
});

socket.on('update', function (data) {
    console.log(data);
    current_room = data;
    redraw();
});

let person_data = {
    "username": undefined,
    "room": undefined,
    "lang": "eng"
};


function change_page(page) {
    $(".page").addClass("disabled");
    $(page).removeClass("disabled");
}

let interval = null;
let settings = {
    "dict": "Complete russian"
};

function redraw_person() {
    if (person_data['username'] !== undefined || current_room['name'] !== undefined) {
        $("#info-card").removeClass("disabled");
    } else {
        $("#info-card").addClass("disabled");
    }
    if (person_data['username'] !== undefined) {
        $("#user-info").removeClass("disabled");
        $("#user-info-label").html(person_data['username']);
    } else {
        $("#user-info").addClass("disabled");
    }
    if (current_room['name'] !== undefined) {
        $("#room-info").removeClass("disabled");
        $("#room-info-label").html(current_room['name']);
    } else {
        $("#room-info").addClass("disabled");
    }
}

function redraw() {
    if (current_room['status'] === 'game_setup') {
        current_screen = '#room_page';
    }
    if (current_room['status'] === 'waiting_round') {
        let current_players = current_room["queue"][current_room["queue_id"]];
        current_screen = '#next-round';
        $(".player1").html(current_players[0]);
        $(".player2").html(current_players[1]);
        if (person_data['username'] != current_players[0]) {
            $("#go-round").addClass("disabled");
        } else {
            $("#go-round").removeClass("disabled");
        }
    } else if (current_room['status'] === 'playing') {
        if (current_screen == "#next-round") {
            round_started_time = new Date().getTime();
            $(".bar").attr("max", current_room['settings']['time'] * 1000);
            $(".bar").attr("value", 0);
            interval = setInterval(tick, 10);
        }
        let current_players = current_room["queue"][current_room["queue_id"]];
        current_screen = '#running-round-play';
        $("#word").html(current_room["pool"][0]);
        if (person_data['username'] != current_players[0]) {
            $(".game-control").addClass("disabled");
        } else {
            $(".game-control").removeClass("disabled");
        }
    } else if (current_room['status'] === 'show_stats') {
        current_screen = '#game-over-page';
        let tbody_html = '';
        console.log(current_room['last_statistics']['users']);
        for (let user in current_room['last_statistics']['users']) {
            tbody_html += '<tr><td>' + current_room['last_statistics']['users'][user]['username'] + '</td>' +
                '<td>' + current_room['last_statistics']['users'][user]['guesses'] + '</td>' +
                '<td>' + current_room['last_statistics']['users'][user]['explanations'] + '</td>' +
                '<td>' + current_room['last_statistics']['users'][user]['mistakes'] + '</td>' +
                '<td>' + current_room['last_statistics']['users'][user]['points'] + '</td></tr>';
            $("#stats").html(tbody_html);
        }
    }

    let participants_html = '';
    for (let key in current_room['members']) {
        participants_html += '<span class="tag" style="margin-right: 3px">' + key + '<span class="' +
            current_room["members"][key] + '">●</span></span>';
    }
    $(".participants").html(participants_html);
    $("#room-name").html(current_room['name']);
    redraw_person();
    change_page(current_screen);
}

function tick() {
    let since_round_started = new Date().getTime() - round_started_time;
    $(".bar").attr("value", since_round_started);
    if (since_round_started >= settings['time'] * 1000) {
        socket.emit("remove_word", {
                "verdict": "mistake",
                "screen_time": 0
            }
        );
        socket.emit("end_round");
        clearInterval(interval);
    }
}

$("#reset_button").on("click", function () {
    socket.emit("endgame");
});

$("#go-round").on("click", function () {
    change_page("#countdown-page");
    init();
    // since_round_started = 0;
    // $(".bar").attr("max", settings['time'] * 1000);
    // $(".bar").attr("value", 0);
    // interval = setInterval(tick, 1000);
});

$("#to-join-button").on("click", function () {
    person_data['username'] = $("#username-field").val();
    change_page("#join-page")
});

$("#sign-out").on("click", function () {
    person_data = {
        "username": undefined,
        "room": undefined
    };
    current_room = {};
    change_page("#login-page");
    redraw_person();
});

$("#join-button").on("click", function () {
    person_data['room'] = $("#room-field").val().trim();
    socket.emit("join", person_data)
});

$("#create-button").on("click", function () {
    person_data['username'] = $("#username-field").val().trim();
    socket.emit("create", person_data)
});

$("#init-game").on("click", function () {
    settings['time'] = Number.parseInt($("#time_slider").val(), 10);
    settings['difficulty'] = Number.parseInt($("#difficulty_slider").val(), 10);
    settings['words'] = Number.parseInt($("#words_slider").val(), 10);
    settings['dispersion'] = Number.parseInt($("#dispersion_slider").val(), 10);
    socket.emit("init", Object.assign({}, person_data, {"settings": settings}));
});

// $("#mistake").on("click", function () {
//
// });

$("#mistake").on("click", function () {
    socket.emit("remove_word", {
            "verdict": "mistake",
            "screen_time": 0
        }
    );
});


$("#give-up").on("click", function () {
    socket.emit("remove_word", {
            "verdict": "timeout",
            "screen_time": 0
        }
    );
    socket.emit("end_round");
});

$("#correct").on("click", function () {
    socket.emit("remove_word", {
            "verdict": "correct",
            "screen_time": 0
        }
    );
});


// Slider implementation

function findOutputForSlider(element) {
    let idVal = element.id;
    let outputs = document.getElementsByTagName('output');
    for (let i = 0; i < outputs.length; i++) {
        if (outputs[i].htmlFor == idVal)
            return outputs[i];
    }
}

document.addEventListener('DOMContentLoaded', function () {
    let sliders = document.querySelectorAll('input[type="range"].slider');
    [].forEach.call(sliders, function (slider) {
        let output = findOutputForSlider(slider);
        if (output) {
            slider.addEventListener('input', function (event) {
                output.value = event.target.value;
            });
        }
    });
});


// Countdown implementation

// Credit: Mateusz Rybczonec

const FULL_DASH_ARRAY = 283;
const WARNING_THRESHOLD = 10;
const ALERT_THRESHOLD = 5;

const COLOR_CODES = {
    info: {
        color: "green"
    },
    warning: {
        color: "orange",
        threshold: WARNING_THRESHOLD
    },
    alert: {
        color: "red",
        threshold: ALERT_THRESHOLD
    }
};

const TIME_LIMIT = 3;
let timePassed = 0;
let timeLeft = TIME_LIMIT;
let timerInterval = null;
let remainingPathColor = COLOR_CODES.info.color;

function init() {

    timePassed = 0;
    timeLeft = TIME_LIMIT;
    timerInterval = null;
    remainingPathColor = COLOR_CODES.info.color;

    document.getElementById("countdown").innerHTML = `
<div class="base-timer">
  <svg class="base-timer__svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <g class="base-timer__circle">
      <circle class="base-timer__path-elapsed" cx="50" cy="50" r="45"></circle>
      <path
        id="base-timer-path-remaining"
        stroke-dasharray="283"
        class="base-timer__path-remaining ${remainingPathColor}"
        d="
          M 50, 50
          m -45, 0
          a 45,45 0 1,0 90,0
          a 45,45 0 1,0 -90,0
        "
      ></path>
    </g>
  </svg>
  <span id="base-timer-label" class="base-timer__label">${formatTime(
        timeLeft
    )}</span>
</div>
`;

    startTimer();
}


function onTimesUp() {
    clearInterval(timerInterval);
    socket.emit("start_round");
}

function startTimer() {
    timerInterval = setInterval(() => {
        timePassed = timePassed += 1;
        timeLeft = TIME_LIMIT - timePassed;
        document.getElementById("base-timer-label").innerHTML = formatTime(
            timeLeft
        );
        setCircleDasharray();
        setRemainingPathColor(timeLeft);

        if (timeLeft === 0) {
            onTimesUp();
        }
    }, 1000);
}

function formatTime(time) {
    return `${time}`;
}

function setRemainingPathColor(timeLeft) {
    const {alert, warning, info} = COLOR_CODES;
    if (timeLeft <= alert.threshold) {
        document
            .getElementById("base-timer-path-remaining")
            .classList.remove(warning.color);
        document
            .getElementById("base-timer-path-remaining")
            .classList.add(alert.color);
    } else if (timeLeft <= warning.threshold) {
        document
            .getElementById("base-timer-path-remaining")
            .classList.remove(info.color);
        document
            .getElementById("base-timer-path-remaining")
            .classList.add(warning.color);
    }
}

function calculateTimeFraction() {
    const rawTimeFraction = timeLeft / (30 * TIME_LIMIT);
    return rawTimeFraction - (1 / TIME_LIMIT) * (1 - rawTimeFraction);
}

function setCircleDasharray() {
    const circleDasharray = `${(
        calculateTimeFraction() * FULL_DASH_ARRAY
    ).toFixed(0)} 283`;
    document
        .getElementById("base-timer-path-remaining")
        .setAttribute("stroke-dasharray", circleDasharray);
}
