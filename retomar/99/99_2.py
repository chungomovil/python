"""Recuperar la página html 'pagina1.html' que se encuentra localizada en:
http://www.scratchya.com.ar/pythonya/ejercicio336/pagina1.html
Decodificar los datos recuperados a UTF-8"""


#Importamos del paquete para conectarnos a internet el modulo para realizar peticiones
from urllib import request

#Hacemos una peticion http para resolver la url citada
pagina=request.urlopen("http://www.scratchya.com.ar/pythonya/ejercicio336/pagina1.html")

#Almacenamos el contenido (en bloque de bytes) en una variable
datos=pagina.read()

#Decodificamos la informacion a formato utf para que sea mas legible
datosutf8=datos.decode("utf-8")

#Mostramos el resultado
print(datosutf8)
