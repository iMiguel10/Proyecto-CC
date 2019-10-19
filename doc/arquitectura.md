## Arquitectura del proyecto
---

La arquitectura será mixta, estará basada en microservicos y en paso de mensajes, para puedan ser desarrollados y desplegados de forma independiente y con lenguajes distintos y además de que se puedan comunicar de forma asíncrona, así que, nos quedarán los siguientes:

- **Catálogo de entradas:** Será el encargado de realizar operaciones con las entradas, es decir, mostrar entradas disponibles, ver entradas asociadas a un usuario, comprar una entrada, etc.
- **Generador de entradas:** Será el encargado de generar una entrada en PDF y almacenarlo.
- **Envío de mensajes (al cliente):** Será el encargado de enviar un mensaje al cliente notificándolo con información o enviando la entrada comprada.

- **Posibles servicios adicionales:** Existe la posibilidad de que se necesite un servicio de configuración remoto (como etcd).

Para la comunicación entre los microservicios se hará uso de sistemas de mensajería haciendo uso del protocolo AMQP, además de que los microservicios, en caso de que fuese necesario cuenten con una API REST. Será necesario AMQP ya que los procesos de generación de PDF y envío de mensajes al cliente tardarán un tiempo indeterminado y por otra parte los demás no necesitan una respuesta.

Por otro lado para el almacenamiento de los datos en el *catálogo de entradas* se hará uso de bases de datos NoSQL, ya que nos permitirán una manipulación más dinámica de los datos.

Para el desarrollo de cada uno de los microservicios se utilizarán lenguajes de programación diferentes, como pueden ser python, ruby, node.js, java, etc.

A continuación se mostrará un diagrama:

![Diagrama ARQ](https://github.com/iMiguel10/Proyecto-CC/blob/master/img/arquitectura-cc.png)
