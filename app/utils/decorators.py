from functools import wraps
from flask_login import current_user
from flask import redirect, url_for, flash


def requiere_permiso(nombre_permiso):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):

            if not current_user.is_authenticated:
                return redirect(url_for("auth.login"))

            if not current_user.tiene_permiso(nombre_permiso):
                flash("No tienes permisos", "danger")
                return redirect(url_for("main.home"))

            return f(*args, **kwargs)

        return wrapper
    return decorator