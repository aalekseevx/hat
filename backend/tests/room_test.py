import pytest


@pytest.mark.usefixtures("app")
@pytest.fixture
def room(app):
    from app.main.room import Room
    obj = Room("комната", "usr1", "русский")
    return obj


def test_join(room):
    assert len(room.members) == 1
    room.join("usr2")
    assert len(room.members) == 2
    room.join("usr2")
    assert len(room.members) == 2
    assert room.members["usr2"] == "online"


def test_leave(room):
    assert room.members["usr1"] == "online"
    room.leave("usr1")
    assert room.members["usr1"] == "offline"


def test_make_offline(room):
    assert room.members["usr1"] == "online"
    room.make_offline("usr1")
    assert room.members["usr1"] == "offline"


def test_online(room):
    for i in range(10):
        room.join(f'usr{i}')
    for i in range(10, 2):
        room.leave(f'usr{i}')
    online_list = room.online()
    for i in range(10, 2):
        assert f'usr{i}' not in online_list
        assert f'usr{i + 1}' in online_list


def test_start_game(room):
    for i in range(10):
        room.join(f'usr{i}')
    room.make_offline("usr0")
    settings = {"time": 50, "words": 100, "difficulty": 30, "dispersion": 40, "dict": "Sample"}
    room.start_game(settings)
    for i in range(1, 10):
        assert f'usr{i}' in room.players
    assert "usr0" not in room.players


def test_get_broadcast_data(room):
    data = room.get_broadcast_data()
    assert len(data) == 11 # number of different info
