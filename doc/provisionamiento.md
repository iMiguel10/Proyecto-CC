# Provisionamiento de máquinas virtuales
---

Para el provisionamiento de máquinas virtuales se ha usado ansible, pero no solo para eso, si no que también ha servido para la creación de las mismas. Además se ha hecho uso de fabric para la realización de tareas en las máquinas ya desplegadas.

### Creación de máquinas virtuales
En primer lugar es necesario crear las máquinas virtuales, se van a hacer uso de 3 máquinas virtuales, una para cada microservicio, para ello se ha hecho uso de este [playbook](https://github.com/iMiguel10/Proyecto-CC/blob/master/provision/create_instances.yml):
```yaml

# Playbook para la creación de las máquinas virtuales que albergarán los microservicios
- name: Creación de las instancias
  hosts: localhost
  vars:
    service_account_email: "988662035384-compute@developer.gserviceaccount.com"
    credentials_file: "key.json"
    project_id: "proyecto-cc-260418"
  tasks:
    - name: Crear las instancias
      gce:
        instance_names: catalogo,generadorpdf,sender
        zone: europe-west2-a
        machine_type: n1-standard-1
        image: ubuntu-minimal-1804-bionic-v20200108
        state: present
        service_account_email: "{{ service_account_email }}"
        credentials_file: "{{ credentials_file }}"
        project_id: "{{ project_id }}"
      register: gce

    - name: Esperar al SSH de las instancias
      wait_for:
        delay: 1
        host: "{{ item.public_ip }}"
        port: 22
        state: started
        timeout: 30
      with_items: "{{ gce.instance_data }}"

    - name: Guardar en el /etc/ansible/hosts las IPs de las máquinas creadas
      lineinfile:
        path: /etc/ansible/hosts
        line: "[{{ item.name }}]\n{{ item.public_ip }}"
      with_items: "{{ gce.instance_data }}"
```

Este playbook tiene o esta dividido en 3 tareas, pero primero es necesario especificar las variables. Como en nuestro caso las máquinas las vamos a tener en Google es necesario especificar esos campos, y para ello tenemos que generar un fichero .json con nuestras credenciales desde la consola de Google. Una vez que tenemos declaradas las variables, podemos crear las máquinas, en esa tarea podemos especificar el nombre, zona (ubicación de la máquina), tipo de máquina(size), la imágen (sistema operativo). Tras esta tarea vamos a iniciar el SSH de cada una de las instancias creadas. Y por último vamos a guardar el nombre y la IP asociada a cada instancia en el fichero de ansible host para luego poder referenciarlas y provisionarlas.

### Provisionamiento común a todas las instancias
Como existen semejanzas en entre las instancias creadas, se ha diseñado un playbook en el cual se realizan tareas comunes para ellas. Estas tareas son la instalación de git, o el lenguaje de progrmación, así como la descarga de los ficheros del proyecto.

```yaml

# Playbook para la realización de las tareas comunes de todas las máquinas
- name: Tareas comunes a todas las máquinas
  hosts: all
  become: yes

  tasks:

  - name: Actualizar sistema
    command: apt update

  - name: Instalar paquetes necesarios
    apt:
      pkg: ["git"]
      state: present

  - name: Instalar dependencias para instalar el lenguaje
    apt:
      pkg: software-properties-common

  - name: Actualizar sistema
    command: apt update

  - name: Instalar Python3.6
    apt:
      pkg: ["python3.6","python3-pip"]
      state: present

  - name: Descargar fuentes desde GitHub
    git:
      repo: https://github.com/iMiguel10/Proyecto-CC.git
      dest: ./Proyecto_CC
      version: master

```

### Provisionamiento de la instancia del catálogo
Para la instancia que contendrá el microservicio del catálogo, será necesario la instalación de postgresql y la creación de las tablas, por ello se han usado 2 playbooks distintos.

```yaml

- name: Creación de la base de datos Postgresql
  hosts: catalogo
  become: yes
  vars_files:
    - vars/main.yml

  roles:
    - role: geerlingguy.postgresql

```
 En este playbook se ha usado la galaxia de ansible de manera que se han facilitado las tareas, ya que solo ha sido necesario la instalación y un fichero de varibles([main.yml](https://github.com/iMiguel10/Proyecto-CC/blob/master/provision/vars/main.yml)), en el que hemos especificado, los valores de la base de datos y los usuarios, en nuestro caso una base de datos (bd) y un usuaro (vagrant).

A continuación vamos a ver el playbook en el que creamos la tabla con el modelo de datos. En el podemos ver una tarea en la que con una query en SQL creamos la tabla, en la base de datos y con el usuario anteriormente creados, con los campos necesarios.

```yaml
- name: Creación de la base de datos Postgresql
  hosts: catalogo
  become: yes
  become_user: vagrant

  tasks:
    - name: Crear tabla entradas
      postgresql_query:
        db: db
        login_password: "{{ lookup('env','BD_PASSWORD') }}"
        login_user: vagrant
        query: CREATE TABLE entradas (id  SERIAL PRIMARY KEY,evento VARCHAR(50),precio NUMERIC(5,2),propietario VARCHAR(100),descripcion TEXT);
```

### Despliegue
Por otro lado para realizar tareas a través de SSH se ha usado fabric. Con esto hemos conseguido automatizar algunas tareamos como instalar dependencias, parar o iniciar los microservicios y actualizar los fuentes. Como estas tareas son comunes a todas las máquinas se ha incorporado la opción de especificar el host al que te conectas mediante una variable de entorno.

```python

# Fabfile to:
#    - Instalar requeriments
#    - Parar
#    - Actualizar
#    - Iniciar

import os

# Import Fabric's module
from fabric import *


def getConnection():
    h = os.environ['HOST']
    c = Connection(host=h, user='vagrant', port=22, connect_kwargs={
            "key_filename": "/home/vagrant/.ssh/id_rsa",
        })
    return c

@task
def install(ctx,ms="all"):
    c = getConnection()
    # Iniciamos el servicio web
    with c.cd('Proyecto_CC/'):
        if (ms == "all"):
            c.run("pip3 install -r requirements.txt")
        else:
            c.run("pip3 install -r requirements-"+ms+".txt")


@task
def start(ctx,port=8080,workers=4,ms="all"):
    c = getConnection()
    # Iniciamos el servicio web
    with ctx.cd('Proyecto_CC/src/'):
        if (ms == "all" or ms == "catalogo"):
            c.run("gunicorn app:app --threads=2 --worker-class=gevent -w "+str(workers)+"  -b :"+str(port)+" &")
        if (ms == "all" or ms == "generador"):
            c.run("python3 generadorEntradas.py &")
        if (ms == "all" or ms == "sender"):
            c.run("python3 emailSender.py &")

# Tarea para parar el servicio
@task
def stop(ctx):
    """Para el servicio web. Que se puede lanzar con invoke start [-p/--port <puerto>]"""
    c = getConnection()
    c.run("pkill gunicorn")

@task
def update(ctx):
    c = getConnection()
    # Iniciamos el servicio web
    with c.cd('Proyecto_CC/'):
        c.run("git pull")

```

### Comprobar prestaciones
Por último vamos a comprobar las prestaciones que nos presentan las máquinas, haciendo uso de Taurus como se hizo anteriormente. Para ello se ha utilizado el mismo fichero de configuración, pero cambiando el url al que se le hacen las peticiones.

```yaml
execution:
- concurrency: 10
  ramp-up: 10s
  hold-for: 20s
  scenario: quick-test

scenarios:
  quick-test:
    requests:
    - http://<ip>:<port>/
```
Estos son los resultados obtenidos:

![Prestaciones](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/img/prestaciones-antigua.png)

Los resultados obtenidos han sido bastante malos, por ello se ha creado una máquina con un número mayor de CPUs, pero los resultados no mejoran, incluso empeoran.

### Bibliografía:

**Principales:**

* [Ansible y VM en Google](https://docs.ansible.com/ansible/latest/modules/gce_module.html)
* [Guía Ansible para GCE](https://docs.ansible.com/ansible/latest/scenario_guides/guide_gce.html)
* [Credenciales Google](https://pygsheets.readthedocs.io/en/latest/authorization.html)
* [Tipos de máquinas de Google](https://cloud.google.com/compute/docs/machine-types)
* [Imágenes disponibles de Google](https://cloud.google.com/compute/docs/images?hl=es)
* [Postgresql Ansible Galaxy](https://galaxy.ansible.com/galaxyproject/postgresql)
* [Módulo DB de Posgresql Ansible](https://docs.ansible.com/ansible/latest/modules/postgresql_db_module.html)
* [Módulo tablas de Posgresql Ansible](https://docs.ansible.com/ansible/latest/modules/postgresql_table_module.html)
* [Módulo usuarios de Posgresql Ansible](https://docs.ansible.com/ansible/latest/modules/postgresql_user_module.html)

**Otros:**

* https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html#playbook-language-example
* https://docs.ansible.com/ansible/latest/modules/copy_module.html
* https://docs.ansible.com/ansible/latest/modules/lineinfile_module.html
