from config.db import db, app, ma


class servicios(db.Model):
    __tablename__ = "tblServicios_Dispo"

    id = db.Column(db.Integer, primary_key=True)
    servicio_dis = db.Column(db.String(200))
    
   

    def __init__(self, servicio_dis):
        self.servicio_dis = servicio_dis
        



with app.app_context():
    # db.create_rall()

    new_citas = [
        servicios("Beauty & Spa"),
        servicios("Body Massage"),
        servicios("Shaving & Facial"),
        servicios("Hair Color"),
    ]

    # Add all instances to the database session
    db.session.add_all(new_citas)

    # Commit the changes to persist the data
    db.session.commit()

    print("4 servicios guardados!")
