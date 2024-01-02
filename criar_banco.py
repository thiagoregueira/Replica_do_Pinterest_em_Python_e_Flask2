from fakepinterest import database, app
from fakepinterest.models import Usuario, Foto  # noqa: F401

with app.app_context():
    database.create_all()
