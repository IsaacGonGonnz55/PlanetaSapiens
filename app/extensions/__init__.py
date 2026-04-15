from flask import Flask

from app.extensions.db import db
from app.extensions.migrate import migrate

def create_app():
    app = Flask(__name__)

    # Configuración
    from app.config.config import Config
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    return app