import io from 'socket.io-client';
import $ from "jquery";

require('./mystyles.scss');

const socket = io('http://localhost:3000', {transports: ['websocket']});
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
    "room": undefined
};


function change_page(page) {
    $(".page").addClass("disabled");
    $(page).removeClass("disabled");
}

let interval = null;
let settings = {};

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
    } else if(current_room['status'] === 'show_stats') {
        current_screen = '#game-over-page';
        let tbody_html = '';
        for (let key in current_room['stats']) {
            tbody_html += '<tr><td>' + key + '</td>' +
            '<td>'+ current_room['stats'][key][0] +'</td>' +
            '<td>' + current_room['stats'][key][1] + '</td>' +
            '<td>' + (current_room['stats'][key][0] + current_room['stats'][key][1]) + '</td></tr>';
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
    change_page(current_screen);
}

async function tick() {
    let since_round_started = new Date().getTime() - round_started_time;
    $(".bar").attr("value", since_round_started);
    if (since_round_started >= settings['time'] * 1000) {
        socket.emit("end_round");
        clearInterval(interval);
    }
}

$("#reset_button").on("click", function () {
    socket.emit("endgame");
});

$("#go-round").on("click", function () {
    socket.emit("start_round");
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
});

$("#join-button").on("click", function () {
    person_data['room'] = $("#room-field").val();
    socket.emit("join", person_data)
});

$("#create-button").on("click", function () {
    person_data['username'] = $("#username-field").val();
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

$("#give-up").on("click", function () {
    socket.emit("end_round");
});

$("#correct").on("click", function () {
    socket.emit("remove_word",  "correct");
});


// Slider implementation

function findOutputForSlider( element ) {
    let idVal = element.id;
    let outputs = document.getElementsByTagName( 'output' );
    for( let i = 0; i < outputs.length; i++ ) {
        if (outputs[ i ].htmlFor == idVal)
            return outputs[ i ];
    }
}

document.addEventListener( 'DOMContentLoaded', function () {
    let sliders = document.querySelectorAll( 'input[type="range"].slider' );
    [].forEach.call( sliders, function ( slider ) {
        let output = findOutputForSlider( slider );
        if ( output ) {
            slider.addEventListener( 'input', function( event ) {
                output.value = event.target.value;
            } );
        }
    } );
} );
