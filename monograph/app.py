import logging
import os

from flasgger import Swagger
from flask import Flask
from flask_cors import CORS

from monograph.api import ApiBlueprint

LOGGER = logging.getLogger(__name__)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def create_app() -> Flask:
    logging.basicConfig(level=logging.INFO)

    app = Flask(__name__)
    app.register_blueprint(ApiBlueprint())

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
                # "static_folder": "static",  # must be set by user
                "swagger_ui": True,
                "specs_route": "/spec/"})

    LOGGER.info(app.url_map)

    return app
