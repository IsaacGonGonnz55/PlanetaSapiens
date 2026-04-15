from app.extensions.db import db
from .base import BaseModel
from datetime import datetime

class Sesion(BaseModel):
    __tablename__ = "sesiones"

    id = db.Column(db.Integer, primary_key=True)

    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=True)

    token = db.Column(db.String(255), nullable=False)
    ip_address = db.Column(db.String(45))
    user_agent = db.Column(db.String(255))

    fecha_inicio = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_fin = db.Column(db.DateTime)

    activa = db.Column(db.Boolean, default=True)

    usuario = db.relationship("Usuario", back_populates="sesiones")
