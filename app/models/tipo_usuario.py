from app.extensions.db import db

class TipoUsuario(db.Model):
    __tablename__ = "tipos_usuario"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(255))

    usuarios = db.relationship("Usuario", back_populates="tipo_usuario")

