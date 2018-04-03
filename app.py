import settings
from flask import Flask
from common.session_utils import RedisSessionInterface
from accounts.routes import bp_account
from chat.routes import bp_chat


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    app.session_interface = RedisSessionInterface()

    app.register_blueprint(bp_account)
    app.register_blueprint(bp_chat)

    return app
