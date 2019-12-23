#!/usr/bin/python
# -*- coding: utf-8 -*-

from invoke import task, run

# Tarea para instalar dependencias
@task
def install(ctx,ms="all"):
    """Instala las dependecias del proyecto. Para expecificar el microservicio usar --ms o -m. Opciones: all, catalogo, generador, sender"""
    print("Instalando dependencias...")
    if (ms == "all"):
        ctx.run("pip install -r requirements.txt")
    else:
        ctx.run("pip install -r requirements-"+ms+".txt")
    print("HECHO!")

# Tarea para ejecutar los tests
@task
def test(ctx):
    """Ejecuta los test del proyecto"""
    with ctx.cd('test/'):
        print("Testeando...")
        ctx.run("pytest -v --cov=./")
        print("Testeado!")

# Tarea para codecov
@task
def codecov(ctx):
    """Sube los resultados de los test de cobertura a codecov"""
    with ctx.cd('test/'):
        ctx.run("codecov")

# Tarea para iniciar el servicio
@task
def start(ctx,port=8080,workers=4,ms="all"):
    """Lanza el servicio web con gunicorn. Puedes especificar el puerto con -p o --port. Por defecto sera el 8080. Puedes especificar los workers con -w o --workers. Por defecto serán 4. Para expecificar el microservicio usar --ms o -m. Opciones: all, catalogo, generador, sender"""
    with ctx.cd('src/'):
        if (ms == "all" or ms == "catalogo"):
            ctx.run("gunicorn app:app --threads=2 --worker-class=gevent -w "+str(workers)+"  -b :"+str(port)+" &")
        if (ms == "all" or ms == "generador"):
            ctx.run("python generadorEntradas.py &")
        if (ms == "all" or ms == "sender"):
            ctx.run("python emailSender.py &")

# Tarea para parar el servicio
@task
def stop(ctx):
    """Para el servicio web. Que se puede lanzar con invoke start [-p/--port <puerto>]"""
    ctx.run("pkill gunicorn")

# Tarea para automatizar la construción del contenedor
@task
def buildDocker(ctx, ruta=".", dockerfile="Dockerfile"):
    """Construye la imagen docker en la ruta con la opción -r o --ruta. Por defecto la ruta es la actual. Utilizando el Dockerfile en el directorio actual, para especificar usar --dockerfile o -d."""
    print("docker build -f "+dockerfile+ " -t catalogo-entradas "+ruta)

# Tarea para automatizar la ejecución de la imagen
@task
def runDocker(ctx, variables, port=8080):
    """Ejecuta la imagen docker con las varibales de entorno del fichero que se pasa como opción con -v o --variables. Es necesario especificar el puerto, con -p o --port, si no se utilizó el de por defecto(8080)"""
    ctx.run("docker run -it --rm --env-file "+variables+" -p 80:"+str(port)+" catalogo-eventos")
