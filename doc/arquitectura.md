## Arquitectura del proyecto
---

La arquitectura estará basada en microservicos, para puedan ser desarrollados y desplegadso de forma independiente y con lenguajes distintos, así que, nos quedarán los siguientes:

- Catálogo de entradas.
- Generador de entradas.
- Envío de mensajes (al cliente).

Para la comunicación entre los microservicios se hará uso de sistemas de mensajería, además de que los microservicios, en caso de que fuese necesario cuenten con una API REST.

Por otro lado para el alamcenamiento de los datos se hará uso de bases de datos NoSQL, ya que nos permitirán una manipulación más dinámica de los datos.

Para el desarrollo de cada uno de los microservicios se utilizarán lenguajes de programación diferentes, como pueden ser python, ruby, node.js, java, etc.

A continuación se mostrará un diagrama:

![Diagrama ARQ](https://github.com/iMiguel10/Proyecto-CC/blob/master/img/arquitectura-cc.png)
