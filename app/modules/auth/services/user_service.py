from app.extensions.db import db
from app.models.usuario import Usuario
from app.models.tipo_usuario import TipoUsuario
from app.models.persona import Persona


def crear_usuario(username, email, password):

    if Usuario.query.filter(
        (Usuario.username == username) |
        (Usuario.email == email)
    ).first():
        return None

    tipo = TipoUsuario.query.filter_by(nombre="USUARIO").first()

    if not tipo:
        return None

    persona = Persona(
        nombre=username,
        apellido_paterno="",
        apellido_materno=""
    )

    db.session.add(persona)
    db.session.flush()

    user = Usuario(
        username=username,
        email=email,
        persona_id=persona.id,
        tipo_usuario_id=tipo.id
    )

    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return user