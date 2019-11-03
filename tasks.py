#!/usr/bin/python
# -*- coding: utf-8 -*-

from invoke import task, run

# Tarea para instalar dependencias
@task
def build(ctx):
    print("Instalando dependencias...")
    ctx.run("pip install -r requirements.txt")
    print("HECHO!")

# Tarea para ejecutar los tests
@task
def test(ctx):
    with ctx.cd('test/'):
        print("Testeando...")
        ctx.run("pytest")
        print("Testeado!")
