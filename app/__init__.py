from flask import Flask
from app.extensions.db import db
from app.extensions.migrate import migrate
import click
from app.modules.auth.services.seed_service import seed_all
from app.extensions.login_manager import login_manager
from app.models.usuario import Usuario

def create_app():
    app = Flask(__name__)

    from app.config.config import Config
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)



    from app import models

    from app.modules.main import main_bp
    from app.modules.auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    from datetime import datetime
    @app.context_processor
    def inject_globals():
        return {
            'current_year': datetime.now().year
        }
    
        # 🔥 COMANDO CLI AQUÍ
    @app.cli.command("seed")
    def seed():
        """Inicializa datos del sistema"""
        seed_all()

   

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))
        


    return app