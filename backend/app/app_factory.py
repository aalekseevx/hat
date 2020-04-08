import os
import sys

from flask import Flask
from flask_socketio import SocketIO
from loguru import logger
import logging

socket_io = SocketIO()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY', 'sample_secret'),
        DEBUG=os.getenv('SECRET_KEY', False)
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        from .main import main as main_blueprint
        app.register_blueprint(main_blueprint)

    socket_io.init_app(app)

    def setup_logger():
        logger.remove(0)
        level = 'DEBUG' if app.config['DEBUG'] else 'INFO'
        logger.add(sys.stdout, level=level)

        class PropagateHandler(logging.Handler):
            def emit(self, record):
                logging.getLogger("gunicorn.error").handle(record)

        logger.remove()
        logger.add(PropagateHandler(), format="{message}")

        logger.add(f"{app.instance_path}/logs/{app.config['ENV']}.log",
                   rotation=app.config['ROTATION'][app.config['ENV']])

        logger.success("Logger was set up.")

    setup_logger()

    logger.info("App created with configuration:")
    configuration = app.config
    configuration['SECRET_KEY'] = '[ HIDDEN BY LOGGER ]'
    for key, value in configuration.items():
        logger.info(f"{key}: {value}")

    return app
