from app.extensions.db import db
from app.models.base import BaseModel

class Permiso(BaseModel):
    __tablename__ = "permisos"

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100), unique=True, nullable=False, index=True)
    descripcion = db.Column(db.String(255))