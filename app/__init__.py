from flask import Flask, request, redirect, url_for
from app.extensions.db import db
from app.extensions.migrate import migrate
import click
from app.modules.auth.services.seed_service import seed_all
from app.extensions.login_manager import login_manager
from app.models.usuario import Usuario
from flask_login import current_user
from app.modules.auth.services.session_service import crear_sesion_anonima


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


    @app.before_request
    def before_request_global():

        
        if request.endpoint != "static":
            crear_sesion_anonima()

        # 🔹 2. Proteger rutas
        rutas_publicas = [
            "main.home",
            "main.acerca",
            "main.servicios",
            "auth.login",
            "auth.register",
            "static"
        ]

        if request.endpoint not in rutas_publicas:
            if not current_user.is_authenticated:
                return redirect(url_for("auth.login"))             


    return app