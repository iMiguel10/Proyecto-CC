# Contenedores para microservicios
---

### Microservicios

Se ha implementado un microservicio que consiste en realizar consultas a una base de datos que contiene la información de entradas para eventos. Para ello primero ha sido necesario, como se va a usar un ORM, definir un modelo de datos ([models](https://github.com/iMiguel10/Proyecto-CC/blob/master/src/models.py)), a continuación se ha definido una capa de operaciones o funciones para manejar los datos que intercambiamos con la base de datos, ([catálogo](https://github.com/iMiguel10/Proyecto-CC/blob/master/src/catalogo.py)), y por último una API REST, que es la que permitirá el acceso a esas funciones([app](https://github.com/iMiguel10/Proyecto-CC/blob/master/src/app.py)).  

~~~
            --> Catalogo ---> Modelo de datos de entradas
            |                    _
API REST -----> GeneradorPDF      |
            |                     |- Esto se ha incluido a modo de prueba
            --> EnviarEntradas   _|

~~~

**Nota:** A modo de prueba se han incorparado los otros 2 módulos, el [generadorEntradasPDF](https://github.com/iMiguel10/Proyecto-CC/blob/master/src/generadorentradasPDF.py) y [enviarEntradas](https://github.com/iMiguel10/Proyecto-CC/blob/master/src/enviarEntradas.py).

Como podemos ver en las acciones que puede realizar el usuario quedan recogidas o ajustadas las [historias de usuario](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/historias-usuario.md) que establecimos al comienzo del desarrollo del proyecto.

Por supuesto, todo el desarrollo queda testeado. Estos test los podemos ver en la carpeta ['test'](https://github.com/iMiguel10/Proyecto-CC/tree/master/test). Y se puede comprobar o ejecutar con la orden `invoke test`.

### Dockerfile

A continuación vamos a ver como hemos construido el contenedor docker que albergará nuestro proyecto a partir de un Dockerfile, el cual, explicaremos que opciones tiene y como funciona o que resultados se espera de cada una de ellas.

Se ha probado con 3 Dockerfile distintos, los tres igual de válidos, pero nos hemos quedado con el primero porque el tamaño de la imagen es mucho más pequeña y además lleva ya incorporado python, en comparación con el último de ubuntu. Los tamaños podemos verlos en la siguiente imagen, donde están los contenedores de python slim, de python en alpine y de ubuntu.

![Imagenes docker](https://github.com/iMiguel10/Proyecto-CC/blob/master/img/imagenes-docker.png)

A continuación vamos a ver los diferentes Dockerfile creados.

###### Dockerfile 1 (Python-Slim)

~~~
FROM python:3.6-slim

LABEL maintainer="imiguel10@correo.ugr.es"

COPY requirements.txt ./
COPY tasks.py ./
RUN pip install invoke
RUN invoke install

COPY src/ src/

EXPOSE 8080

CMD ["invoke", "start"]
~~~

Ahora vamos a explicar el contenido del mismo, instrucción por instrucción:
- **FROM:** Contenedor que elegimos como base. En este caso uno de python3.6 porque es la versión de desarrollo del microservico y slim porque queremos que el espacio ocupado sea el mínimo.
- **LABEL:** Etiqueta que define la persona encargada de crear esta nuevo contenedor, y es introducido como metadatos.
- **COPY:** Copiamos el archivo requirements en el directorio actual.
- **COPY:** Copiamos el archivo tasks.py en el directorio actual.
- **RUN:** Instalamos primero Invoke.
- **RUN:** Instalamos las dependecias del proyecto con invoke.
- **COPY:** Copiamos la carpeta donde se encuentra nuestro programa.
- **EXPOSE:** Nos permite especificar que puertos va a escuchar el contenedor. En nuestro caso hemos elegido el 8080.
- **CMD:** Proporcionamos al contendor la ejecución de levantar el servicio REST por defecto.

###### Dockerfile 2 (Python3-Alpine)

~~~
FROM python:3.6-alpine

LABEL maintainer="imiguel10@correo.ugr.es"

COPY requirements.txt ./
COPY tasks.py ./
# Dependecias para psycopg2
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
# Dependecias para Pillow
RUN apk add --no-cache jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev
RUN apk add --no-cache bash
RUN pip install invoke
RUN invoke install

COPY src/ src/

EXPOSE 8080

CMD ["invoke", "start"]
~~~

Al igual que en el anterior vamos a explicar el contenido:
- **FROM:** Contenedor que elegimos como base. En este caso uno de python3.6 porque es la versión de desarrollo del microservico y alpine porque estas imagenes base tienen alrededor de 5MB de tamaño.
- **LABEL:** Etiqueta que define la persona encargada de crear esta nuevo contenedor, y es introducido como metadatos.
- **COPY:** Copiamos el archivo requirements en el directorio actual.
- **COPY:** Copiamos el archivo tasks.py en el directorio actual.
- **RUN:** Es necesario para instalar las dependecias para psycopg2.
- **RUN:** Es necesario para instalar las dependecias de Pillow.
- **RUN:** Añadimos el bash para utilizarlo en las siguientes ordenes.
- **RUN:** Instalamos primero Invoke.
- **RUN:** Instalamos las dependecias del proyecto con invoke.
- **COPY:** Copiamos la carpeta donde se encuentra nuestro programa.
- **EXPOSE:** Nos permite especificar que puertos va a escuchar el contenedor. En nuestro caso hemos elegido el 8080.
- **CMD:** Proporcionamos al contendor la ejecución de levantar el servicio REST por defecto.


###### Dockerfile 3 (Ubuntu)

~~~
FROM ubuntu:latest

LABEL maintainer="imiguel10@correo.ugr.es"

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN ln -s /usr/bin/pip3 /usr/bin/pip
COPY requirements.txt ./
COPY tasks.py ./
RUN pip install invoke
RUN invoke install

COPY src/ src/

EXPOSE 8080

CMD ["invoke", "start"]
~~~

Al igual que en el anterior vamos a explicar el contenido:
- **FROM:** Contenedor que elegimos como base. En este caso uno de ubuntu:latest el sistema operativo en el que se esta desarrollando (18.04).
- **LABEL:** Etiqueta que define la persona encargada de crear esta nuevo contenedor, y es introducido como metadatos.
- **RUN:** Actualizamos el sistema.
- **RUN:** Instalamos python3.
- **RUN:** Instalamos pip3.
- **RUN:** Para que pip3 sea igual que pip creamos un enlace simbólico.
- **COPY:** Copiamos el archivo requirements en el directorio actual.
- **COPY:** Copiamos el archivo tasks.py en el directorio actual.
- **RUN:** Instalamos primero Invoke.
- **RUN:** Instalamos las dependecias del proyecto con invoke.
- **COPY:** Copiamos la carpeta donde se encuentra nuestro programa.
- **EXPOSE:** Nos permite especificar que puertos va a escuchar el contenedor. En nuestro caso hemos elegido el 8080.
- **CMD:** Proporcionamos al contendor la ejecución de levantar el servicio REST por defecto.

Una vez vistos todos los Dockerfile vamos e ver qué instrucciones se han usado para construir y ejecutar las contenedores/imagenes.  
Para construir los contenedores realizamos la orden:  
`[sudo] docker build -t app .`  
* Con esta orden constrimos la imagen con el nombre _app_ en el directorio que nos encontramos.

Para ejecutar el contenedor realizamos lo siguiente:  
`[sudo] docker run -it --env-file variables --rm --name name-app -p 8080:80 app`
* Con esta orden ejecutamos la imagen.
* _-it_: nos permite conectarnos con el contenedor de forma interactiva.
* _--env-file_: nos permite pasarle las variables de entorno en un fichero.
* _--rm_: nos permite borrar automáticamente el contenedor cuando no se esta ejecutando.
* _--name_: nos permite asiganarle un nombre al contenedor.
* _-p_: nos permite especificar el mapeo de puertos entre el contenedor y la máquina anfitriona.
* _app_: es el nombre que le pusimos anteriormente al contenedor.

Por otro lado los contenedores se han publicado en:
~~~
Docker Hub: https://hub.docker.com/r/imiguel10/catalogo-eventos/dockerfile

GitHub: https://github.com/iMiguel10/Proyecto-CC/packages/65465?version=latest
~~~

### Bibiografía:

- https://docs.docker.com/engine/reference/builder/
- https://docs.docker.com/engine/reference/commandline/run/
- https://hub.docker.com/_/python
- https://hub.docker.com/_/ubuntu
- https://help.github.com/es/github/managing-packages-with-github-packages/configuring-docker-for-use-with-github-packages
