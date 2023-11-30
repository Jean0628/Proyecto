from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from model.servicios import servicios



routes_servicios = Blueprint("routes_servicio", __name__)





@routes_servicios.route('/Guardar_servicio', methods=['POST'])
def Guardar_Clientes():
    tipoPersona = request.form['tipoPersona']
    servicio_dis = request.form['servicio_dis']
    
    
    if tipoPersona == 'PersonaNormal':
        new_cli = Clientes(servicio_dis )
        db.session.add(new_cli)
        db.session.commit()
    
        
    return "si"
    