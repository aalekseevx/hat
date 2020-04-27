<i18n>
    en:
        statistics: Statistics
        empty: Still no statistics
        users: Users
        words: Words
        word: Word
        tries: Tries
        time: Explanation time
        result: Result
        username: Username
        explanations: Explanations
        guesses: Guesses
        mistakes: Mistakes
        points: Points
    ru:
        statistics: Статистика
        empty: Статистики ещё нет
        users: Пользователи
        words: Слова
        word: Слово
        tries: Попытки
        time: Время на объяснение
        result: Результат
        username: Пользователь
        explanations: Слов объяснено
        guesses: Слов угадано
        mistakes: Ошибок при объяснении
        points: Очков
</i18n>

<template>
    <div>
        <b-tabs>
            <b-tab-item :label="$t('users')" icon-pack="fas" icon="users">
                <b-table
                        :data="data['users']"
                        :bordered="true"
                        :striped="true"
                        :hoverable="true"
                        :mobile-cards="true">

                    <template slot-scope="props">
                        <b-table-column field="username" :label="$t('username')">
                            {{ props.row.username }}
                        </b-table-column>

                        <b-table-column field="explanations" :label="$t('explanations')">
                            {{ props.row.explanations }}
                        </b-table-column>

                        <b-table-column field="guesses" :label="$t('guesses')">
                            {{ props.row.guesses }}
                        </b-table-column>

                        <b-table-column field="mistakes" :label="$t('mistakes')">
                            {{ props.row.mistakes }}
                        </b-table-column>

                        <b-table-column field="points" :label="$t('points')">
                            {{ props.row.points }}
                        </b-table-column>
                    </template>

                    <template slot="empty">
                        <section class="section">
                            <div class="content has-text-grey has-text-centered">
                                <p>
                                    <b-icon
                                            icon="heart-broken"
                                            pack="fas"
                                            size="is-large">
                                    </b-icon>
                                </p>
                                <p>{{ $t('empty') }}</p>
                            </div>
                        </section>
                    </template>
                </b-table>
            </b-tab-item>
            <b-tab-item :label="$t('words')" icon-pack="fas" icon="language">
                <b-table
                        :data="data['words']"
                        :bordered="true"
                        :striped="true"
                        :hoverable="true"
                        :mobile-cards="true">

                    <template slot-scope="props">
                        <b-table-column field="word" :label="$t('word')">
                            {{ props.row.word }}
                        </b-table-column>

                        <b-table-column field="tries" :label="$t('tries')">
                            {{ props.row.tries }}
                        </b-table-column>

                        <b-table-column field="time" :label="$t('time')">
                            {{ toMMSS(props.row.screen_time) }}
                        </b-table-column>

                        <b-table-column field="mistake" :label="$t('result')" width="40">
                            <b-icon pack="fas" :icon="!props.row.mistake ? 'check' : 'times'"></b-icon>
                        </b-table-column>
                    </template>

                    <template slot="empty">
                        <section class="section">
                            <div class="content has-text-grey has-text-centered">
                                <p>
                                    <b-icon
                                            icon="heart-broken"
                                            pack="fas"
                                            size="is-large">
                                    </b-icon>
                                </p>
                                <p>{{ $t('empty') }}</p>
                            </div>
                        </section>
                    </template>
                </b-table>
            </b-tab-item>
        </b-tabs>
    </div>
</template>

<script>
    export default {
        name: "Statistics",
        data: function () {
            return {
                show_last: false
            }
        },
        methods: {
            toMMSS: function (str) {
                let sec_num = Math.round(parseInt(str, 10) / 1000.0) ;
                let hours   = Math.floor(sec_num / 3600);
                let minutes = Math.floor((sec_num - (hours * 3600)) / 60);
                let seconds = sec_num - (hours * 3600) - (minutes * 60);

                if (hours   < 10) {hours   = "0"+hours;}
                if (minutes < 10) {minutes = "0"+minutes;}
                if (seconds < 10) {seconds = "0"+seconds;}
                return minutes+':'+seconds;
            }
        },
        props: ['data'],
    }
</script>

<style scoped>

</style>
