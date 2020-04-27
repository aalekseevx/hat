<i18n>
  en:
    play: "Play"
    rules: "Rules"
    sign-out: "Sign out"
    game_over: "Interrupt the game"
    stopping: "Stopping the game"
    stopping_msg: "Are you sure that you want to interrupt the game? It will stop the game for everyone in the room."
  ru:
    play: "Играть"
    rules: "Правила"
    sign-out: "Выйти"
    game_over: "Прервать игру"
    stopping: "Прерываниие игры"
    stopping_msg: "Вы уверены, что хотите прервать игру? Это прекратит игру для всех в комнате"
</i18n>

<template>
    <nav class="navbar">
        <div class="navbar-brand">
            <router-link class="navbar-item" to="/">
                <b-icon pack="fab" icon="redhat" size="is-medium" class="logo"/>
                <h1 class="title is-9">{{ $t('name') }}</h1>
            </router-link>
            <a role="button"
               :class="['navbar-burger', {'is-active': activeBurger}]"
               @click="activeBurger = !activeBurger"
               aria-label="menu" aria-expanded="false"
            >
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>
        <div :class="['navbar-menu', {'is-active': activeBurger}]">
            <div class="navbar-start">
                <router-link class="navbar-item" to="/play">
                    {{ $t('play') }}
                </router-link>
                <router-link class="navbar-item" to="/help">
                    {{ $t('rules') }}
                </router-link>
            </div>
            <div class="navbar-end">
                <div class="navbar-item">
                    <div>
                        <div class="buttons">
                            <div v-if="authorized" style="padding-top: 9px; padding-right: 10px">
                                <b-button @click="signout" icon-pack="fas" icon-left="sign-out-alt">{{ $t('sign-out') }}</b-button>
                                <router-link to="/play" style="padding-right: 10px">
                                    <b-button icon-pack="fas" :icon-left="icon_user">{{ credentials['user'] }}</b-button>
                                </router-link>
                                <router-link to="/play" style="padding-right: 10px">
                                    <b-button icon-pack="fas" :icon-left="icon_room">{{ credentials['room'] }}</b-button>
                                </router-link>
                                <b-button v-if="game_state !== 'game_setup'" @click="game_over" icon-pack="fas" icon-left="power-off">{{ $t('game_over') }}</b-button>
                            </div>
                            <b-select placeholder="Language" v-model="locale" icon="language" icon-pack="fas">
                                <option value="en">English</option>
                                <option value="ru">Russian</option>
                            </b-select>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
    import i18n from "@/translations";
    import {change_lang} from "@/validation";
    import commonMessage from '../../common_locales';
    import {mapMutations, mapActions, mapGetters} from 'vuex'
    import router from "@/router";

    export default {
        name: 'Navbar',
        data() {
            return {
                locale: i18n.locale,
                userActive: false,
                roomActive: false,
                icon_user: "user",
                icon_room: "house-user",
                    activeBurger: false,
            }
        },
        methods: {
            ...mapMutations({
                'SET_LANG': 'SET_LANG',
                "resetState": 'resetState'
            }),
            ...mapActions({
                "action_sign_out": "sign_out"
            }),

            signout() {
                this.action_sign_out();
                this.resetState();
                router.push('/login')
            },

            game_over() {
                this.$buefy.dialog.confirm({
                    title: this.$i18n.t('stopping'),
                    message: this.$i18n.t('stopping_msg'),
                    confirmText: this.$i18n.t('game_over'),
                    type: 'is-danger',
                    hasIcon: true,
                    iconPack: "fas",
                    icon: "power-off",
                    onConfirm: () => {
                        window.vm.$socket.emit("endgame");
                    }
                })
            }
        },
        watch: {
            locale(val) {
                i18n.locale = val;
                change_lang(val);
            }
        },
        i18n: {
            sharedMessages: commonMessage
        },
        computed: {
            ...mapGetters(['authorized', 'credentials', 'game_state'])
        }
    };
</script>

<style scoped>
    .logo {
        margin-right: 5px;
    }
</style>
