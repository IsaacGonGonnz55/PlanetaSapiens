from flask import render_template
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

