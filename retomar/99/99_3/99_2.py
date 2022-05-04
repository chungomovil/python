"""Recuperar la página html 'pagina1.html' y el archivo 'imagen1.jpg' que se encuentran localizados en:
http://www.scratchya.com.ar/pythonya/ejercicio336/pagina1.html
http://www.scratchya.com.ar/pythonya/ejercicio336/imagen1.jpg
Luego grabar los dos archivos en forma local en el equipo donde se está ejecutando el script de Python."""

#Importamos libreria necesaria para conectarse con internet y el modulo para realizar peticiones http
from urllib import request
#Importamos libreria para rutas
import os

#Funcion que devuelve la ruta donde guardar los archivos
def Ruta():
    ruta=os.path.dirname(__file__)
    return ruta+"\\archivos"

#Realizamos la peticion a la url
web1=request.urlopen("http://www.scratchya.com.ar/pythonya/ejercicio336/pagina1.html")

#Leemos el contenido de la pagina
datos1=web1.read()

#Abrimos un archivo en modo escritura de bytes
archivo1=open(os.path.join(Ruta(), "pagina-web.html"), "wb") #'wb' es modo de escritura en bytes

#Insertamos el contenido de la web en el archivo
archivo1.write(datos1)

#Cerramos el archivo
archivo1.close()

#Realizamos la peticion http
web2=request.urlopen("http://www.scratchya.com.ar/pythonya/ejercicio336/imagen1.jpg")

#Leemos los datos de la web
datos2=web2.read()

#Abrimos un archivo en modo escritura de bytes
archivo2=open(os.path.join(Ruta(), "imagen.jpg"), "wb")

#Agregamos el contenido de la url al archivo
archivo2.write(datos2)

#Cerramos el archivo
archivo2.close()
