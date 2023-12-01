from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma


#model
from model.clientes import Cliente
from model.servicios import servicios
from model.agendas import agenda

#rutas
from rutas.Clientes import routes_Cliente
from rutas.servicios import routes_servicios
from rutas.agendas import routes_agendas



app.register_blueprint(routes_Cliente, url_prefix='/fronted')



@app.route("/")
def index():
    titulo="Pagina Principal"
    return render_template('/main/index.html', titulo=titulo)    

# Datos de la tabla de Editoriales
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    
    
    
    #Aqui guardar datos
    
    