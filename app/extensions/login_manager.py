from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = "auth.login" 
login_manager.login_message = "Debes iniciar sesión primero"
login_manager.login_message_category = "warning"

@login_manager.user_loader
def load_user(user_id):
    from app.models.usuario import Usuario  # import interno (evita ciclos)
    return Usuario.query.get(int(user_id))
