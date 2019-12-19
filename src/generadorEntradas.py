#!/usr/bin/python
# -*- coding: utf-8 -*-
import pika
import json
from generadorentradasPDF import GeneradorPDF
import os


parameters = pika.URLParameters(os.environ["AMQP_SERVER"])
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

def callback(ch, method, properties, body):
    print("Message received")
    datos = json.loads(body)
    pdf = GeneradorPDF(datos)
    e = pdf.generarPDF()
    f = open(e, 'rb')
    entrada = f.read()
    f.close()
    ch.basic_publish(exchange='', routing_key='envia', body=entrada)


    print("Enviando mensaje para confirmar comprar")


channel.basic_consume(
    queue='genera', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages')
channel.start_consuming()
