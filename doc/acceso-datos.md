## Configuración del acceso a datos con inversión de dependencias

Principalmente el mricroservicio que accede a una base de datos es el del catálogo, y para la configuración del acceso a los datos se hace uso, en primer lugar de un ORM, en concreto, [SQLAlchemy](https://www.sqlalchemy.org/), que me permite un nivel de abstracción superior de la base de datos. Por otra parte se definen distintas clases/archivos para evitar instroducir esa dependencia de los datos, de manera que la estructura de clases queda asi:

**BASE** ([*base.py*](https://github.com/iMiguel10/Proyecto-CC/blob/master/src/base.py))  

En ella se le pasa la url de conexión de la base de datos y se crea la sesión que se usará para el acceso.

**CATÁLOGO** ([*catalogo.py*](https://github.com/iMiguel10/Proyecto-CC/blob/master/src/catalogo.py))  

Es la que realmente accede a la base de datos y en ella se definen unos métodos que usarán otros módulos para la obtención de la información, de manera que queden desligados del acceso a base de datos.

Explicado esto vamos a ver como queda el diagrama de clases:

![Esquema](https://github.com/iMiguel10/Proyecto-CC/blob/master/doc/img/acceso-bbdd.png)
