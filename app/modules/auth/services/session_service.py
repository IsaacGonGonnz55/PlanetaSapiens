from app.models.sesion import Sesion
from app.extensions.db import db
from datetime import datetime
from flask import request
from flask_login import current_user


def crear_sesion_anonima():
    sesion_existente = Sesion.query.filter_by(
        ip_address=request.remote_addr,
        activa=True,
        es_autenticado=False
    ).first()

    if sesion_existente:
        return

    sesion = Sesion(
        ip_address=request.remote_addr,
        user_agent=request.headers.get("User-Agent"),
        es_autenticado=False,
        payload={
            "endpoint": request.endpoint,
            "metodo": request.method
        }
    )

    db.session.add(sesion)
    db.session.commit()


def autenticar_sesion(usuario):
    sesion = Sesion.query.filter_by(
        ip_address=request.remote_addr,
        activa=True
    ).order_by(Sesion.id.desc()).first()

    if sesion:
        sesion.usuario_id = usuario.id
        sesion.es_autenticado = True
        db.session.commit()


def cerrar_sesion():
    sesion = Sesion.query.filter_by(
        usuario_id=current_user.id,
        activa=True
    ).order_by(Sesion.id.desc()).first()

    if sesion:
        sesion.fecha_fin = datetime.utcnow()
        sesion.activa = False
        db.session.commit()