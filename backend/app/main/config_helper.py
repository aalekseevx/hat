from words_controller.dictionary import Dictionary, DictionaryInstance, SimpleDictionary
from flask import current_app as app


def get_dict_by_name(name: str) -> Dictionary:
    return Dictionary(f"{app.instance_path}/dictionaries_data/{app.config['AVAILABLE_DICT'][name]}")


def get_dict_by_lang(lang: str) -> Dictionary:
    return Dictionary(f"{app.instance_path}/dictionaries_data/{app.config['DEFAULT_DICT'][lang]}")


def get_dict_instance_by_name(name: str) -> DictionaryInstance:
    return DictionaryInstance(f"{app.instance_path}/dictionaries_data/{app.config['AVAILABLE_DICT'][name]}")


def get_dict_instance_by_lang(lang: str) -> DictionaryInstance:
    return DictionaryInstance(f"{app.instance_path}/dictionaries_data/{app.config['DEFAULT_DICT'][lang]}")


def get_simple_dict_by_name(name: str) -> Dictionary:
    return SimpleDictionary(**{'filename': f"{app.instance_path}/dictionaries_data/{app.config['SIMPLE_DICT'][name]}"})
