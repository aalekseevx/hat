<i18n>
    en:
        words_left: "Words left:"
        last_hits: "Last round hits:"
        explains: "explains to"
        start: "Start"
    ru:
        words_left: "Слов осталось:"
        last_hits: "Угадано в последнем раунде:"
        explains: "объясняет"
        start: "Начать"
</i18n>

<template>
    <div class="has-text-centered" style="display: inline-block; width: 100%">
        <div class="has-text-centered">
            <b-tag type="is-primary is-large">{{ $t('words_left') }} {{ words_left }}</b-tag>
            <b-tag v-if="last_hits != null" type="is-info is-large">{{ $t('last_hits') }} {{ last_hits }}</b-tag>
        </div>
        <br/>
        <div class="has-text-centered is-fullwidth">
            <b-tag type="is-info is-large" style="margin-right: 5px">{{ player1 }} {{ $t('explains') }} {{ player2 }}</b-tag>
<!--            <b-tag type="is-info is-large" style="margin-right: 5px">{{ $t('explains') }}</b-tag>-->
<!--            <b-tag type="is-info is-large" style="margin-right: 5px">{{ player2 }}</b-tag>-->
        </div>
        <br/>
        <b-button class="is-large" @click="start_round" v-if="username === player1">{{ $t('start') }}</b-button>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex'
    export default {
        name: "WaitingRound",
        methods: {
            start_round() {
                window.vm.$socket.emit("start_round");
            }
        },
        computed: {
            ...mapGetters(["words_left", "last_hits", "player1", "player2", "username"])
        }
    }
</script>

<style scoped>

</style>
