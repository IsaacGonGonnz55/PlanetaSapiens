from app.extensions.db import db
from .base import BaseModel
from datetime import datetime

class Sesion(BaseModel):
    __tablename__ = "sesiones"

    id = db.Column(db.Integer, primary_key=True)

    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=True)

    session_token = db.Column(db.String(36), unique=True)

    ip_address = db.Column(db.String(45))
    user_agent = db.Column(db.String(255))

    es_autenticado = db.Column(db.Boolean, default=False)

    payload = db.Column(db.JSON, nullable=True)  

    fecha_inicio = db.Column(db.DateTime)
    fecha_fin = db.Column(db.DateTime)

    activa = db.Column(db.Boolean, default=True)