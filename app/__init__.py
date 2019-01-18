import os
from flask import Flask
from app.controller import (main, pwa)

def create_app():
    app = Flask(__name__,
                instance_relative_config=True,
                static_url_path='')
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY') or 'gwapo-ni-mamer',)

    app.register_blueprint(main.bp)
    app.register_blueprint(pwa.bp)

    return app
