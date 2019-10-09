[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)   

# Proyecto-CC (Gestión de entradas)

Repositorio para el proyecto basado en microservicios de la asignatura Cloud Computing de la UGR.

## Descripción

El proyecto consistirá en una serie de microservicos en la nube, entre los que existen, uno para la gestión de entradas, otro para la generación de esas entradas y otro posible microservicio para el envio de mensajes al cliente.  
El proyecto está pensado para incorporarse en una aplicación de eventos en los que hay una venta de entradas online, enfocada a empresas organizadoras de los mismos.

## Herramientas

* Este proyecto será llevado a cabo con varios lenguajes.  
* Se hará uso de una API como interfaz con el usuario/cliente.
* La idea es usar una base de datos, NoSQL, para el almacenamiento.
* Los microservicios se comunicarán mediante protocolos como HTTP (REST) con la API, pero también de forma asincrónica entre ellos, con RabbitMQ.
* Para el desarrollo basado en test se implementarán distintas pruebas para todos los microservicios usando algún framework en cada uno de los lenguajes usados.
Se tiene pensado utilizar Travis CI, ya que nos permite pasar los test y además incorporarlo con GitHub.

<!--[**Documentación Herramientas**]()-->
