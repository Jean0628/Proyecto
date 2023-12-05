from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from model.barberos import barberos



routes_barberos = Blueprint("routes_barberos", __name__)





@routes_barberos.route('/Guardar_barbero', methods=['POST'])
def Guardar_barbero():
    tipoPersona = request.form['tipoPersona']
    barbero_dis = request.form['barbero_dis']
    
    
    if tipoPersona == 'PersonaNormal':
        new_barber = barberos(barbero_dis )
        db.session.add(new_barber)
        db.session.commit()
    
        
    return "si"
    