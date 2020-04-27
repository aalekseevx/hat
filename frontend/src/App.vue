<i18n>
    ru:
        cookie: Продолжая использовать сайт, вы соглашаетесь на сбор файлов cookie
    en:
        cookie: By continuing to use the site, you agree to the collection of cookies
</i18n>

<template>
    <div id="app">
        <Navbar/>
        <keep-alive>
            <div class="card is-fullwidth" style="margin: 10px">
                <div class="card-content">
                    <b-loading :active.sync="loading"></b-loading>
                    <keep-alive>
                        <router-view></router-view>
                    </keep-alive>
                </div>
            </div>
        </keep-alive>
        <Footer/>
    </div>
</template>

<script>
    import Navbar from './components/page_components/Navbar.vue'
    import Footer from './components/page_components/Footer.vue'
    import { mapGetters, mapMutations } from 'vuex'
    // import i18n from "@/translations";

    export default {
        name: 'App',
        components: {
            Navbar,
            Footer
        },
        sockets : {
            connect: function () {
                console.log('socket connected');
            },
            update: function (val) {
                console.log('receive update');
                this.$store.commit("SOCKET_UPDATE", val);
            }
        },
        beforeMount() {
            // this.$buefy.snackbar.open(this.$i18n.t('cookie'));
        },

        computed: {
            ...mapGetters([
                'loading',
            ])
        },

        methods: {
            ...mapMutations([
                'SET_LOADING',
            ])
        }
    }
</script>
