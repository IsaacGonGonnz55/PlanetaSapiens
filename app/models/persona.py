from app.extensions.db import db
from .base import BaseModel

class Persona(BaseModel):
    __tablename__ = "personas"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)

    usuario = db.relationship("Usuario", back_populates="persona", uselist=False)
    

