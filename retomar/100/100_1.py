"""Ahora implementaremos una aplicación en Python que recupere y muestre los datos del archivo JSON que devuelve como resultado el archivo de PHP 'retornararticulos.php'"""

#Importamos las librerias necesarias
from urllib import request
#Libreria para transformar datos a json
import json

#Realizamos la peticion al servidor
peticion=request.urlopen("http://web/retornararticulos.php")
#Analizamos los datos
datos=peticion.read()
#Codificamos los datos para mejor legibilidad
datosutf8=datos.decode("utf-8")
print(100*"_")
#Mostramos datos codificados
print(datosutf8)
#Transformamos los datos a json
datosjson=json.loads(datosutf8)
print(100*"_")
#Mostramos los datos codificados en json
print(datosjson)
print(100*"_")
print(f"{'CODIGO':<15}{'DESCRIPCION':<25}{'PRECIO'}")
#Recorremos y mostramos los datos en json en una tabla (RECORDAR: al codificados a json estamos recorriendo un diccionario)
for articulo in datosjson:
    codigo=articulo["codigo"]
    descripcion=articulo["descripcion"]
    precio=articulo["precio"]
    print(f"{codigo:<15}{descripcion:<25}{precio}")
