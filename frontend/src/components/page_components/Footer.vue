<i18n>
  en:
    author1: "Aleksandr Alekseev"
    author2: "Aleksandr Pechonkin"
    under_lic: The source code is licensed
    lic: BSD 3-Clause "New" or "Revised" Licence
    by: by
    privacy: Privacy policy
    cookie: By continuing to use the site, you agree to the collection of cookies
  ru:
    author1: "Александром Алексеевым"
    author2: "Александром Печёнкиным"
    under_lic: Исходный код распространяется под
    lic: «Новой» лицензией BSD
    by: разработана
    privacy: Политика в отношении обработки персональных данных
    cookie: Продолжая использовать сайт, вы соглашаетесь на сбор файлов cookie
</i18n>

<template>
    <footer class="footer">
        <div class="content has-text-centered">
            <p>
                <strong>{{ $t('name') }}</strong> {{ $t('by') }} <a href="https://github.com/aalekseevx/">{{ $t('author1') }}</a> and <a
                    href="https://github.com/Piachonkin-Alex">{{ $t('author2') }}</a>. {{ $t('under_lic') }}
                <a href="https://github.com/aalekseevx/mipt-tp-game/blob/master/LICENSE">{{ $t('lic') }}</a>.

                <br/>
                <br/>
                <router-link to="/policy">{{ $t('privacy')}}</router-link>
                <br/>
                <span>{{ $t('cookie')}}</span>

                <br/>
                <br/>

                <a href="https://github.com/aalekseevx/mipt-tp-game/" class="button is-medium">
                    <b-icon
                            pack="fab" icon="github"
                    >
                    </b-icon>
                </a>
            </p>
        </div>
    </footer>
</template>

<script>
    import commonMessage from "@/common_locales";

    export default {
        name: 'Footer',
        i18n: {
            sharedMessages: commonMessage
        }
    };
</script>

<style scoped>
</style>
