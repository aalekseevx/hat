<i18n>
  en:
    waiting: "Please wait, your room is being created..."
  ru:
    waiting: "Пожалуйста, подождите. Комната вот-вот откроется."
</i18n>

<template>
    <div class="title is-12">
        <section class="hero is-medium">
            <div class="hero-body">
                {{ $t('waiting') }}
            </div>
        </section>
    </div>
</template>

<script>
    export default {
        name: 'Waiting',
        components: {},
        data() {
            return {
            }
        }
    }
</script>
