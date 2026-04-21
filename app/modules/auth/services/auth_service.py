from app.models.usuario import Usuario
from sqlalchemy import or_

def login_user(identifier, password):
    user = Usuario.query.filter(
        (Usuario.username == identifier) |
        (Usuario.email == identifier)
    ).first()

    if not user:
        return None

    if not user.check_password(password):
        return None

    return user


def autenticar_usuario(identifier, password):
    user = Usuario.query.filter(
        or_(
            Usuario.username == identifier,
            Usuario.email == identifier
        )
    ).first()

    if user and user.check_password(password) and user.activo:
        return user

    return None


def obtener_redirect_por_rol(user):
    rol = user.tipo_usuario.nombre

    if rol == "ADMIN":
        return "main.dashboard"
    elif rol == "MODERADOR":
        return "main.dashboard"
    else:
        return "main.home"    