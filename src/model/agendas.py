from config.db import db, app, ma


class agenda(db.Model):
    __tablename__ = "tblAgenda_citas"

    id = db.Column(db.Integer, primary_key=True)
    id_cli = db.Column(db.Integer,db.ForeignKey('tblClientess.id'))
    id_servi = db.Column(db.Integer,db.ForeignKey('tblServicios_Dispo.id'), nullable=True)
    fecha = db.Column(db.Date)
    hora = db.Column(db.String(50))
    observaciones = db.Column(db.String(1000))
   

    def __init__(self, id_cli, id_servi, fecha, hora, observaciones):
        self.id_cli = id_cli
        self.id_servi = id_servi
        self.fecha = fecha
        self.hora = hora
        self.observaciones = observaciones
        



with app.app_context():
    db.create_all()
