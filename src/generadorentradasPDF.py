#!/usr/bin/python
# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import qrcode
import textwrap
import time
import json
from os import remove
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')


class Documento:

    def __init__(self, datos):
        self.contenido = datos


    def generarPDF(self):
        try:
            # Preparamos el documento
            doc = str(self.contenido["id"])+".pdf"
            w, h = A4
            c = canvas.Canvas(doc, pagesize=A4)

            # Creamos un marco rectangular
            c.roundRect(10, 10, 575, 821, 10)

            # Creamos un título para la entrada
            c.setFont("Helvetica", 10)
            c.drawString(50, 750, "Fecha: "+time.strftime("%d/%m/%y"))

            # Creamos un título para la entrada
            c.setFont("Helvetica-Bold", 20)
            c.drawString(50, 700, "Entrada: "+self.contenido["evento"])

            # Ponemos el nombre identificador del usuario
            c.setFont("Helvetica", 12)
            c.drawString(50, 670, "Usuario: " + self.contenido["propietario"])

            # Ponemos el QR para la entrada
            qr = self.generaQR()
            c.drawImage(qr, 50, 350, 300, 300)

            # Ponemos el precio de la entrada
            c.setFont("Helvetica-Bold", 16)
            c.drawString(50, 250, "Precio: " + str(self.contenido["precio"])+" €")

            # Ponemos una descripción
            c.setFont("Helvetica", 12)
            lineas = textwrap.wrap(self.contenido["descripcion"],80)
            h = 230
            for l in lineas:
                c.drawString(50,h , l) #100
                h-=15

            # Ponemos mensaje de agradecimiento
            c.setFont("Helvetica-Bold", 16)
            c.drawString(50, 50, "GRACIAS POR SU COMPRA") 

            # Guardamos el documento
            c.showPage()
            c.save()

            # Eliminamos qr generado
            remove(qr)

            logging.info('PDF: '+doc+' generado')
            return True

        except Exception as e:

            logging.error('Error en la creación del PDF:'+str(e))
            return False

    def generaQR(self):

        try:

            qr = "qr.png"
            text = json.dumps(self.contenido, indent=4)

            img = qrcode.make(text)

            f = open(qr, "wb")
            img.save(f)
            f.close()

            logging.info('QR: '+qr+' generado')
            return qr

        except Exception as e:

            logging.error('Error en la creación del QR:'+str(e))
            return False
