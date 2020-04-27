import Vue from 'vue';
import {ValidationProvider, extend, configure, localize} from 'vee-validate';
import {required, min, max} from "vee-validate/dist/rules";
import i18n from "./translations";
import api from "./api"

export function change_lang(lang) {
    localize(lang);
    configure({
        defaultMessage: (field, values) => {
            values._field_ = i18n.t(`fields.${field}`);
            return i18n.t(`validation.${values._rule_}`, values);
        }
    });
    localize(lang);
}

change_lang(i18n.locale);

extend("required", required);
extend("min", min);
extend("max", max);

extend('username_chars', value => {
    return RegExp("^[a-zA-Z0-9_-]*$").test(value);
});

extend('room_exists', async function (value) {
    const params = {
        room: value
    };
    let return_value = null
    await api().get('/check_existence', {
        params
    }).then(function (response) {
        return_value = response['data']['exists'];
    })
    return return_value;
});


// Register it globally
Vue.component('ValidationProvider', ValidationProvider);
