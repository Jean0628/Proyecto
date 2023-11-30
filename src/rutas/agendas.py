from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from model.agendas import agendas



routes_Cliente = Blueprint("routes_agendas", __name__)





@routes_Cliente.route('/Guardar_agendas', methods=['POST'])
def Guardar_Clientes():
    tipoPersona = request.form['tipoPersona']
    NombreC = request.form['NombreC']
    Email = request.form['Email']
    
    telefono = request.form['telefono']
    
    if tipoPersona == 'PersonaNormal':
        new_cli = Clientes(NombreC, Email, telefono, )
        db.session.add(new_cli)
        db.session.commit()
    elif tipoPersona == 'Repartidor':
        new_rep = Repartidor(NombreC, Email, telefono)
        db.session.add(new_rep)
        db.session.commit()
        
    return "si"
    