"""Crear un programa en Python que envie el codigo del producto ingresado por teclado al archivo PHP que lo devolverá en JSON.
Luego codificar el resultado a JSON con Python y mostrarlo en pantalla."""

#Importamos librerias necesarias para conectarse a internet y para codificar a JSON
from urllib import request
import json

#Algoritmo a intentar
try:
    #Introducimos el codigo por teclado
    codigo=int(input("Codigo de articulo: "))
#Procesamos excepcion
except ValueError:
    codigo=False

#Si devuelve el digito del codigo (es decir, NO hubo problemas)
if codigo!=False:
    #Hacemos la peticion al archivo PHP pasando como parametro el codigo
    peticion=request.urlopen(f"http://web/retornararticulo.php?codigo={codigo}")
    #Leemos los datos
    datos=peticion.read()
    #Codificamos
    datosutf8=datos.decode("utf-8")
    #Transformamos los datos a json
    datosjson=json.loads(datosutf8)
    #Si la lista comiente algo
    if len(datosjson)>0:
        print(f"{'CODIGO':<15}{'DESCRIPCION':<25}{'PRECIO'}")
        #Mostramos el resultado(OJO: es una lista que posee dentro un diccionario)
        print(f"{datosjson[0]['codigo']:<15}{datosjson[0]['descripcion']:<25}{datosjson[0]['precio']}")
    #Si la lista esta vacia
    else:
        print("El articulo solicitado no existe.")
#Si devuelve 'False' (es decir, hubo una excepcion)
else:
    print("Codigo incorrecto.")
