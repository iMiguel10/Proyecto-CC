# Integración Continua
---

### Herramienta de construcción

Se ha usado invoke como herramienta de construción para automatizar las tareas. Esta herramienta hace uso del archivo [tasks.py](https://github.com/iMiguel10/Proyecto-CC/blob/master/tasks.py), que es en el que se definen las tareas.

~~~

#!/usr/bin/python
# -*- coding: utf-8 -*-

from invoke import task, run

# Tarea para instalar dependencias
@task
def build(ctx):
    print("Instalando dependencias...")
    ctx.run("pip install -r requirements.txt")
    print("HECHO!")

# Tarea para ejecutar los tests
@task
def test(ctx):
    with ctx.cd('test/'):
        print("Testeando...")
        ctx.run("pytest --cov=./")
        print("Testeado!")

# Tarea para codecov
@task
def codecov(ctx):
    with ctx.cd('test/'):
        ctx.run("codecov")

~~~

Para definir una tarea es necesario poner el decorador `@task` y debajo la función que va a realizar esa tarea. Por ello en nuestro caso como podemos ver tenemos 3 tareas:
+ **build:** Es la tarea usada para la instalación de las dependecias.
+ **test:** Es la tarea usada para ejecutar los test.
+ **codecov:** Es la tarea que se usa para enviar los resultados de test de cobertura a codecov.

Como veremos a continuación los sistemas de integración contínua harán uso de ella de la siguiente forma:
+ `invoke test`
+ `invoke codecov`
+ `invoke build`

### Incorporación de sistemas CI

Para añadir integración continua a nuestro proyecto vamos a utilizar Travis-CI y CircleCI, así que, para ello voy a hacer una explicación para su configuración:

#### Paso 1 :
Tener el código a testear y los test en el repositorio.

#### Paso 2 :
Luego tenemos que vincular nuestra cuenta de GitHub a Travis y a CircleCI, para ello basta con ir a la [página de Travis](https://travis-ci.com/) y a la de [CircleCI](https://circleci.com/).

#### Paso 3 :
A continuación debemos seleccionar los repositorios que queremos que Travis y Circle pase los test.

#### Paso 4 :
Para que **Travis** funcione correctamente es necesario añadir al repositorio un archivo de configuración [*.travil.yml*](https://github.com/iMiguel10/Proyecto-CC/blob/master/.travis.yml):
~~~
language: python

python:
  - "3.6.8"

install:
  - pip install -r requirements.txt

script:
  - invoke test
  - invoke codecov
~~~


En este archivo de configuración podemos ver lo siguiete:
+ **language:** Especificamos el lenguaje que se va a usar.
+ **python:** Especificamos las versiones del lenguaje que queremos usar.
+ **install:** En este apartado indicamos las ordenes que llevarán a cabo las instalación de dependencias antes de que se ejecuten los scripts.
+ **script:** Aquí especificamos los scripts que queremos que se ejecuten. En nuestro caso queremos que se ejecuten los test y se suban a codecov haciendo uso de invoke con las tareas definidas dentro del tasks.py.


Y para **Cirle** es necesario añadir una carpeta con un archivo, [**.circleci/config.yml**](https://github.com/iMiguel10/Proyecto-CC/blob/master/.circleci/config.yml)
~~~
version: 2
jobs:
  build:
    docker:
      - image: circleci/python:3.5
    steps:
      - checkout
      - run:
          name: Instalando dependencias
          command: |
            python3 -m venv venv
            . venv/bin/activate
            pip install -r requirements.txt
      - run:
          name: Ejecutando test
          command: |
            . venv/bin/activate
            invoke test
~~~

En este archivo de configuración, en este caso de Circle podemos ver lo siguiete:
+ **jobs:** Dentro de este apartado vamos a definir los trabajos que se van a llevar a cabo.
+ **build:** Especificamos que se va a usar docker con la imagen que deseemos. En nuestro caso vamos a usar una acorde con el lenguaje que usamos en el proyecto, junto con la versión, que en este caso es la mínima con la que funciona.
+ **steps:** Son los pasos que se van a dar dentro de ese trabajo o tarea. En nuestro caso tenemos 3:
  + **checkout:** Se utiliza para verificar el código fuente de la ruta configurada, en nuestro caso es el directorio raiz del proyecto por defecto.
  + **run:** Para que todo funcione correctamente, primero creamos un entorno virtual y lo activamos y a continuación instalamos las dependencias.
  + **run:** Por último volvemos a activar el entorno y ejecutamos los test con invoke.

#### Ejemplos:
![Ejemplo Travis](https://github.com/iMiguel10/Proyecto-CC/blob/master/img/integracion-continua.png)   
![Ejemplo Circle](https://github.com/iMiguel10/Proyecto-CC/blob/master/img/integracion-continua2.png)

### Test
Los [test](https://github.com/iMiguel10/Proyecto-CC/tree/master/test) que se han escrito son para comprobar la funcionalidad de los [microservicios](https://github.com/iMiguel10/Proyecto-CC/tree/master/src).

**MS: GeneradorPDF**
+ **test_generarQR:** Comprueba que se genera correctamente un código QR.
+ **test_generarPDF:** Comprueba que se genera correctamente un PDF.

**MS: Gestor de correo**
+ **test_crearMensaje:** Comprueba que se crea correctamente un mensaje.
+ **test_adjuntar:** Comprueba que se adjunta un archivo correctamente.
+ **test_enviar:** Comprueba que se envía un correo correctamente.

Además de estos test se han incorporado test de cobertura. Para ver los resultados podemos hacer lo siguiente: `invoke test` y después `coverage report -m` dentro de la carpeta de test. O en [codecov](https://codecov.io/gh/iMiguel10/Proyecto-CC).
