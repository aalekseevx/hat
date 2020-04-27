<i18n>
    en:
        correct: Correct
        give_up: Give up
        mistake: Mistake
        explains: explains to
        sn1: "EXPLANATION IS NOW BANNED!"
        sn2: "ANSWERS ARE NOT ACCEPTED ANYMORE. Please select, if the last answer was correct."
    ru:
        correct: Угадано
        give_up: Сдаться
        mistake: Ошибка
        explains: "объясняет"
        sn1: "ДАЛЬНЕЙШЕЕ ОБЪЯСНЕНИЕ ЗАПРЕЩЕНО"
        sn2: "ОТВЕТЫ БОЛЬШЕ НЕ ПРИНИМАЮТСЯ. Пожалуйста отметьте, был ли последний ответ верен."
</i18n>

<template>
    <div>
        <b-progress :value="since" :max="round_time * 1000"></b-progress>
        <div class="has-text-centered" style="width: 100%">
            <div class="has-text-centered is-fullwidth">
                {{ player1 }} {{ $t('explains') }} {{ player2 }}
<!--                <b-tag type="is-medium" style="margin-right: 5px"></b-tag>-->
<!--                <b-tag type="is-medium" style="margin-right: 5px"></b-tag>-->
<!--                <b-tag type="is-medium" style="margin-right: 5px"></b-tag>-->
            </div>
        <div v-if="username === player1">
            <br/>
<!--            <div class="tag is-large " style="height:70px; padding: 20px">-->
                <div class="is-12" style="font-size: 35px">
                    {{ current_word }}
<!--                </div>-->
            </div>
                <br/>
                <br/>
                <div class="has-text-centered">
                    <b-button @click="mistake_word" class="is-danger is-large" style="margin-right: 10px; margin-bottom: 10px">{{ $t('mistake') }}</b-button>
                    <b-button @click="end_round" class="is-large" style="margin-right: 10px; margin-bottom: 10px">{{ $t('give_up') }}</b-button>
                    <b-button @click="accept_word" class="is-success is-large" style="margin-right: 10px; margin-bottom: 10px">{{ $t('correct') }}</b-button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex'
    import 'vue-timers'
    export default {
        name: "Explanation",
        data: function() {
            return {
                start_time: new Date().getTime(),
                since: 0,
                last_word_shown: new Date().getTime(),
                sn1: false,
                sn2: false
            }
        },
        timers: {
            progress_checker: {
                time: 50,
                autostart: true,
                repeat: true
            }
        },
        methods: {
            progress_checker() {
                this.since = new Date().getTime() - this.start_time;
                if (!this.sn1 && this.round_time * 1000 - this.since < 0) {
                    this.sn1 = true;
                    this.$buefy.toast.open({
                        duration: 2000,
                        message: this.$i18n.t('sn1'),
                        position: 'is-bottom',
                        type: 'is-danger'
                    })
                }

                if (!this.sn2 && this.round_time * 1000 - this.since < -3000) {
                    this.sn2 = true;
                    this.$buefy.toast.open({
                        duration: 10000,
                        message: this.$i18n.t('sn2'),
                        position: 'is-bottom',
                        type: 'is-danger'
                    })
                }
            },


            commit_event(verdict, finish_round=false) {
                window.vm.$socket.emit("remove_word", {
                    verdict,
                    finish_round,
                    "screen_time": new Date().getTime() - this.last_word_shown,
                });
            },

            accept_word() {
                this.commit_event("correct", this.round_time * 1000 - this.since < 3000);
                this.last_word_shown = new Date().getTime()
            },

            mistake_word() {
                this.commit_event("mistake");
            },

            end_round() {
                this.commit_event("timeout");
            }
        },
        computed: {
            ...mapGetters(["round_time", "current_word", "username", "player1", "player2"])
        }
    }
</script>

<style scoped>

</style>
