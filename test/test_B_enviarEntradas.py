#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import sys
sys.path.append('../src/')
from enviarEntradas import Sender
import os

@pytest.fixture
def sender():
    '''Devuelve una instancia del sender correcto'''
    destinatarios = [os.environ["MAIL"]]
    return Sender(destinatarios)

@pytest.fixture
def sender_error():
    '''Devuelve una instancia del sender erroneo'''
    destinatarios = None
    return Sender(destinatarios)

def test_crearMensaje(sender,sender_error):
    '''Comprobar que se crea el mensaje correctamente'''
    assert sender.crearMensaje() == True, "Ha fallado la creación del mensaje"
    assert sender_error.crearMensaje() == False,  "Ha fallado la creación del mensaje"

def test_adjuntar(sender,sender_error):
    '''Comprobar que se adjunta el PDF correctamente'''
    sender.crearMensaje()
    sender_error.crearMensaje()
    assert sender.adjuntar('test-entrada.pdf') == True, "Ha fallado al adjuntar archivo"
    assert sender_error.adjuntar(None) == False,  "Ha fallado al adjuntar archivo"
    assert sender_error.adjuntar("lskdnd") == False,  "Ha fallado al adjuntar archivo"

def test_enviar(sender,sender_error):
    '''Comprobar que se envia el mensaje correctamente'''
    sender.crearMensaje()
    sender.adjuntar('test-entrada.pdf')
    sender_error.crearMensaje()
    sender_error.adjuntar('test-entrada.pdf')
    assert sender.enviar() == True, "Ha fallado el envio del correo"
    assert sender_error.enviar() == False, "Ha fallado el envio del correo"
