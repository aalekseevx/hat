import pytest


@pytest.mark.usefixtures("app")
def test_is_singleton(app):
    with app.app_context():
        from app.main.config_helper import get_dict_by_name
        obj1 = get_dict_by_name("Sample")
        obj2 = get_dict_by_name("Sample")
    assert obj1 is obj2
