## Configuración SSH
---

Para llevar a cabo la configuración de SSH, de manera que podamos hacer `git push` sin necesidad de introducir nuestras credenciales se han seguido los siguientes pasos:

### 1. Generar un par de claves SSH

Para generar la claves solamente se ha usado `ssh-keygen`, de esta manera hemos obtenido un par de claves.

---

### 2. Incorporar las claves a GitHub

---

Una vez que tenemos las claves, vamos a:  
**GitHub -> Personal Setting -> SSH and GPG keys -> New SSH key.**

Ahora le damos un nombre a la clave y pegamos el contenido del archivo que contiene nuestra clave pública *~/.ssh/id_rsa.pub*, y añadimos la clave.

![SSH KEYS]()

### 3. Cambiar el URL del repositorio

Cambiamos el url del repositorio en caso de que los cambios los suba a través de http. Esto lo podemos comprobar con `git remote -v`.
En mi caso yo cambié _https://github.com/iMiguel10/Proyecto-CC.git_ por _git@github.com:iMiguel10/Proyecto-CC.git_ con `git remote set-url origin git@github.com:iMiguel10/Proyecto-CC.git`.

### 4. Probar
---
Probamos que todo funcione correctamente.

![SSH PRUEBA]()

**NOTA:** Se ha seguido el siguiente tutorial [Autenticar con clave pública](https://www.linuxito.com/programacion/1041-como-autenticar-con-clave-publica-en-github).
