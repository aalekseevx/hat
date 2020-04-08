from . import main


@main.route('/')
def hello_world():
    return "Hat Backend service is UP."
