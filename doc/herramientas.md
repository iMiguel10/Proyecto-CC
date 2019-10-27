## Herramientas del proyecto
---

Para el desarrollo del proyecto se van a necesitar hacer uso de algunas herramientas. Estas herramientas son las siguientes:

* **Lenguajes:** Para el desarrollo de los microservicios se usará Python 3, ya que se han encontrado liberías para el desarrollo de las funciones deseadas, como son, `logging` para los logs, `psycopg2` para la conexión con la base de datos, `reportlab` para la generación de PDF, `qrcode` para generar código QR para introducir en el PDF y por último `smtplib` para el envío de correos al cliente.  
Por otro lado se usará `virtualenv` como entorno virtual para el desarollo aislado de los microservicios.

* **Almacenamiento:** Para el almacenamiento de los datos en el microservico de catálogo de entradas se usuará una base de datos SQL, en concreto [ElephantSQL](https://www.elephantsql.com/). Se va a hacer uso de una base de datos SQL porque tenemos el siguiente modelo de datos para las entradas.

![Modelo de datos](https://github.com/iMiguel10/Proyecto-CC/blob/master/img/datos-bd.png)

* **Comunicación:** Los microservicios se comunicarán mediante envío de mensajes (con RabbitMQ), como muestra el diagrama de arquitectura.

* **Test:** Para el desarrollo basado en test se implementarán distintas pruebas para todos los microservicios y se hará uso [PyTest](https://docs.pytest.org/en/latest/). Se tiene pensado utilizar Travis CI, ya que nos permite pasar los test y además incorporarlo con GitHub.

* **Servicios:** Se necesitan servicios para la configuración distribuida, para ello se hará uso de [etcd](https://etcd.io/), y para el log, se usará logging, que nos permite sacar log de nuestros microservicios y se utilizará syslog para centralizarlos todos.
