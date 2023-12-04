from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from model.clientes import Cliente
from model.agendas import agenda


routes_Cliente = Blueprint("routes_Cliente", __name__)


@routes_Cliente.route('/Guardar_Clientes', methods=['POST'])
def Guardar_Clientes():
    name = request.json['fullname']
    correo = request.json['fullcorreo']
    phone = request.json['fullphone']
    print(name, correo,phone)
    
    new_cli = Cliente(name, correo,phone)
    db.session.add(new_cli)
    db.session.commit()
  
    cliente_data = {
        'id': new_cli.id,
        'nombre': new_cli.NombreC,
        'correo': new_cli.Email,
        'phone': new_cli.telefono,
    }

    # Return a JSON response
    return jsonify(cliente_data), 201

@app.route('/Guardar_Citas', methods=['POST'])
def Guardar_Citas():

  clienteId = request.json['data']['clienteId']
  clienteId = request.json['data']['clienteId']
  fechaInput = request.json['data']['fullfechaInput']
  horaSelect = request.json['data']['fullhoraSelect']
  message = request.json['data']['fullmessage']
  
  print(clienteId,fechaInput,horaSelect,message)
  


  

  # new_cita = agenda(clienteId,fechaInput, horaSelect,message)
  # db.session.add(new_cita)
  # db.session.commit()

  return 'terminado'
    