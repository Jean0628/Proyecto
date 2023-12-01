from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from model.clientes import Cliente



routes_Cliente = Blueprint("routes_Cliente", __name__)





@routes_Cliente.route('/Guardar_Clientes', methods=['POST'])
def Guardar_Clientes():
    tipoPersona = request.form['tipoPersona']
    NombreC = request.form['NombreC']
    Email = request.form['Email']
    
    telefono = request.form['telefono']
    
    if tipoPersona == 'PersonaNormal':
        new_cli = Cliente(NombreC, Email, telefono, )
        db.session.add(new_cli)
        db.session.commit()
  
    return "si"
    