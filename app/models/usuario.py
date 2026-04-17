from app.extensions.db import db
from .base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Usuario(UserMixin,BaseModel):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)

    persona_id = db.Column(db.Integer, db.ForeignKey("personas.id"), nullable=False)

    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)


    es_superadmin = db.Column(db.Boolean, default=False)
    activo = db.Column(db.Boolean, default=True)

    persona = db.relationship("Persona", back_populates="usuario")
    
    tipo_usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("tipos_usuario.id"),
        nullable=False
    )

    tipo_usuario = db.relationship(
        "TipoUsuario",
        back_populates="usuarios"
    )

    
    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    
    def tiene_permiso(self, nombre_permiso: str) -> bool:
        if self.es_superadmin:
            return True

        return any(
            permiso.nombre == nombre_permiso
            for permiso in self.tipo_usuario.permisos
        )

    def __repr__(self):
        return f"<Usuario {self.username}>"

    __table_args__ = (
        db.Index('idx_usuario_login', 'username', 'email'),
    )