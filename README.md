[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)   

# Proyecto-CC (Gestión de entradas)

Repositorio para el proyecto basado en microservicios de la asignatura Cloud Computing de la UGR.

## Descripción

El proyecto consistirá en una serie de microservicos en la nube, entre los que existen, uno para el catálogo o gestión de entradas, otro para la generación de esas entradas y otro posible microservicio para el envio de mensajes al cliente.  
El proyecto está pensado para incorporarse en una aplicación de eventos en los que hay una venta de entradas online, enfocada a empresas organizadoras de los mismos.

[**Historias de usuario**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/historias-usuario.md)

## Arquitectura

Se pretende tener una arquitectura mixta, basada en microservicos y en eventos, de manera que, cada microservicio pueda ser desarrolado y desplegado de forma independiente y con lenguajes distintos y se comuniquen a través de AMQP y si es necesario a través de HTTP (con una API REST). De esta manera nos quedarían 3 microservicos principales más un servicio de configuración remota y uno de logs: **catálogo de entradas, generador de entradas y envío de mensajes**.

![Diagrama ARQ](https://github.com/iMiguel10/Proyecto-CC/blob/master/img/arquitectura-cc.png)

[**Documentación Arquitectura**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/arquitectura.md)

## Herramientas

* **Lenguajes:** Para el desarrollo de los microservicios se usará Python 3. Por otro lado se usará `virtualenv` como entorno virtual para el desarollo aislado de los microservicios.
* **Almacenamiento:** Para el almacenamiento de los datos en el microservico de catálogo de entradas se usuará una base de datos SQL, en concreto [ElephantSQL](https://www.elephantsql.com/).
* **Comunicación:** Los microservicios se comunicarán mediante envío de mensajes (con RabbitMQ).
* **Test:** Para el desarrollo basado en test se implementarán distintas pruebas para todos los microservicios usando [PyTest](https://docs.pytest.org/en/latest/). Se tiene pensado utilizar Travis CI, ya que nos permite pasar los test y además incorporarlo con GitHub.
* **Servicios:** Se necesitan servicios para la configuración distribuida, para ello se hará uso de [etcd](https://etcd.io/), y para el log, se usará logging, que nos permite sacar log de nuestros microservicios y se utilizará syslog para centralizarlos todos.

[**Documentación Herramientas**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/herramientas.md)
