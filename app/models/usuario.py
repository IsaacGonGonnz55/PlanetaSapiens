from app.extensions.db import db
from .base import BaseModel

class Usuario(BaseModel):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)

    persona_id = db.Column(db.Integer, db.ForeignKey("personas.id"), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    tipo_usuario_id = db.Column(db.Integer, db.ForeignKey("tipos_usuario.id"))

    is_active = db.Column(db.Boolean, default=True)
    last_login = db.Column(db.DateTime)

    persona = db.relationship("Persona", back_populates="usuario")
    sesiones = db.relationship("Sesion", back_populates="usuario")

    tipo_usuario = db.relationship("TipoUsuario", backref="usuarios")