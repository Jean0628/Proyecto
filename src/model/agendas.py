from config.db import db, app, ma


class agendas(db.Model):
    __tablename__ = "tblAgenda_citas"

    id = db.Column(db.Integer, primary_key=True)
    id_cli = db.Column(db.Integer,db.ForeignKey('tblClientess.id'))
    id_cli = db.Column(db.Integer,db.ForeignKey('tblServicios_Dispo.id'))
    fecha = db.Column(db.Date)
    hora = db.Column(db.Integer)
    observaciones = db.Column(db.String(1000))
   

    def __init__(self, NombreC, Email,  telefono):
        self.NombreC = NombreC
        self.Email = Email
        self.telefono = telefono



with app.app_context():
    db.create_all()
