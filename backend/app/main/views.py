from . import main
from flask import jsonify
from flask import current_app as c_app


@main.route('/')
def hello_world():
    return "Hat Backend service is UP."


@main.route('/config')
def config_get():
    return jsonify({
        'AVAILABLE_DICT': c_app.config['AVAILABLE_DICT']
    })
