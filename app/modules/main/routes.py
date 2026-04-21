from flask import render_template
from flask_login import login_required, current_user
from . import main_bp
from app.utils.decorators import requiere_permiso  # 🔥 IMPORT CLAVE



@main_bp.route("/")
def home():
    return render_template("public/main/home.html")


@main_bp.route("/acerca")
def acerca():
    return render_template("public/main/acerca.html")


@main_bp.route("/servicios")
def servicios():
    return render_template("public/main/servicios.html")


@main_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("private/dashboard/dashboard.html")


@main_bp.route("/admin")
@requiere_permiso("acceso_admin")
def admin():
    return "Panel Admin"