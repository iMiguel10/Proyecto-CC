#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import sys
sys.path.append('../src/')
from generadorentradasPDF import GeneradorPDF

@pytest.fixture
def generador():
    '''Devuelve una instancia del GeneradorPDF con el contenido correcto'''
    datos = {
        "id": 12232323,
        "evento": "Concierto Pablo Alborán",
        "precio": 49.99,
        "propietario": "probando@correo.es",
        "descripcion": "Lorem ipsum dolor sit amet consectetur adipiscing elit, augue enim nulla sodales vulputate ad, lacus himenaeos nostra ante cubilia ut. Penatibus arcu semper ultricies viverra platea netus cubilia parturient per turpis class sollicitudin habitasse, sem primis tincidunt libero duis eros erat nostra luctus dis sociosqu ut senectus, quis dui purus lectus nunc mattis ornare hac ad id convallis enim. Praesent accumsan luctus pharetra congue nostra vitae aenean nascetur, sem curabitur quam tristique massa inceptos."
    }
    return GeneradorPDF(datos)

@pytest.fixture
def generador_error():
    '''Devuelve una instancia del GeneradorPDF con el contenido erroneo'''
    datos = {"as":"as"}
    return GeneradorPDF(datos)

def test_generarQR(generador,generador_error):
    '''Comprobar que se genera el QR correctamente'''
    assert generador.generaQR() != False, "Ha fallado la creación del QR"
    assert generador_error.generaQR() != False,  "Ha fallado la creación del QR"

def test_generarPDF(generador,generador_error):
    '''Comprobar que se genera PDF correctamente'''
    assert generador.generarPDF() != False, "Los datos son incorrectos, deberían tener un formato adecuado"
    assert generador_error.generarPDF() == False, "Los datos son incorrectos, deberían tener un formato adecuado"
