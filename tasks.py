#!/usr/bin/python
# -*- coding: utf-8 -*-

from invoke import task, run

# Tarea para instalar dependencias
@task
def install(ctx):
    print("Instalando dependencias...")
    ctx.run("pip install -r requirements.txt")
    print("HECHO!")

# Tarea para ejecutar los tests
@task
def test(ctx):
    with ctx.cd('test/'):
        print("Testeando...")
        ctx.run("pytest -v --cov=./")
        print("Testeado!")

# Tarea para codecov
@task
def codecov(ctx):
    with ctx.cd('test/'):
        ctx.run("codecov")

# Tarea para iniciar el servicio
@task
def start(ctx):
    with ctx.cd('src/'):
        ctx.run("gunicorn -b :8080 app:app &")

# Tarea para parar el servicio
@task
def stop(ctx):
    ctx.run("pkill gunicorn")
