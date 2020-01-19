# Fabfile to:
#    - Instalar requeriments
#    - Parar
#    - Actualizar
#    - Iniciar

import os

# Import Fabric's module
from fabric import *


def getConnection():
    h = os.environ['HOST']
    c = Connection(host=h, user='vagrant', port=22, connect_kwargs={
            "key_filename": "/home/vagrant/.ssh/id_rsa",
        })
    return c

@task
def install(ctx,ms="all"):
    c = getConnection()
    # Iniciamos el servicio web
    with c.cd('Proyecto_CC/'):
        if (ms == "all"):
            c.run("pip3 install -r requirements.txt")
        else:
            c.run("pip3 install -r requirements-"+ms+".txt")


@task
def start(ctx,port=8080,workers=4,ms="all"):
    c = getConnection()
    # Iniciamos el servicio web
    with ctx.cd('Proyecto_CC/src/'):
        if (ms == "all" or ms == "catalogo"):
            c.run("gunicorn app:app --threads=2 --worker-class=gevent -w "+str(workers)+"  -b :"+str(port)+" &")
        if (ms == "all" or ms == "generador"):
            c.run("python3 generadorEntradas.py &")
        if (ms == "all" or ms == "sender"):
            c.run("python3 emailSender.py &")

# Tarea para parar el servicio
@task
def stop(ctx):
    """Para el servicio web. Que se puede lanzar con invoke start [-p/--port <puerto>]"""
    c = getConnection()
    c.run("pkill gunicorn")

@task
def update(ctx):
    c = getConnection()
    # Iniciamos el servicio web
    with c.cd('Proyecto_CC/'):
        c.run("git pull")
