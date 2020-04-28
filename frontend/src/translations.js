// Create VueI18n instance with options
import Vue from 'vue'
import VueI18n from 'vue-i18n'
import ru from "vee-validate/dist/locale/ru.json";
import en from "vee-validate/dist/locale/en.json";
Vue.use(VueI18n);


let i18n = new VueI18n({
    locale: 'ru', // set locale
    messages: {
        ru: {
            fields: {
                username: "Имя пользователя",
                room: "Комната",
                difficulty: "Сложность",
                words_per: "Количество слов",
                time_per: "Время в секундах на итерацию",
                dictionary: "Словарь"
            },
            validation: {
                ...ru.messages,
                "username_chars": "Используйте только английские буквы, цифры или символы '_', '-'",
                "room_exists": "Такая комната сейчас закрыта. Постучитесь потом."
            }
        },
        en: {
            fields: {
                username: "Username",
                room: "Room",
                difficulty: "Difficulty",
                words_per: "Number of words",
                time_per: "Time per iteration",
                dictionary: "Dictionary"
            },
            validation: {
                ...en.messages,
                "username_chars": "Use only english letters, digits and symbols '_', '-'",
                "room_exists": "Тhe room is closed now, knock later."
            }
        }
    }
});

export default i18n;
