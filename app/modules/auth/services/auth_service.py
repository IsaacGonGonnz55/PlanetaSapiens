from app.models.usuario import Usuario


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