import Vue from 'vue'
import Vuex from 'vuex'
import Buefy from 'buefy';
import VueI18n from 'vue-i18n'
import axios from 'axios'
import VueAxios from 'vue-axios'
import io from 'socket.io-client';
import VueSocketIO from 'vue-socket.io'
import VueTimers from 'vue-timers'

import App from './App.vue'
import router from './router';
import store from './store';

import 'buefy/dist/buefy.css';
import i18n from "@/translations";
import "./validation";

Vue.use(VueTimers)
Vue.use(VueAxios, axios);
Vue.use(VueI18n);
Vue.use(Buefy);
Vue.use(Vuex);

export const socketInstance = io();

Vue.use(new VueSocketIO({
    connection: socketInstance,
    vuex: {
        store,
    },
}));

const vm = new Vue({
    i18n,
    router,
    store,
    render: h => h(App),
}).$mount('#app');

window.vm = vm;
