# Goodservice

Caso número 3 portafolio de título

En el backend en settings.py, en la sección Databases, deben cambiar el name a su localhost con el puerto en que esté conectado el sql developer.

En el front deben ingresar a la carpeta front end, hacer un npm install, para que se instalen los paquetes que requiere react para funcionar.

Finalmente ejecutar el comando npm run build, para que se cree la carpeta build, que es la que está sincronizada con el backend.

En python para crear un superuser deben estar a la misma altura en consola que el archivo manage.py y ejecutar el siguiente comando.

python3 manage.py createsuperuser (no se en windows si deben usar ek python3, en mac asi debo hacerlo xd)

completar los datos correspondientes de que serán solicitados en consola.

Luego

python3 manage.py makemigrations  para que se realicen los cambios hechos en la bd.
python3 manage.py migrate para que se migren los cambios
python3 manage.py runserver para correr el servidor

Con eso debería bastar ingresan al IP que les genera el servidor y al final le ponen /admin y podran loguearse con el super user que crearon.
