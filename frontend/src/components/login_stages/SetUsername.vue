<i18n>
    en:
        introduce: Please, introduce yourself
        user_help: >
            During the game, you will be referred using the username. Users who play together must have
            different names. If you exit the room, you can join it back using the same username. Progress will
            be saved. System allows same usernames for players in different rooms.
        username: Username
        join: Join room
        create: Create room
        validation: Use only latin characters and digits. Should be 4-20 characters long.
        room_name: Room name
        form_errors: Please, fill in a form in a proper way
        legal_notice: "By filling out the form, you consent to the processing of your personal data."

    ru:
        introduce: Представьтесь, пожалуйста
        user_help: >
            Во время игры система будет обращаться к вам через Имя пользователя. Пользователи, которые будут
            играть вместе должны иметь различные имена. Если вы случайно выйдите из комнаты, вы можете вернуться,
            используя то же имя пользователя - весь прогресс сохранится. Система не запрещает иметь одинаковые
            имена пользователям в разных комнатах.
        username: Имя пользователя
        join: Присоединиться к комнате
        create: Создать комнату
        validation: "Используйте только латинские символы и цифры. Длина: 4-20 символов."
        room_name: "Имя комнаты"
        form_errors: "Пожалуйста, заполните поля в соотвествии с ограничениями"
        legal_notice: "Заполняя форму, вы даете согласие на обработку своих персональных данных."
</i18n>
<template>
    <ValidationObserver ref="observer">
        <div>
            <div class="title">
                {{ $t('introduce') }}
            </div>

            <div class="notification">
                {{ $t('user_help') }}
            </div>

            <b-field>
                <BInputWithValidation
                        rules="required|username_chars|min:4|max:20"
                        icon-pack="fas"
                        icon="user"
                        :label="$t('username')"
                        vid="username"
                        name="username"
                        v-model="username"
                        size="is-medium"
                        @input="handle_input"
                />
            </b-field>

            <div class="notification is-light">
                {{ $t('legal_notice')}}
            </div>

            <div class="buttons">
                <b-button type="is-primary" @click="go_set_room" class="is-medium">{{ $t('join') }}</b-button>
                <b-button type="is-primary" @click="create" class="is-medium">{{ $t('create') }}</b-button>
            </div>

        </div>
    </ValidationObserver>
</template>

<script>
    import {ValidationObserver} from "vee-validate";
    // import BSelectWithValidation from "./inputs/BSelectWithValidation";
    import BInputWithValidation from "../inputs/BInputWithValidation";
    import {showError} from '../../utils';
    // import BCheckboxesWithValidation from "./inputs/BCheckboxesWithValidation";


    export default {
        name: 'SetUsername',
        props: ['value'],
        data() {
            return {
                username: this.value['username'],
                room: this.value['room']
            }
        },

        components: {
            ValidationObserver,
            BInputWithValidation
        },

        methods: {
            async do_validated_event(event, args=null) {
                await this.$refs.observer.validate();
                if (this.$refs.observer.flags.valid) {
                    if (args === null) {
                        this.$emit(event);
                    } else {
                        this.$emit(event, args);
                    }
                } else {
                    showError(this.$i18n.t('form_errors'));
                }
            },

            async go_set_room() {
                this.do_validated_event('go_set_room')
            },

            async create() {
                this.do_validated_event('create', {
                    "username": this.username
                });
            },

            // eslint-disable-next-line no-unused-vars
            handle_input (_) {
                this.$emit('input', {
                    username: this.username,
                    room: this.room
                })
            },
        }
    }
</script>
