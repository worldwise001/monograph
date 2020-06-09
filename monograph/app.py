import logging
import os

from flasgger import Swagger
from flask import Flask
import flask_login
from flask_cors import CORS

from monograph.api import ApiBlueprint

LOGGER = logging.getLogger(__name__)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def create_app() -> Flask:
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('urllib3.connectionpool').setLevel(level=logging.DEBUG)

    app = Flask(__name__)
    app.register_blueprint(ApiBlueprint())

    login_manager = flask_login.LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(username):
        if username != "admin":
            return

        user = User()
        user.id = user
        return user

    @login_manager.request_loader
    def request_loader(request):
        username = request.form.get('username')
        if username != "admin":
            return

        user = User()
        user.id = username

        user.is_authenticated = request.form['password'] == 'admin'

        return user

    CORS(app)
    Swagger(app, template_file=os.path.join(ROOT_DIR, 'swagger', 'template.yml'), parse=True,
            config={
                "headers": [],
                "specs": [
                    {
                        "endpoint": 'api/spec',
                        "route": '/api/spec',
                        "rule_filter": lambda rule: True,  # all in
                        "model_filter": lambda tag: True,  # all in
                    }
                ],
                "static_url_path": "/static/flasgger",
                "swagger_ui": True,
                "specs_route": "/spec"})

    LOGGER.info(app.url_map)

    return app


class User(flask_login.UserMixin):
    pass

