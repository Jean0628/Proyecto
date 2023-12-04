from config.db import db, app, ma


class servicios(db.Model):
    __tablename__ = "tblServicios_Dispo"

    id = db.Column(db.Integer, primary_key=True)
    servicio_dis = db.Column(db.String(200))
    
   

    def __init__(self, servicio_dis):
        self.servicio_dis = servicio_dis
        



with app.app_context():
    db.create_all()

    if not db.session.query(servicios).count():
        new_servicio = [
            servicios("Corte de Cabello"),
            servicios("Corte de Cabello Infantil"),
            servicios("Afeitado de barba"),
            servicios("Peinado"),
            servicios("Depilacion de Cejas"),
        ]
        db.session.add_all(new_servicio)
        db.session.commit()
        print("4 servicios guardados!")
    else:
        print("Los servicios ya existen en la base de datos.")
