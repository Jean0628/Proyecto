from config.db import db, app, ma


class Cliente(db.Model):
    __tablename__ = "tblClientess"

    id = db.Column(db.Integer, primary_key=True)
    NombreC = db.Column(db.String(200))
    Email = db.Column(db.String(200))
    telefono = db.Column(db.String(10))
   

    def __init__(self, NombreC, Email,  telefono):
        self.NombreC = NombreC
        self.Email = Email
        self.telefono = telefono



with app.app_context():
    db.create_all()
