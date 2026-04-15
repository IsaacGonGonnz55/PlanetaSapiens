from flask import Flask
from app.extensions.db import db
from app.extensions.migrate import migrate

def create_app():
    app = Flask(__name__)

    from app.config.config import Config
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app import models

    return app