[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Build Status](https://travis-ci.com/iMiguel10/Proyecto-CC.svg?branch=master)](https://travis-ci.com/iMiguel10/Proyecto-CC)
[![CircleCI](https://circleci.com/gh/iMiguel10/Proyecto-CC.svg?style=svg)](https://circleci.com/gh/iMiguel10/Proyecto-CC) [![codecov](https://codecov.io/gh/iMiguel10/Proyecto-CC/branch/master/graph/badge.svg)](https://codecov.io/gh/iMiguel10/Proyecto-CC)  [![DevQAGRX](https://img.shields.io/badge/DevQAGRX-blueviolet?style=svg&logo=Git)](https://github.com/JJ/curso-tdd)
# Proyecto-CC (Gestión de entradas)

El proyecto consistirá en una serie de microservicos en la nube, entre los que existen, uno para el catálogo o gestión de entradas, otro para la generación de esas entradas y otro posible microservicio para el envio de mensajes al cliente.  
El proyecto está pensado para incorporarse en una aplicación de eventos en los que hay una venta de entradas online, enfocada a empresas organizadoras de los mismos.

## Empezar
Para la instalación, testeo y ejecución del proyecto, en nuestra máquina local será necesario realizar las siguientes acciones.

#### Prerrequisitos
Es neceario tener instalado **python 3** y la herramienta de construcción **invoke**.
~~~
Versión de desarrollo: Python 3.6.8   
~~~
Por otro lado son necesarias las siguientes **variables de entorno**:

~~~
MAIL: Dirección de correo (Gmail) emisor de los mensajes.   
MAIL_PASS: Contraseña de la dirección de correo emisor.  
BD: URL de conexión con la base de datos.  
CODECOV_TOKEN: Token para subir los datos de los test de cobertura a codecov.  
AMQP_SERVER: URL de conexión con el servidor de colas AMQP.
~~~

#### Instalación
Para la instalación del proyecto es necesario:  

**Paso 1:** Clonar el repositorio.  
~~~

git clone https://github.com/iMiguel10/Proyecto-CC.git

~~~

**Paso 2:** Instalar dependecias.  
~~~

invoke install [-m/--ms <microservicio>]

~~~

**Paso 3:** Adicionalme si queremos construir el contenedor docker.
~~~

invoke buildDocker [-r/--ruta <Dockerfile path>]

~~~

Una vez hecho esto tendremos todo lo necesario para poder testear y usar los microservicios.

#### Ejecutar test
Para ejecutar los test se va a usar [PyTest](https://docs.pytest.org/en/latest/), pero todo esto quedará automatizado con la herramienta de construcción. Y se podrá hacer de la siguiente manera.

~~~

invoke test

~~~

Además de ejecutar los test se puede ver los resultados de los test de cobertura realizando lo siguiente en la carpeta de [test]().

~~~

coverage report -m

~~~

Para la integración continua se han usado CircleCI ([config.yml](https://github.com/iMiguel10/Proyecto-CC/blob/master/.circleci/config.yml)), que testea la versión 3.5 y TravisCI ([.travis.yml](https://github.com/iMiguel10/Proyecto-CC/blob/master/.travis.yml)), que testea la versión 3.6.8 y la 3.7.

~~~

buildtool: tasks.py

~~~

#### Despliegue
Para el despliegue de los microservicios implementados es necesario volver a usar la herramienta de construcción de la siguiente manera.

~~~

invoke start [-p/--port <puerto>] [-m/--ms <microservicio>] [-w/--workers <nº>]

~~~

Con esto levantamos el servidor wsgi en el puerto especificado, o por el contrario en el 8080 (defecto).

Adicionalmente si queremos parar el servicio podemos relaizar lo siguiente.

~~~

invoke stop

~~~

Por último si hemos contruido la imagen docker en la instalación, también podemos ejecutarla.

~~~

invoke runDocker [-v/--variables <fichero-variables-entorno] [-p/--port <puerto>]

~~~

Además se ha podido desplegar en Google Cloud, haciendo uso de [Cloud Run](https://cloud.google.com/run/?hl=es). A continuación se muestra la ruta del despligue.

~~~

Catalogo Eventos (Desplegado): https://catalogo-augbbnavea-ew.a.run.app

~~~


#### Publicación y descarga de contenedores

~~~
Contenedor: https://hub.docker.com/r/imiguel10/catalogo-eventos
~~~


- **Google:** `docker pull gcr.io/proyecto-cc-260418/github.com/imiguel10/proyecto-cc:catalogo-latest` --> MS: Catálogo
- **Google:** `docker pull gcr.io/proyecto-cc-260418/github.com/imiguel10/proyecto-cc:generador-latest` --> MS: Generador PDF
- **Google:** `docker pull gcr.io/proyecto-cc-260418/github.com/imiguel10/proyecto-cc:sender-latest` --> MS: Sender de correo
- **GitHub:** `docker pull docker.pkg.github.com/imiguel10/proyecto-cc/catalogo:latest` --> MS: Catálogo
- **GitHub:** `docker pull docker.pkg.github.com/imiguel10/proyecto-cc/generador:latest` --> MS: Generador PDF
- **GitHub:** `docker pull docker.pkg.github.com/imiguel10/proyecto-cc/sender:65e7c1795c0d` --> MS: Sender de correo
- **DockerHub:** `docker pull imiguel10/catalogo-eventos:latest` --> MS: Catálogo
- **DockerHub:** `docker pull imiguel10/catalogo-eventos:latest-generador` --> MS: Generador PDF
- **DockerHub:** `docker pull imiguel10/catalogo-eventos:latest-sender` --> MS: Sender de correo

#### Medición de prestaciones

Para la medición de las prestaciones se ha usado Taurus, con el fichero de configuración **quick_test.yml**. Haciendo uso de la siguiente orden: `bzt quick_test.yml -report`.
~~~
Prestaciones: quick_test.yml
~~~

#### Máquinas virtuales, provisionamiento y despliegue

Para la creación de las máquinas virtuales, provisionamiento y despliegue de las mimas se han usado ficheros de ansibles y un fichero de fabric. De esta manera hemos podido automatizar estas tareas, además de poder replicar estas acciones.

Para llevar a cabo estas tareas es necesario lo siguiente:

**Provisionamiento:** `ansible-playbook [playbook]`  

**Despliegue:** `fab [tarea] [parámetros]`
* Tareas: `install, start, stop, update`

**NOTA:** Es necesario estar en el directorio en el que se encuentran los ficheros, provision o despliegue.

#### Autores

- [**Miguel Jiménez Cazorla**](https://github.com/iMiguel10) - Desarrollador principal.

### Licencia

Este proyecto esta bajo la licencia LGPL v3 - Ver [LICENSE](https://github.com/iMiguel10/Proyecto-CC/blob/master/LICENSE) para más detalle.

#### Documentación Extra

- [**Historias de usuario**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/historias-usuario.md)
- [**Documentación Arquitectura**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/arquitectura.md)
- [**Documentación Herramientas**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/herramientas.md)
- [**Documentación Integración Continua**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/integracion-continua.md)
- [**Documentación Contenedores-Microservicios**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/contenedores-microservicios.md)
- [**Resultados ab**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/resultados-ab.md)
- [**Documentación Prestaciones**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/prestaciones.md)
- [**Documentación Acceso a datos**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/acceso-datos.md)
- [**Documentación Provisionamiento**](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/provisionamiento.md)
