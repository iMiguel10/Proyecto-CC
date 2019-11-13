[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Build Status](https://travis-ci.com/iMiguel10/Proyecto-CC.svg?branch=master)](https://travis-ci.com/iMiguel10/Proyecto-CC)
[![CircleCI](https://circleci.com/gh/iMiguel10/Proyecto-CC.svg?style=svg)](https://circleci.com/gh/iMiguel10/Proyecto-CC) [![codecov](https://codecov.io/gh/iMiguel10/Proyecto-CC/branch/master/graph/badge.svg)](https://codecov.io/gh/iMiguel10/Proyecto-CC)  [![DevQAGRX](https://img.shields.io/badge/DevQAGRX-blueviolet?style=svg&logo=Git)](https://github.com/JJ/curso-tdd)
# Proyecto-CC (Gestión de entradas)

Repositorio para el proyecto basado en microservicios de la asignatura Cloud Computing de la UGR.

###### Ayuda

- **Versión:** `Python 3.6.8`
- **Instalar:** `invoke build` o `pip install -r requirements.txt`
- **Test:** `invoke test`
<!-- - **Ejecutar:** -->

## Descripción

El proyecto consistirá en una serie de microservicos en la nube, entre los que existen, uno para el catálogo o gestión de entradas, otro para la generación de esas entradas y otro posible microservicio para el envio de mensajes al cliente.  
El proyecto está pensado para incorporarse en una aplicación de eventos en los que hay una venta de entradas online, enfocada a empresas organizadoras de los mismos.

[**Historias de usuario**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/historias-usuario.md)

## Arquitectura

Se pretende tener una arquitectura mixta, basada en microservicos y en eventos, de manera que, cada microservicio pueda ser desarrolado y desplegado de forma independiente y con lenguajes distintos y se comuniquen a través de AMQP y si es necesario a través de HTTP (con una API REST). De esta manera nos quedarían 3 microservicos principales más un servicio de configuración remota y uno de logs: **catálogo de entradas, generador de entradas y envío de mensajes**.

[**Documentación Arquitectura**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/arquitectura.md)

## Herramientas

* **Lenguajes:** Para el desarrollo de los microservicios se usará Python 3. Independientemente de las herramientas usadas se usará `virtualenv` como entorno virtual para el desarollo local de los microservicios.
* **Almacenamiento:** Para el almacenamiento de los datos en el microservico de catálogo de entradas se usuará una base de datos SQL, en concreto [ElephantSQL](https://www.elephantsql.com/).
* **Comunicación:** Los microservicios se comunicarán mediante envío de mensajes (con RabbitMQ).
* **Test:** Para el desarrollo basado en test se implementarán distintas pruebas para todos los microservicios usando [PyTest](https://docs.pytest.org/en/latest/). Se tiene pensado utilizar Travis CI, ya que nos permite pasar los test y además incorporarlo con GitHub.
* **Servicios:** Se necesitan servicios para la configuración distribuida, para ello se hará uso de [etcd](https://etcd.io/), y para el log, se usará logging, que nos permite sacar log de nuestros microservicios y se utilizará syslog para centralizarlos todos.

[**Documentación Herramientas**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/herramientas.md)

## Integración continua

Para la integracion continua se han usado 2 servicios diferentes, Travis CI, para testear la versión del lenguaje con la que se está desarrolando (3.6.8), y Circle CI, con la que se testea la versión mínima con la que funcionan los microservicios (3.5).

Se van a testear todos los [**microservicios**](https://github.com/iMiguel10/Proyecto-CC/tree/master/src) (**Catálogo de entradas, generador PDF, envio de correo**), así como sus entidades.

Por otro lado para **instalarla y testearla** es necesario instalar los [*requirements.txt*](https://github.com/iMiguel10/Proyecto-CC/blob/master/requirements.txt) con *pip* (`pip install -r requirements.txt`) y hacer uso de *PyTest* para ejecutar los test. Todo esto quedará automatizado con la herramienta de construción **Invoke**, pudiendo hacer `invoke build` o `invoke test` respectivamente.

Por último también se han añadido test de cobertura que podemos ver tras hacer `invoke test` y `coverage report -m`. O desde [**codecov**](https://codecov.io/gh/iMiguel10/Proyecto-CC).

Todas estas tareas quedan recogidas en el [tasks.py](https://github.com/iMiguel10/Proyecto-CC/blob/master/tasks.py). Este archivo es el que usa la herramienta de construcción **Invoke**, en el se definen todas las tareas de manera que queden automatizadas. Por ello en nuestro caso tenemos 3 tareas:
+ **build:** Es la tarea usada para la instalación de las dependecias.
+ **test:** Es la tarea usada para ejecutar los test.
+ **codecov:** Es la tarea que se usa para enviar los resultados de test de cobertura a codecov.

buildtool: tasks.py

[**Documentación Integración Continua**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/integracion-continua.md)
