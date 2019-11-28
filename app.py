#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from catalogo import Catalogo

# PROBANDO
from generadorentradasPDF import GeneradorPDF
from enviarEntradas import Sender



catalogo = Catalogo()
app = Flask(__name__)

# ------------------ ESTADO ------------------------------------------------#

# Ruta que devuelve status OK
@app.route('/', methods = ['GET'])
def inicio():
	return jsonify(status="OK"),200


# Ruta para el hito 4 (Contenedor Docker)
@app.route('/status', methods = ['GET'])
def status():
	return jsonify(status="OK"),200

# ------------------ ENTRADAS ------------------------------------------------#

# Si usas el método muestra todas las entradas(disponibles) del catálogo
@app.route('/entradas', methods = ['GET'])
def entradas():
    data = catalogo.getEntradasDisponibles()
    return data,200


# Si usas el método devuelve o elimina una entrada con id = n
@app.route('/entrada/<n>', methods = ['GET','DELETE'])
def entrada(n):

	try:
		id = int(n)
	except:
		return '',400

	if request.method == 'DELETE':
		codigo = catalogo.delEntradaById(n)
		return '', codigo
	data = {}
	if request.method == 'GET':
		data = catalogo.getEntradaById(n)
	return data,200


# Si usas el método inserta una entrada en el catálogo
@app.route('/entrada', methods = ['PUT'])
def addEntrada():
	json_data = request.get_json()
	codigo = catalogo.addEntrada(json_data)
	return '',codigo

# Si usas el método devuelve las entradas de un propietario p
@app.route('/entradas/propietario/<p>', methods = ['GET'])
def entradasPropietrio(p):

	data = {}

	try:
		propietario = str(p)
	except:
		return '',404

	data = catalogo.getEntradaByPropietario(propietario)

	return data, 200

# ------------------ COMPRAR ------------------------------------------------#
# Si usas el método actualiza el propietario si no tiene, es decir, compra la
# entrada
@app.route('/entrada/comprar/<n>', methods = ['POST'])
def comprarEntrada(n):

	p = ''
	# Comprar
	try:
		id = int(n)
		json_data = request.get_json()
		p = json_data['propietario']
	except:
		return '',400

	codigo = catalogo.comprarEntrada(p,id)

	# PROBANDO
	if (codigo == 201):
		datos = catalogo.getEntradaById(n)
		documento = GeneradorPDF(datos['entradas'][0])
		documento.generarPDF()

		destinatarios = ['m1gu3l1ll0@gmail.com']
		sender = Sender(destinatarios)

		sender.crearMensaje()
		sender.adjuntar(str(datos['entradas'][0]['id'])+'.pdf')
		sender.enviar()

	return '', codigo


if __name__ == '__main__':
	app.run(host='localhost', debug=True)
