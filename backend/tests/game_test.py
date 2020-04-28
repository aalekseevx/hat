import pytest


@pytest.mark.usefixtures("app")
@pytest.fixture
def Game_Controller(app):
    from app.main.game import GameController
    obj = GameController()
    return obj


@pytest.fixture
def Game_Controller_with_start(Game_Controller):
    players = ["usr1", "usr2", "usr3", "usr4", "usr5"]
    settings = {"time": 50, "words": 100, "difficulty": "medium", "dispersion": 40, "dict": "Sample"}
    Game_Controller.start_game_(players, settings)
    return Game_Controller


def test_start_game_(Game_Controller_with_start):
    assert Game_Controller_with_start.status == 'waiting_round'
    assert len(Game_Controller_with_start.word_dictionary) == 22579
    assert len(Game_Controller_with_start.pool) == 100 * len(Game_Controller_with_start.players)
    assert len(Game_Controller_with_start.queue) == 20


def test_start_round(Game_Controller_with_start):
    Game_Controller_with_start.start_round()
    assert len(Game_Controller_with_start.players) == 5
    assert Game_Controller_with_start.status == "playing"


def test_finish_round(Game_Controller_with_start):
    now_queue_id = Game_Controller_with_start.queue_id
    Game_Controller_with_start.start_round()
    Game_Controller_with_start.finish_round()
    assert Game_Controller_with_start.status == "waiting_round"
    assert (now_queue_id + 1) % len(Game_Controller_with_start.queue) == Game_Controller_with_start.queue_id


def test_circle_queue_id(Game_Controller_with_start):
    for i in range(1250):
        test_start_round(Game_Controller_with_start)
        test_finish_round(Game_Controller_with_start)


def test_remove_word(Game_Controller_with_start):
    first_len = len(Game_Controller_with_start.pool)
    Game_Controller_with_start.remove_word('mistake', 1.0)
    assert first_len == len(Game_Controller_with_start.pool) + 1
    for i in range(500 - 1):
        assert Game_Controller_with_start.status == 'waiting_round'
        now_len = Game_Controller_with_start.get_pool_size()
        Game_Controller_with_start.remove_word('correct', 1.0)
        assert now_len == Game_Controller_with_start.get_pool_size() + 1
    assert Game_Controller_with_start.status == "game_setup"
