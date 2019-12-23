# Completar microservicios a un nivel de prestaciones determinado
---
### Objetivo

- Alcanzar **1000 hits/s** con **10 usuarios concurrentes.**

### Estado incial

Inicialmente el servicio ofrecía unas prestaciones aproximadas de 30 hits/s. Esto se debía a que el contenedor estaba desplegado en la nube y además el servidor solo contaba con 2 workers. Además había que añadir que para el almacenamiento se usaba una base de datos como servicio y el plan que se tenía solo permitía 2 ó 3 sesiones simultáneas. Todo esto favorecía unos malos resultado en cuanto al rendimiento se refiere.

Para comprobar las prestaciones iniciales, se ha usado el siguiente fichero de configuración que usa Taurus para comprobar las prestaciones.
En nuestro caso será de 10, (para satisfacer el objetivo), y a continuación podemos ver el que se han establecido 10s para alcanzar ese número de usuarios y que los mantenga durante 20s. Por último definimos un escenario, que vamos a utilizar. En el especificaremos las rutas a las que se van a realizar las peticiones. Para nosotros se hará a la dirección raiz, ya que es un simple test para comprobar las prestaciones.

```yaml
execution:
- concurrency: 10
  ramp-up: 10s
  hold-for: 20s
  scenario: quick-test

scenarios:
  quick-test:
    requests:
    - http://localhost:5000/
```

### Alcanzando objetivos

Para intentar alcanzar los objetivos establecidos, se han llevado a cabo las siguientes tareas:

- Uso de una base de datos local.
- Despliegue del servicio en local.
- Utilizar 4 workers en el servidor en vez de 2.

**Con la realización de estas acciones conseguimos llegar a 900 hits/s.** Una mejora bastante buena pero mejorable.

![4 Workers](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/img/4w.png)

Una vez llegados a este estado vamos a intentar mejorar la configuración del servidor para ver si conseguimos mejores prestaciones. Por ello a continuación **se utilizaron 10 workers** ya que es el nivel de concurrencia objetivo. Con esta acción casi se consiguió llegar al nivel de prestaciones objetivo, llegando a los **940 hits/s**. No fue una mejora sustancial pare es mejor que la anterior.  

![10 Workers](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/img/10w.png)

Por último, se ha intentado mejorar las prestaciones utilizando hebras en el servidor, en concreto 2, y utilizando workers de la clase *gevent*, con un número de 4. Se han utilizado esta métricas ya que mi ordenador personal tiene 4 cores físicos y 2 cores virtuales por cada uno de ellos, es decir 8. Por lo tanto con esta medida al fin se consiguieron el nivel de prestaciones objetivo, llegando a los **1200 hits/s**

![4 Workers - 2 Threads](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/img/4w-2t.png)


### Bibiografía:

* https://medium.com/building-the-system/gunicorn-3-means-of-concurrency-efbb547674b7
* https://stackoverflow.com/questions/10938360/how-many-concurrent-requests-does-a-single-flask-process-receive
* https://gettaurus.org/
