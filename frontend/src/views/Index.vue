<i18n>
en:
  message: "The Hat is a game about words explanations. Now even during social distancing!"
  sub_message: "Connect via your favourite voice call service, create a room and play!"
  play: "Play"
  rules: "Read the rules"
ru:
  message: "Шляпа - это игра на объяснение слов. Теперь и на самоизоляции!"
  sub_message: "Подключайтесь по вашей любимой голосовой связи, создайте уютную комнату и вперёд!"
  play: "Играть"
  rules: "Прочитать правила"
</i18n>

<template>
    <div>
        <div class="title is-12">
            <section class="hero is-primary is-light is-medium">
                <div class="hero-body">
                    <h1 class="title">
                        {{ $t('message') }}
                    </h1>
                    <h1 class="subtitle">
                        {{ $t('sub_message') }}
                    </h1>
                    <div class="buttons">
                        <b-button class="is-light is-large" tag="router-link" to="/play">{{ $t('play') }}</b-button>
                        <b-button class="is-light is-large" tag="router-link" to="/help">{{ $t('rules') }}</b-button>
                    </div>
                </div>
            </section>
        </div>
    </div>
</template>

<script>
    import i18n from "@/translations";
    export default {
        name: 'Index',
        data () {
            return { locale: i18n.locale }
        }
    }
</script>
