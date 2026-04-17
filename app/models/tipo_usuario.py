from app.extensions.db import db
from app.models.base import BaseModel
from app.models.tipo_usuario_permiso import tipo_usuario_permisos

class TipoUsuario(BaseModel):
    __tablename__ = "tipos_usuario"

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(
        db.String(50),
        unique=True,
        nullable=False,
        index=True
    )

    descripcion = db.Column(db.String(255))

    activo = db.Column(db.Boolean, default=True)

    # 🔗 Relación con permisos
    permisos = db.relationship(
        "Permiso",
        secondary=tipo_usuario_permisos,
        backref=db.backref("tipos_usuario", lazy="dynamic"),
        lazy="joined"
    )

    # 🔗 Relación con usuarios
    usuarios = db.relationship(
        "Usuario",
        back_populates="tipo_usuario",
        lazy=True
    )

    def __repr__(self):
        return f"<TipoUsuario {self.nombre}>"