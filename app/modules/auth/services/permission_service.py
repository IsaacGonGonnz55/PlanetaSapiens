from app.extensions.db import db
from app.models.permiso import Permiso
from app.models.tipo_usuario import TipoUsuario


def crear_permisos():
    permisos = [
        "ver_usuarios", "crear_usuarios", "editar_usuarios", "eliminar_usuarios",
        "ver_cursos", "crear_cursos", "editar_cursos", "eliminar_cursos",
        "ver_foro", "crear_publicacion", "editar_publicacion", "eliminar_publicacion",
        "ver_eventos", "crear_eventos", "editar_eventos", "eliminar_eventos",
        "usar_calculadora",
        "acceso_admin", "gestionar_permisos"
    ]

    for nombre in permisos:
        if not Permiso.query.filter_by(nombre=nombre).first():
            db.session.add(Permiso(nombre=nombre))

    db.session.commit()


def asignar_permisos():
    roles_config = {
        "SUPER_ADMIN": "ALL",
        "ADMIN": ["ver_usuarios", "crear_usuarios", "ver_cursos", "crear_cursos", "acceso_admin"],
        "MODERADOR": ["ver_foro", "editar_publicacion", "eliminar_publicacion"],
        "INSTRUCTOR": ["crear_cursos", "editar_cursos", "ver_cursos"],
        "USUARIO": ["ver_cursos", "ver_foro", "crear_publicacion", "usar_calculadora"]
    }

    for rol_nombre, permisos_lista in roles_config.items():
        rol = TipoUsuario.query.filter_by(nombre=rol_nombre).first()
        if not rol:
            continue

        if permisos_lista == "ALL":
            rol.permisos = Permiso.query.all()
        else:
            rol.permisos = Permiso.query.filter(
                Permiso.nombre.in_(permisos_lista)
            ).all()

    db.session.commit()