from app.extensions.db import db


tipo_usuario_permisos = db.Table(
    "tipo_usuario_permisos",

    db.Column(
        "tipo_usuario_id",
        db.Integer,
        db.ForeignKey("tipos_usuario.id", ondelete="CASCADE"),
        primary_key=True
    ),

    db.Column(
        "permiso_id",
        db.Integer,
        db.ForeignKey("permisos.id", ondelete="CASCADE"),
        primary_key=True
    )

)