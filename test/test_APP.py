#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../src/')

import os
import tempfile

import pytest
import app


@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    client = app.app.test_client()

    yield client

def test_status(client):
    rv = client.get('/')
    rv2 = client.get('/status')
    json_data = rv.get_json()
    json_data2 = rv2.get_json()
    assert json_data['status']=="OK" and rv.status_code == 200
    assert json_data['status']=="OK" and rv2.status_code == 200


def test_entrada(client):
    # Casos satisfactorios
    rv = client.put('/entrada', json={"entrada": [{"descripcion": "Esto es una" +
    "prueba en la base de datos estamos insertando datos en la base de datos para" +
    "probarla a ver como funciona bien o mal regular o peor",
    "evento": "AÑADIR ENTRADA", "precio": 23.1}]})
    rv2 = client.get('/entradas')
    json_data = rv2.get_json()
    id = json_data['entradas'][-1]['id']
    rv3 = client.get('/entrada/'+str(id))
    rv5 = client.post('/entrada/comprar/'+str(id), json={"propietario": "luisito@gmail.com"})
    rv6 = client.get('/entradas/propietario/luisito@gmail.com')
    # FALLO
    rv5F2 = client.post('/entrada/comprar/'+str(id), json={"propietario": "luisito@gmail.com"})

    rv4 = client.delete('/entrada/'+str(id))

    # Casos con fallos
    rvF = client.put('/entrada', json={})
    rv3F = client.delete('/entrada/-21')
    rv4F = client.get('/entrada/dds')
    rv5F1 = client.post('/entrada/comprar/'+str(id))
    rv5F3 = client.post('/entrada/comprar/'+str(id), json={"propietario": "luisito@gmail.com"})


    # Casos satisfactorios
    assert rv.status_code == 201
    assert rv2.status_code == 200
    assert rv3.status_code == 200
    assert rv4.status_code == 201
    assert rv5.status_code == 201
    assert rv6.status_code == 200



    # Casos con fallos
    assert rvF.status_code == 400
    assert rv3F.status_code == 404
    assert rv4F.status_code == 400
    assert rv5F1.status_code == 400
    assert rv5F2.status_code == 401
    assert rv5F3.status_code == 404
