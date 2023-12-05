from config.db import db, app, ma


class barberos(db.Model):
    __tablename__ = "tbl_Barberos"

    id = db.Column(db.Integer, primary_key=True)
    barberos = db.Column(db.String(200))
    
   

    def __init__(self, barberos):
        self.barberos = barberos
        



with app.app_context():
    db.create_all()

    if not db.session.query(barberos).count():
        new_barber = [
            barberos("KevinGarcia "),
            barberos("Andrew Smith "),
            barberos("Marcus Patiño"),
           
        ]
        db.session.add_all(new_barber)
        db.session.commit()
        print("3 servicios guardados!")
    else:
        print("Los servicios ya existen en la base de datos.")

