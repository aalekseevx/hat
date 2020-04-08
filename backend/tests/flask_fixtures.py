import pytest


@pytest.fixture(scope="module")
def app(request):
    from app import create_app
    app = create_app()
    print("Start app")

    # pushes an application context manually
    ctx = app.app_context()
    ctx.push()

    # bind the test life with the context through the
    request.addfinalizer(ctx.pop)
    return app


@pytest.fixture()
def test_client(request, app):

    client = app.test_client()
    client.__enter__()

    request.addfinalizer(
        lambda: client.__exit__(None, None, None))
    return client


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()


@pytest.fixture(autouse=True)
def app_context(app):
    """Creates a flask app context"""
    with app.app_context():
        yield app


@pytest.fixture
def request_context(app_context):
    """Creates a flask request context"""
    with app_context.test_request_context():
        yield


@pytest.fixture
def client(app_context):
    return app_context.test_client(use_cookies=True)
