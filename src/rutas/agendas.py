from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from model.agendas import agenda



routes_agendas = Blueprint("routes_agendas", __name__)





@routes_agendas.route('/Guardar_agendas', methods=['POST'])
def Guardar_agendas():
    tipoPersona = request.form['tipoPersona']
    fecha = request.form['fecha']
    hora = request.form['hora']
    observaciones  = request.form['observaciones']

 
    
    if tipoPersona == 'PersonaNormal':
        new_age = agenda(fecha, hora, observaciones )
        db.session.add(new_age)
        db.session.commit()
    
        
    return "si"
    