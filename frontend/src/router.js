import Vue from 'vue';
import Router from 'vue-router';
// import store from './store';

import Help from './views/Help.vue'
import Index from './views/Index.vue'
import Login from './views/Login.vue'
import Play from './views/Play.vue'
import Policy from "@/views/Policy";

Vue.use(Router);

const router = new Router({
    routes: [
        {
            path: '/',
            name: 'Index',
            component: Index
        },
        {
            path: '/login',
            name: 'Login',
            component: Login
        },
        {
            path: '/play',
            name: 'Play',
            component: Play,
            meta: {
                requiresAuth: true
            }
        },
        {
            path: '/help',
            name: 'Help',
            component: Help
        },
        {
            path: '/policy',
            name: 'Policy',
            component: Policy
        }
    ]
});

// router.beforeEach((to, from, next) => {
//     console.log("resolving");
//     if (to.name === 'Play' && window.vm.$store.getters['Users/authorized']) {
//         console.log("guarding!");
//         next({path: '/login'});
//     }
//     else {
//         console.log("ok!");
//         next()
//     }
// });


export default router;
