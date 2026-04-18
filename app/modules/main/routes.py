from flask import render_template
from flask_login import login_required, current_user
from . import main_bp



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
    return render_template("private/main/dashboard.html")