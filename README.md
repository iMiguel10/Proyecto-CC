[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Build Status](https://travis-ci.com/iMiguel10/Proyecto-CC.svg?branch=master)](https://travis-ci.com/iMiguel10/Proyecto-CC)
[![CircleCI](https://circleci.com/gh/iMiguel10/Proyecto-CC.svg?style=svg)](https://circleci.com/gh/iMiguel10/Proyecto-CC) [![codecov](https://codecov.io/gh/iMiguel10/Proyecto-CC/branch/master/graph/badge.svg)](https://codecov.io/gh/iMiguel10/Proyecto-CC)  [![DevQAGRX](https://img.shields.io/badge/DevQAGRX-blueviolet?style=svg&logo=Git)](https://github.com/JJ/curso-tdd)
# Proyecto-CC (Gestión de entradas)

Repositorio para el proyecto basado en microservicios de la asignatura Cloud Computing de la UGR.

###### Ayuda

- **Versión:** `Python 3.6.8`
- **Instalar:** `invoke install` o `pip install -r requirements.txt`
- **Test:** `invoke test`
- **Ejecutar:** `invoke start`
- **Parar:** `invoke stop`

**Variables de entorno necesarias:**

- **MAIL** Dirección de correo (Gmail) emisor de los mensajes.  
- **MAIL_PASS** Contraseña de la dirección de correo emisor.
- **BD** URL de conexión con la base de datos.
- **CODECOV_TOKEN** Token para subir los datos de los test de cobertura a codecov.


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

Para la integracion continua se han usado 2 servicios diferentes, Travis CI, para testear la versión del lenguaje con la que se está desarrolando (3.6.8), además de la 3.7 y Circle CI, con la que se testea la versión mínima con la que funcionan los microservicios (3.5).

Se van a testear todos los [**microservicios**](https://github.com/iMiguel10/Proyecto-CC/tree/master/src) (**Catálogo de entradas, generador PDF, envio de correo**), así como sus entidades.

Por otro lado para **instalarla y testearla** es necesario instalar los [*requirements.txt*](https://github.com/iMiguel10/Proyecto-CC/blob/master/requirements.txt) con *pip* (`pip install -r requirements.txt`) y hacer uso de *PyTest* para ejecutar los test. Todo esto quedará automatizado con la herramienta de construción **Invoke**, pudiendo hacer `invoke install` o `invoke test` respectivamente, siendo la forma más correcta.

Por último también se han añadido test de cobertura que podemos ver tras hacer `invoke test` y `coverage report -m`. O desde [**codecov**](https://codecov.io/gh/iMiguel10/Proyecto-CC).

Todas estas tareas quedan recogidas en el [tasks.py](https://github.com/iMiguel10/Proyecto-CC/blob/master/tasks.py). Este archivo es el que usa la herramienta de construcción **Invoke**, en el se definen todas las tareas de manera que queden automatizadas. Por ello en nuestro caso tenemos 3 tareas:
+ **install:** Es la tarea usada para la instalación de las dependecias.
+ **test:** Es la tarea usada para ejecutar los test.
+ **codecov:** Es la tarea que se usa para enviar los resultados de test de cobertura a codecov.

~~~

buildtool: tasks.py

~~~

[**Documentación Integración Continua**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/integracion-continua.md)

## Contenedores para microservicos

Para esta parte de contenedores para microservicios, en primer lugar se ha creado una API Rest para consultar los eventos de un catálogo ([app](https://github.com/iMiguel10/Proyecto-CC/blob/master/src/app.py)), y en segundo lugar se ha buscado un contendor lo más adecuado posible para que albergue esa aplicación. Por ello se ha hecho uso de Docker y se ha creado un [Dockerfile](https://github.com/iMiguel10/Proyecto-CC/blob/master/Dockerfile). En el que se ha elegido una imagen base de python 3.6 slim, porque la aplicación esta escrita en ese lenguaje y en esa versión, y además tras instalar las dependencias es el contenedor que menos nos ocupa, ya que se han probado con otras imagenes base como python3.6-alpine o ubuntu (18.04).

También se ha desplegado o subido el contendor a distintos lugares, a Docker Hub y a GitHub(Para subirlo se ha hecho [esto](https://help.github.com/es/github/managing-packages-with-github-packages/configuring-docker-for-use-with-github-packages)). A continuación se muestran las rutas.

~~~
Contenedor: https://hub.docker.com/r/imiguel10/catalogo-eventos/dockerfile

GitHub: https://github.com/iMiguel10/Proyecto-CC/packages/65465?version=latest
~~~

[**Documentación Contenedores-Microservicios**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/contenedores-microservicios.md)
