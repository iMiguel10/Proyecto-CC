#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import sys
sys.path.append('../src/')
from generadorentradasPDF import Documento

@pytest.fixture
def documento():
    '''Devuelve una instancia del Documento con el contenido correcto'''
    datos = {
        "id": 12232323,
        "evento": "Concierto Pablo Alborán",
        "precio": 49.99,
        "propietario": "imiguel10@correo.ugr.es",
        "descripcion": "Lorem ipsum dolor sit amet consectetur adipiscing elit, augue enim nulla sodales vulputate ad, lacus himenaeos nostra ante cubilia ut. Penatibus arcu semper ultricies viverra platea netus cubilia parturient per turpis class sollicitudin habitasse, sem primis tincidunt libero duis eros erat nostra luctus dis sociosqu ut senectus, quis dui purus lectus nunc mattis ornare hac ad id convallis enim. Praesent accumsan luctus pharetra congue nostra vitae aenean nascetur, sem curabitur quam tristique massa inceptos."
    }
    return Documento(datos)

@pytest.fixture
def documento_error():
    '''Devuelve una instancia del Documento con el contenido erroneo'''
    datos = {"as":"as"}
    return Documento(datos)

def test_generarQR(documento,documento_error):
    '''Comprobar que se genera el QR correctamente'''
    assert documento.generaQR() != False, "Ha fallado la creación del QR"
    assert documento_error.generaQR() != False,  "Ha fallado la creación del QR"

def test_generarPDF(documento,documento_error):
    '''Comprobar que se genera PDF correctamente'''
    assert documento.generarPDF() != False, "Los datos son incorrectos, deberían tener un formato adecuado"
    assert documento_error.generarPDF() == False, "Los datos son incorrectos, deberían tener un formato adecuado"
