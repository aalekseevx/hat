import Vue from 'vue';
import Vuex from 'vuex';
import api from "../api"

Vue.use(Vuex);

async function get_config() {
    let return_value = null;
    await api().get('/config').then(function (response) {
        return_value = response['data'];
    })
    return return_value
}

function getDefaultState () {
    let data = {
        isConnected: false,
        authorized: false,
        username: null,
        room: null,
        lang: "en",
        room_session: null,
        loading: false,
        current_hits: 0,
        last_hits: null
    }
    get_config().then(function (value) {
        data['config'] = value
    });
    return data;
}

const state = getDefaultState();

const actions = {
    create(ctx, data) {
        const transfer_data = {
            username: data['username'],
            room: null,
            lang: state.lang
        };
        window.vm.$socket.emit('create', transfer_data, function () {
            ctx.commit('SET_CREDENTIALS', data);
            window.vm.$router.push({ path: 'play' }).catch((err) => {
                throw new Error(`Problem handling push: ${err}.`);
            })
        });
    },
    join(ctx, data) {
        const transfer_data = {
            username: data['username'],
            room: data['room'],
            lang: state.lang
        };
        window.vm.$socket.emit('join', transfer_data, function () {
            ctx.commit('SET_CREDENTIALS', data);
            console.log("join socket emit");
            window.vm.$router.push({ path: 'play' }).catch((err) => {
                throw new Error(`Problem handling push: ${err}.`);
            })
        });
    },

    init_game(ctx, data) {
        const transfer_data = {
            settings: {
                "dict": "Complete russian"
            }
        };
        window.vm.$socket.emit('join', transfer_data, function () {
            ctx.commit('SET_CREDENTIALS', data);
            window.vm.$router.push({ path: 'play' }).catch((err) => {
                throw new Error(`Problem handling push: ${err}.`);
            })
        });
    },

    // eslint-disable-next-line no-unused-vars
    sign_out(ctx, data) {
        console.log("emitting signout");
        window.vm.$socket.emit('signout', function () {
        });
    }
};

const mutations = {
    // eslint-disable-next-line no-shadow
    SET_CREDENTIALS(state, data) {
        state.username = data['username'];
        state.authorized = true;
    },

    SET_LANG(state, lang) {
        state.lang = lang;
    },

    SOCKET_UPDATE(state, room_session) {
        console.log("this is socket update");
        state.isConnected = true;
        state.room_session = room_session;
        state.room = room_session['name']
    },

    SOCKET_CONNECT(state) {
        state.isConnected = true;
    },

    SOCKET_DISCONNECT(state) {
        state.isConnected = false;
    },

    SET_LOADING(state, bool_var) {
        state.loading = bool_var
    },

    resetState (state) {
        Object.assign(state, getDefaultState())
    }
};

const getters = {
    // eslint-disable-next-line no-shadow
    authorized(state) {
        return state.authorized;
    },
    // eslint-disable-next-line no-shadow
    username(state) {
        return state.username;
    },

    credentials(state) {
        return {
            "user": state.username,
            "room": state.room
        }
    },

    room(state) {
        return state.room;
    },

    game_state(state) {
        if (state.isConnected) {
            return state.room_session['status'];
        } else {
            return 'unconnected';
        }
    },

    room_members() {
        return state.room_session.members;
    },

    loading() {
        return state.loading
    },

    dicts() {
        if (state.config === undefined) {
            return undefined
        } else {
            return Object.keys(state.config['AVAILABLE_DICT'])
        }
    },

    levels() {
        if (state.config === undefined) {
            return undefined
        } else {
            return Object.keys(state.config['AVAILABLE_DICT']['Complete russian']['subdicts'])
        }
    },

    words_left() {
        return state.room_session['pool'].length
    },

    last_hits() {
        return state.last_hits
    },

    player1() {
        let id = state.room_session['queue_id']
        return state.room_session['queue'][id][0]
    },

    player2() {
        let id = state.room_session['queue_id']
        return state.room_session['queue'][id][1]
    },

    online() {
        let onl = Array()
        for (const [key, value] of Object.entries(state.room_session['members'])) {
            if (value === 'online') {
                onl.push(key)
            }
        }
        return onl;
    },

    round_time() {
        return state.room_session['settings']['time'];
    },

    current_word() {
        return state.room_session['pool'][0]
    },

    last_statistics() {
        return state.room_session['last_statistics']
    },

    global_statistics() {
        return state.room_session['global_statistics']
    }
};

const store = new Vuex.Store({
    state,
    actions,
    mutations,
    getters
});

export default store;
