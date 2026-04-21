"""Seed service module for initializing the application with default data."""

from .role_service import crear_tipos_usuario
from .permission_service import crear_permisos, asignar_permisos
from app.extensions.db import db
from app.models.usuario import Usuario
from app.models.tipo_usuario import TipoUsuario
from app.models.persona import Persona


def seed_all():
    crear_tipos_usuario()
    crear_permisos()
    asignar_permisos()

    print("Sistema inicializado correctamente") 


def crear_super_admin():
    if Usuario.query.filter_by(es_superadmin=True).first():
        print("⚠️ Ya existe un super admin")
        return

    rol = TipoUsuario.query.filter_by(nombre="SUPER_ADMIN").first()

    persona = Persona(
        nombre="Super",
        apellido_paterno="Admin",
        apellido_materno="Sistema"
    )
    db.session.add(persona)
    db.session.flush()

    user = Usuario(
        persona_id=persona.id,
        username="superadmin",
        email="admin@planetasapiens.com",
        es_superadmin=True,
        tipo_usuario=rol
    )

    user.set_password(os.getenv("DEFAULT_ADMIN_PASSWORD"))

    db.session.add(user)
    db.session.commit()

    print("Super admin creado")    