#!/usr/bin/python
# -*- coding: utf-8 -*-
import pika
import json
import os
from enviarEntradas import Sender
import PyPDF2
import re

parameters = pika.URLParameters(os.environ["AMQP_SERVER"])
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

def callback(ch, method, properties, body):

    f = open('entrada.pdf','wb')
    f.write(body)
    f.close()

    print("Recibida la entrada")

    file = open('entrada.pdf', 'rb')
    pdfreader = PyPDF2.PdfFileReader(file)
    pageobj = pdfreader.getPage(0)
    pdftext = pageobj.extractText()
    destinatarios = re.findall(r'[\w\-\.]+@[\w\-\.]+\.+[a-zA-Z]{1,4}', pdftext)

    sender = Sender(destinatarios)

    sender.crearMensaje()
    sender.adjuntar('entrada.pdf')
    sender.enviar()

channel.basic_consume(
    queue='envia', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
