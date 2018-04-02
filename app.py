import settings
from flask import Flask
from common.session_utils import RedisSessionInterface


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    app.session_interface = RedisSessionInterface()

    return app
