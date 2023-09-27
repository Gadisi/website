

from flask import Flask
from src.config import config_instance

from src.utils import template_folder, static_folder


def create_app(config=config_instance()):
    app = Flask(__name__)
    app.template_folder = template_folder()
    app.static_folder = static_folder()
    app.config.from_object(config)

    with app.app_context():
        from src.routes.home import home_route
        app.register_blueprint(home_route)

    return app