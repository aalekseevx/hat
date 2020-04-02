from dictionary import Dictionary

DEBUG = True
SECRET_KEY = 'sample_secret'

DEFAULT_DICT = {
    "rus": "dictionary_ru.txt",
    "eng": "dictionary_ru.txt",
}

AVAILABLE_DICT = {
    "Complete russian": Dictionary("dictionary_ru.txt")
}
