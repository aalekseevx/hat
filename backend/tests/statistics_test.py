import pytest


@pytest.mark.usefixtures("app")
@pytest.fixture
def PartyStatistics(app):
    from app.main.statistics import PartyStatistics
    users = ["usr1", "usr2", "usr3"]
    words = ["сок", "банан", "сыр"]
    obj = PartyStatistics(users, words)
    return obj


def test_add_objects(PartyStatistics):
    PartyStatistics.add_objects(["usr4"], ["сок"])
    assert len(PartyStatistics.inside) == 4
    assert len(PartyStatistics.user_statistics) == 4
    assert len(PartyStatistics.words_statistics) == 3
    PartyStatistics.add_objects(["usr1"], ["генератор"])
    assert len(PartyStatistics.inside) == 4
    assert len(PartyStatistics.user_statistics) == 4
    assert len(PartyStatistics.words_statistics) == 4


def test_add_result(PartyStatistics):
    PartyStatistics.add_result("usr1", "usr3", "сок", 'correct', 2.0)
    assert PartyStatistics.user_statistics["usr1"].points == 1
    assert PartyStatistics.user_statistics["usr1"].explanations == 1
    assert PartyStatistics.user_statistics["usr1"].guesses == 0
    assert PartyStatistics.user_statistics["usr1"].mistakes == 0
    assert PartyStatistics.user_statistics["usr3"].points == 1
    assert PartyStatistics.user_statistics["usr3"].explanations == 0
    assert PartyStatistics.user_statistics["usr3"].guesses == 1
    assert PartyStatistics.words_statistics["сок"].tries == 1
    assert PartyStatistics.words_statistics["сок"].screen_time == 2.0
    PartyStatistics.add_result("usr1", "usr3", "сок", 'mistake', 3.0)
    assert PartyStatistics.user_statistics["usr1"].points == 0
    assert PartyStatistics.user_statistics["usr1"].mistakes == 1
    assert PartyStatistics.user_statistics["usr3"].points == 1
    assert PartyStatistics.words_statistics["сок"].tries == 2
    assert PartyStatistics.words_statistics["сок"].screen_time == 5.0


def test_get(PartyStatistics):
    PartyStatistics.add_result("usr1", "usr3", "сок", 'correct', 2.0)
    PartyStatistics.add_result("usr1", "usr3", "сок", 'mistake', 3.0)
    stats_dictionary = PartyStatistics.get()
    assert stats_dictionary["users"][0]["username"] == "usr3"
    assert stats_dictionary["words"][0]['word'] == "сок"
