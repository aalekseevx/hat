<template>
    <component :is="component"
               @go_set_user="go_set_user"
               @go_set_room="go_set_room"
               @create="create"
               @join="join"
               v-model="loginInfo"
               >
    </component>
</template>

<script>
    import i18n from "@/translations";
    import SetUsername from '../components/login_stages/SetUsername'
    import SetRoom from '../components/login_stages/SetRoom'
    import {mapActions} from "vuex";
    import store from "@/store";

    export default {
        name: 'Login',
        beforeRouteEnter (to, from, next) {
            if (store.getters.authorized) {
                next('/play')
            } else {
                next();
            }
        },
        data () {
            return {
                locale: i18n.locale,
                component: "SetUsername",
                loginInfo: {
                    username: null,
                    room: null
                }
            }
        },
        components: {
            SetUsername,
            SetRoom
        },
        methods: {
            go_set_user() {
                this.component = "SetUsername";
            },

            go_set_room() {
                this.component = "SetRoom";
            },

            ...mapActions(['create', 'join'])
        }
    }
</script>
