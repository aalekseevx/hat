<i18n>
  en:
    room_users: "Users in the room"
    room: "Room"
    easy: "Easy"
    medium: "Medium"
    hard: "Hard"
    very_hard: "Very hard"
    difficulty: "Difficulty"
    select_difficulty: "Select difficulty"
    select_words_per: "Select words per player"
    select_time_per: "Select seconds for explanations per move"
    words_per: Words per person
    time_per: "One move duration in seconds"
    start: Start
    dictionary: Dictionary
    not_enough_online: "You can't play alone, can you?"
    statistics: Statistics
    show_last: "Show only last game statistics"
  ru:
    room_users: "Пользователи в комнате"
    room: Комната
    easy: "Легко"
    medium: "Средне"
    hard: "Сложно"
    very_hard: "Очень сложно"
    difficulty: "Сложность"
    select_difficulty: "Выберете сложность"
    select_words_per: "Выберете количество слов на человека в шляпе"
    select_time_per: "Выберите длительность одного хода в секундах"
    words_per: Количество слов на игрока
    time_per: Длительность в секундах
    start: "Начать"
    dictionary: Словарь
    not_enough_online: "Вы же не собираетесь играть один, да?"
    statistics: Статистика
    show_last: Статистика за последнюю игру
</i18n>

<template>
    <div>
    <ValidationObserver ref="observer">
        <div class="columns">
            <div class="column is-one-third">
                <div class="subtitle">
                    {{ $i18n.t("room_users") }}
                </div>
                <div class="list is-hoverable">
                    <span v-for="(status, user) in room_members" :key="user"
                          :class="{ 'online': status === 'online', 'offline': status === 'offline'}" class="list-item">
                        {{ user }}
                    </span>
                </div>
            </div>
            <div class="column">
                <div class="title">
                    {{ $i18n.t('room') }}
                    "<span>{{ room }}</span>"
                </div>

                <b-field :label="$i18n.t('dictionary')" style="margin-right: 20px">
                    <BSelectWithValidation name="dictionary" rules="required" v-model="c_dict" :placeholder="$i18n.t('select_dictionary')">
                        <option v-for="dict in dicts" :value="dict" :key="dict">{{ dict }}</option>
                    </BSelectWithValidation>
                </b-field>

                <b-field :label="$i18n.t('difficulty')" style="margin-right: 20px">
                    <BSelectWithValidation name="difficulty" rules="required" v-model="c_level" :placeholder="$i18n.t('select_difficulty')">
                        <option v-for="level in levels" :value="level" :key="level">{{ $i18n.t(level) }}</option>
                    </BSelectWithValidation>
                </b-field>

                <b-field :label="$i18n.t('words_per')" style="margin-right: 20px">
                    <BSelectWithValidation name="words_per" rules="required" v-model="c_words" :placeholder="$i18n.t('select_words_per')">
                        <option v-for="cnt in words_cnt" :value="cnt" :key="cnt">{{ cnt }}</option>
                    </BSelectWithValidation>
                </b-field>

                <b-field :label="$i18n.t('time_per')">
                    <BSelectWithValidation name="time_per" rules="required" v-model="c_time" :placeholder="$i18n.t('select_time_per')">
                        <option v-for="time in time_per" :value="time" :key="time">{{ time }}</option>
                    </BSelectWithValidation>
                </b-field>

                <b-button @click="init_game" type="is-primary is-large">{{ $i18n.t('start') }}</b-button>
            </div>
        </div>
    </ValidationObserver>
    <div class="title">
        {{ $t('statistics') }}
    </div>
    <b-field grouped group-multiline>
        <div class="control">
            <div class="container">
                <b-switch v-model="show_last"></b-switch>
                {{ $t('show_last') }}
            </div>
        </div>
    </b-field>
    <Statistics v-bind:data="show_last ? last_statistics : global_statistics"/>
    </div>
</template>

<style>
    .online {
        background-color: hsl(141, 53%, 53%) !important;
        color: white !important;
    }

    .offline {
        background-color: hsl(348, 100%, 61%) !important;
        color: white !important;
    }
</style>

<script>
    import {mapGetters} from "vuex";
    import BSelectWithValidation from "@/components/inputs/BSelectWithValidation";
    import {showError} from "@/utils";
    import {ValidationObserver} from "vee-validate";
    import Statistics from "@/components/play_stages/Statistics";
    export default {
        name: 'GameSetup',
        components: {
            BSelectWithValidation,
            ValidationObserver,
            Statistics
        },
        data() {
            return {
                show_last: false,
                c_level: null,
                c_words: null,
                c_time: null,
                c_dict: null,
                words_cnt: [
                    2,
                    5,
                    10,
                    15,
                    20,
                    30,
                    50,
                    100
                ],
                time_per: [
                    10,
                    15,
                    20,
                    30,
                    45,
                    60
                ],
                levels: [
                    "easy",
                    "medium",
                    "hard",
                    "very_hard"
                ]
            }
        },

        methods: {
            async do_validated_event(event, args=null) {
                await this.$refs.observer.validate();
                if (this.$refs.observer.flags.valid) {
                    if (args === null) {
                        window.vm.$socket.emit(event);
                    } else {
                        window.vm.$socket.emit(event, args);
                    }
                } else {
                    showError(this.$i18n.t('form_errors'));
                }
            },

            init_game() {
                let transfer_data = {
                    settings: {
                        "difficulty": this.c_level,
                        "words": this.c_words,
                        "time": this.c_time,
                        "dict": this.c_dict,
                    }
                }
                if (this.online.length <= 1) {
                    showError(this.$i18n.t('not_enough_online'));
                } else {
                    this.do_validated_event("init", transfer_data);
                }
            },
        },

        computed: {
            ...mapGetters([
                'room_members',
                'room',
                'dicts',
                'online',
                'last_statistics',
                'global_statistics'
            ]),
        }
    }
</script>
