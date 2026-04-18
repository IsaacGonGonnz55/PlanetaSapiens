from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth_bp
from app.modules.auth.services.auth_service import autenticar_usuario



@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    if request.method == "POST":
        identifier = request.form.get("identifier")
        password = request.form.get("password")

        user = autenticar_usuario(identifier, password)

        if user:
            login_user(user)
            return redirect(url_for("main.dashboard"))

        flash("Credenciales inválidas", "danger")

    return render_template("public/auth/login.html")


# 📝 REGISTER (vista simple por ahora)
@auth_bp.route("/register")
def register():
    return render_template("public/auth/registro.html")


# 🚪 LOGOUT
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))