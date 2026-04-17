"""Seed service module for initializing the application with default data."""

from .role_service import crear_tipos_usuario
from .permission_service import crear_permisos, asignar_permisos
from .user_service import crear_super_admin 


def seed_all():
    crear_tipos_usuario()
    crear_permisos()
    asignar_permisos()
    crear_super_admin()

    print("Sistema inicializado correctamente") 
    