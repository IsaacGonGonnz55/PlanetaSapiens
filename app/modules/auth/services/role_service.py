from app.extensions.db import db
from app.models.tipo_usuario import TipoUsuario


def crear_tipos_usuario():
    tipos = [
        "SUPER_ADMIN",
        "ADMIN",
        "MODERADOR",
        "INSTRUCTOR",
        "USUARIO"
    ]

    for nombre in tipos:
        if not TipoUsuario.query.filter_by(nombre=nombre).first():
            db.session.add(TipoUsuario(nombre=nombre))

    db.session.commit()
    