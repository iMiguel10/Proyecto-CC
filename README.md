[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)   

# Proyecto-CC (Gestión de entradas)

Repositorio para el proyecto basado en microservicios de la asignatura Cloud Computing de la UGR.

## Descripción

El proyecto consistirá en una serie de microservicos en la nube, entre los que existen, uno para el catálogo o gestión de entradas, otro para la generación de esas entradas y otro posible microservicio para el envio de mensajes al cliente.  
El proyecto está pensado para incorporarse en una aplicación de eventos en los que hay una venta de entradas online, enfocada a empresas organizadoras de los mismos.

## Arquitectura

Se pretende tener una arquitectura mixta, basada en microservicos y en eventos, de manera que, cada microservicio pueda ser desarrolado y desplegado de forma independiente y con lenguajes distintos y se comuniquen a través de AMQP y si es necesario a través de HTTP (con una API REST). De esta manera nos quedarían 3 microservicos principales: **catálogo de entradas, generador de entradas y envío de mensajes**.

![Diagrama ARQ](https://github.com/iMiguel10/Proyecto-CC/blob/master/img/arquitectura-cc.png)

[**Documentación Arquitectura**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/arquitectura.md)

## Herramientas

* **Lenguajes:** Aún sin determinar.  
* **Almacenamiento:** Base de datos NoSQL (MongoDB quizá).
* **Comunicación:** Los microservicios se comunicarán mediante envío de mensajes (con RabbitMQ) y si fuese necesario se implementaría una API REST.
* **Test:** Para el desarrollo basado en test se implementarán distintas pruebas para todos los microservicios usando algún framework en cada uno de los lenguajes usados. Se tiene pensado utilizar Travis CI, ya que nos permite pasar los test y además incorporarlo con GitHub.

<!--[**Documentación Herramientas**]()-->
