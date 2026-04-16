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

    from app.modules.main import main_bp
    from app.modules.auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    from datetime import datetime

    @app.context_processor
    def inject_global_variables():
        return {
            "current_year": datetime.utcnow().year
        }


    return app