#!/usr/bin/python
# -*- coding: utf-8 -*-
from base import Session, engine, Base
from models import Entradas
import pika
import json
import os

class Catalogo:

    def __init__(self):
        # Generamos el esquema de la BD
        Base.metadata.create_all(engine)
        self.parameters = pika.URLParameters(os.environ["AMQP_SERVER"])
        self.connection = pika.BlockingConnection(self.parameters)

    def get_json(self,entrada):
        return {
            'id': entrada.id,
            'evento': entrada.evento,
            'precio': float(entrada.precio),
            'propietario': entrada.propietario,
            'descripcion': entrada.descripcion
        }


    def getEntradasDisponibles(self):
        # Creamos una nueva sesion
        session = Session()

    	# Obtenemos todas las entradas del catálogo
        entradas = session.query(Entradas).filter_by(propietario=None)
        session.close()
        data = {}
        data['entradas'] = []
        for e in entradas:
            data['entradas'].append(self.get_json(e))

        return data

    def getEntradaById(self,id):
        # Creamos una nueva sesion
        session = Session()
        e = session.query(Entradas).filter_by(id=id).first()
        session.close()
        data = {}
        data['entradas'] = []
        if (e is not None):
            data['entradas'].append(self.get_json(e))
        return data

    def getEntradaByPropietario(self,p):
        # Creamos una nueva sesion
        session = Session()
        entradas = session.query(Entradas).filter_by(propietario=p)
        session.close()
        data = {}
        data['entradas'] = []
        if (entradas is not None):
            for e in entradas:
                data['entradas'].append(self.get_json(e))
        return data

    def addEntrada(self,datos):
        # Añadir
        try:

        	e = datos['entrada'][0]
        	# Creamos una nueva sesion
        	session = Session()
        	entrada = Entradas(e['evento'],e['precio'],None,e['descripcion'])

        	session.add(entrada)
        	session.commit()
        	session.close()

        	return 201
        except:
        	return 400

    def comprarEntrada(self,propietario,id):
        # Creamos una nueva sesion
        session = Session()
        entrada = session.query(Entradas).filter_by(id=id).first()
        if entrada is not None:
            if entrada.propietario is None:
                entrada.propietario = str(propietario)
                session.commit()
            else: return 401
        else: return 404
        session.close()
        channel = self.connection.channel()
        datos = json.dumps(self.get_json(entrada))
        channel.basic_publish(exchange='', routing_key='genera', body=datos)
        logging.info('Enviado a la cola el mensaje con la entrada: '+id)
        connection.close()

        return 201

    def delEntradaById(self,id):
        # Creamos una nueva sesion
        session = Session()
        entrada = session.query(Entradas).filter_by(id=id).first()
        if (entrada is None):
            session.close()
            return 404
        else:
            session.delete(entrada)
            session.commit()
            session.close()
            return 201
