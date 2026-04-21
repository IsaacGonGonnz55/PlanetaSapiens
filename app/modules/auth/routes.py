from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth_bp
from app.modules.auth.services.auth_service import autenticar_usuario
from app.modules.auth.services.auth_service import obtener_redirect_por_rol


#  LOGIN
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        identifier = request.form.get("identifier")
        password = request.form.get("password")
        remember = True if request.form.get("remember") else False

        user = autenticar_usuario(identifier, password)

        if user:
            login_user(user, remember=remember)
            return redirect(url_for(obtener_redirect_por_rol(user)))

            return redirect(url_for("main.home"))

        flash("Credenciales inválidas", "danger")

    return render_template("public/auth/login.html")


#  REGISTER
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm_password")

        # Validación
        if password != confirm:
            flash("Las contraseñas no coinciden", "danger")
            return redirect(url_for("auth.register"))

        from app.modules.auth.services.user_service import crear_usuario

        user = crear_usuario(
            username=username,
            email=email,
            password=password
        )

        if not user:
            flash("El usuario o email ya existe", "danger")
            return redirect(url_for("auth.register"))

        flash("Cuenta creada correctamente", "success")
        return redirect(url_for("auth.login"))

    return render_template("public/auth/register.html")


# 🚪 LOGOUT
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))