#!/usr/bin/python
# -*- coding: utf-8 -*-
# Usado el código de ejemplo: https://gist.github.com/2624789/d42aaa12bf3a36356342#file-enviar_correo_con_adjunto-py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

class Sender:

    def __init__(self, destinatarios):
        # Iniciamos los parámetros
        self.remitente = os.environ["MAIL"]
        self.destinatarios = destinatarios
        self.asunto = 'Entrada'
        self.cuerpo = 'Gracias por su compra, aquí adjuntamos la entrada que deberá mostrar a la entrada del evento.\nUn saludo.'
        self.nombre_adjunto = 'entrada.pdf'
        self.mensaje = None

    def crearMensaje(self):

        if (self.destinatarios is not None):
            # Creamos el objeto mensaje
            self.mensaje = MIMEMultipart()
            # Establecemos los atributos del mensaje
            self.mensaje['From'] = self.remitente
            self.mensaje['To'] = ", ".join(self.destinatarios)
            self.mensaje['Subject'] = self.asunto

            return True
        else :
            return False

    def adjuntar(self,ruta_adjunto):


        if (self.mensaje is not None):

            # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
            self.mensaje.attach(MIMEText(self.cuerpo, 'plain'))

            try:
                # Abrimos el archivo que vamos a adjuntar
                archivo_adjunto = open(ruta_adjunto, 'rb')
            except:
                print("FALLANDO")
                return False


            # Creamos un objeto MIME base
            adjunto_MIME = MIMEBase('application', 'octet-stream')

            # Y le cargamos el archivo adjunto
            adjunto_MIME.set_payload((archivo_adjunto).read())

            # Codificamos el objeto en BASE64
            encoders.encode_base64(adjunto_MIME)

            # Agregamos una cabecera al objeto
            adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % self.nombre_adjunto)

            # Y finalmente lo agregamos al mensaje
            self.mensaje.attach(adjunto_MIME)

            return True

        else:
            return False

    def enviar(self):

        if (self.mensaje is not None):
            # Creamos la conexión con el servidor
            sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
            # Ciframos la conexión
            sesion_smtp.starttls()
            # Iniciamos sesión en el servidor
            sesion_smtp.login(self.remitente,os.environ["MAIL_PASS"])
            # Convertimos el objeto mensaje a texto
            texto = self.mensaje.as_string()
            # Enviamos el mensaje
            sesion_smtp.sendmail(self.remitente, self.destinatarios, texto)
            # Cerramos la conexión
            sesion_smtp.quit()
            return True
        else:
            return False
