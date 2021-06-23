"""Recuperar la página html 'pagina1.html' que se encuentra localizada en:
http://www.scratchya.com.ar/pythonya/ejercicio336/pagina1.html"""

#Importamos del paquete necesario para conectarnos con internet, el modulo para hacer peticiones a las paginas web
from urllib import request

#Hacemos una peticion http de la url en cuestion
pagina=request.urlopen("http://www.scratchya.com.ar/pythonya/ejercicio336/pagina1.html")

#Leemos los datos de dicha pagina (en bloque de bytes)
datos=pagina.read()
#Imprimimos el bloque de bytes resultante
print(datos)
