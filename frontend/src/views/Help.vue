<i18n>
  en:
    rules: "There is no rules now, but you can read them    "
    here: here
  ru:
    rules: "Пока правила не готовы, но вы можете прочитать их "
    here: здесь
</i18n>

<template>
    <div>
        <div class="title is-12">
            <section class="hero is-medium">
                <div class="hero-body">
                    {{ $t('rules') }}
                    <a href="http://thehat.ru/rules/">{{ $t('here') }}</a>
                </div>
            </section>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Help',
        components: {},
        data() {
            return {
            }
        }
    }
</script>
