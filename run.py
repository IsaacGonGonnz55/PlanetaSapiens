from app import create_app
from app.extensions.db import db
from sqlalchemy import text

app = create_app()

@app.route("/")
def test_db():
    try:
        result = db.session.execute(text("SELECT 1"))
        return f"Conexión exitosa: {list(result)}"
    except Exception as e:
        return f"Error de conexión: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)

