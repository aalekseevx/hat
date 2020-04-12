import pytest


@pytest.mark.usefixtures("app")
def test_is_singleton(app):
    with app.app_context():
        from app.main.config_helper import get_dict_by_name
        obj1 = get_dict_by_name("Sample")
        obj2 = get_dict_by_name("Sample")
    assert obj1 is obj2


@pytest.fixture
def create_dict(app):
    from app.main.config_helper import get_dict_by_name
    obj = get_dict_by_name("Sample")
    return obj


def test_add_word(create_dict):
    init_len = len(create_dict)
    create_dict.add_word('Москва', 12)  # нет городов в словаре -> точная гарантия добавления
    assert ('Москва' in create_dict.word_list)
    assert ('Москва' in create_dict.dictionary.keys())
    assert init_len + 1 == len(create_dict)
    create_dict.add_word('Москва', 12)
    assert init_len + 1 == len(create_dict)


def test_del_word(create_dict):
    init_len = len(create_dict)
    create_dict.del_word('сон')
    assert 'сон' not in create_dict.word_list
    assert 'сон' not in create_dict.dictionary.keys()
    assert init_len - 1 == len(create_dict)
    create_dict.del_word('сон')
    assert init_len - 1 == len(create_dict)


def test_del_random_word(create_dict):
    init_len = len(create_dict)
    word = create_dict.pop_random_word()
    assert word not in create_dict.word_list
    assert word not in create_dict.dictionary.keys()
    assert init_len - 1 == len(create_dict)
    assert type(word) == str


@pytest.fixture
def create_immutable_dict():
    from app.main.config_helper import get_dict_instance_by_name
    obj = get_dict_instance_by_name("Sample")
    return obj


def test_get_dict_for_game(create_immutable_dict):
    a = create_immutable_dict.get_dict_for_game(3000, 10, 1)  # проверка расширения границ
    assert len(a) == 3000
    assert type(a) == dict
    b = create_immutable_dict.get_dict_for_game(30000, 50, 50)  # берем больше, чем в словаре. в нем 22580
    assert len(b) == 22580


from words_controller.dictionary import SimpleDictionary


def test_create_simple_from_instance_dictionary(create_dict):
    simple_dict = create_dict.create_simple_dictionary(1000, 10, 1)
    assert type(simple_dict) == SimpleDictionary
    assert len(simple_dict) == 1000


@pytest.fixture
def create_simple_dict():
    from app.main.config_helper import get_simple_dict_by_name
    obj = get_simple_dict_by_name("Sample")
    return obj


def test_simple_initializtion():
    word_list = ["заяц0", "заяц1", "заяц2"]
    dictionary = SimpleDictionary(**{'dictionary': word_list})
    assert len(dictionary) == 3
    for i in range(3):
        assert f'заяц{str(i)}' in dictionary.word_list


def test_simple_get_dict_for_game(create_simple_dict):
    dictionary = create_simple_dict.get_dict_for_game(500)
    assert type(dictionary) == list
    assert len(dictionary) == 500


def test_simple_add_word(create_simple_dict):
    init_len = len(create_simple_dict)
    create_simple_dict.add_word('Москва')
    assert 'Москва' in create_simple_dict.word_list
    assert init_len + 1 == len(create_simple_dict)
    create_simple_dict.add_word('Москва')
    assert init_len + 1 == len(create_simple_dict)


def test_simple_del_word(create_simple_dict):
    init_len = len(create_simple_dict)
    assert 'такси' in create_simple_dict.word_list
    create_simple_dict.del_word('такси')
    assert 'такси' not in create_simple_dict.word_list
    assert init_len - 1 == len(create_simple_dict)
    create_simple_dict.del_word('такси')
    assert init_len - 1 == len(create_simple_dict)