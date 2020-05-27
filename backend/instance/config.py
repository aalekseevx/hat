DEBUG = True

ROTATION = {
    "development": "500MB",
    "production": "1 week"
}

DEFAULT_DICT = {
    "ru": "dictionary_ru.txt",
    "en": "dictionary_ru.txt",
}

AVAILABLE_DICT = {
    "Complete russian": {
        "file": "dictionary_ru.txt",
        "subdicts": {
            "easy": (5645, 1, 34),
            "medium": (5645, 46, 12),
            "hard": (5645, 75, 25),
            "very_hard": (5645, 100, 25)
        }
    },
    "Sample": {
        "file": "dictionary_ru.txt",
        "subdicts": {
            "easy": (5645, 1, 34),
            "medium": (5645, 46, 12),
            "hard": (5645, 75, 25),
            "very_hard": (5645, 100, 25)
        }
    }
}

SIMPLE_DICT = {
    "Sample": "dictionary_sample.txt"
}
