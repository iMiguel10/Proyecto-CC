# Integración Continua
---

Para añadir integración continua a nuestro proyecto vamos a utilizar Travis-CI y CircleCI, así que, para ello voy a hacer una explicación para su configuración:

### Paso 1 :
Tener el código a testear y los test en el repositorio.

### Paso 2 :
Luego tenemos que vincular nuestra cuenta de GitHub a Travis y a CircleCI, para ello basta con ir a la [página de Travis](https://travis-ci.com/) y a la de [CircleCI](https://circleci.com/).

### Paso 3 :
A continuación debemos seleccionar los repositorios que queremos que Travis y Circle pase los test.

### Paso 4 :
Para que Travis funcione correctamente es necesario añadir al repositorio un archivo de configuración [*.travil.yml*](https://github.com/iMiguel10/Proyecto-CC/blob/master/.travis.yml):
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

Y para Cirle es necesario añadir una carpeta con un archivo, [**.circleci/config.yml**](https://github.com/iMiguel10/Proyecto-CC/blob/master/.circleci/config.yml)
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

Basicamente en los 2 es necesario indicar el lenguaje y la versión del mismo, después realizar la instalación de las despendencias y por último ejecutar los test o scripts necesarios.

### Ejemplos:
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
