from flask import Flask
from config import config_instance


def create_app(config=config_instance()):
    app = Flask(__name__, template_folder="template", static_folder="static")
    app.config.from_object(config)


