from words_controller.dictionary import Dictionary, DictionaryInstance
from functools import lru_cache
from flask import current_app as app


def get_dict_by_name(name: str) -> Dictionary:
    return Dictionary(f"{app.instance_path}/dictionaries_data/{app.config['AVAILABLE_DICT'][name]['file']}")


def get_dict_by_lang(lang: str) -> Dictionary:
    return Dictionary(f"{app.instance_path}/dictionaries_data/{app.config['DEFAULT_DICT'][lang]}")


def get_dict_instance_by_name(name: str) -> DictionaryInstance:
    return DictionaryInstance(f"{app.instance_path}/dictionaries_data/{app.config['AVAILABLE_DICT'][name]['file']}")


def get_dict_instance_by_lang(lang: str) -> DictionaryInstance:
    return DictionaryInstance(f"{app.instance_path}/dictionaries_data/{app.config['DEFAULT_DICT'][lang]}")


def get_simple_dict_(dict_name: str, numb: int, complexity: int, variation: int):
    c_dict = get_dict_by_name(dict_name)
    return c_dict.create_simple_dictionary(numb, complexity, variation)


@lru_cache(maxsize=None)
def get_simple_dict(dict_name: str, subdict_name: str):
    return get_simple_dict_(dict_name, *app.config['AVAILABLE_DICT'][dict_name]['subdicts'][subdict_name])