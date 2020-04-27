<template>
    <div>
        <Waiting v-if="game_state === 'unconnected'"></Waiting>
        <GameSetup v-if="game_state === 'game_setup'"></GameSetup>
        <WaitingRound v-if="game_state === 'waiting_round'"></WaitingRound>
        <Explanation v-if="game_state === 'playing'"></Explanation>
    </div>
</template>

<script>
    import store from "@/store";
    import Waiting from '../components/play_stages/Waiting'
    import GameSetup from "../components/play_stages/GameSetup";
    import { mapGetters } from 'vuex'
    import WaitingRound from "@/components/play_stages/WaitingRound";
    import Explanation from "@/components/play_stages/Explanation";

    export default {
        name: 'Play',
        components: {
            Explanation,
            Waiting,
            GameSetup,
            WaitingRound
        },
        beforeRouteEnter (to, from, next) {
            if (!store.getters.authorized) {
                next('/login')
            } else {
                next();
            }
        },
        data() {
            return {

            }
        },
        computed: {
            ...mapGetters([
                'game_state',
                'username',
            ])
        }
    }
</script>
