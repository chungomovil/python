"""Convertir los datos recuperados a una lista y mediante un for mostrar los atributos "userID", "id", "title" y "body".
EXTRA: Se ha empleado recursividad para recorrer los diccionarios dentro de diccionarios."""

#Importamos modulos necesarios
from urllib import request
import json

#Funcion Recursiva para recorrer diccionario
def RecorrerDiccionario(diccionario, sep=0):
    #Recorremos el diccionario
    for clave in diccionario:
        #Mostramos las claves
        print(sep*" ", clave, end=": ")
        #Si el valor actual no es un diccionario lo mostramos
        if type(diccionario[clave]) is not dict:
            print(str(diccionario[clave]))
        #Si el valor es un diccionario creamos recursion para recorrerlo
        else:
            #Creamos salto de linea
            print("")
            #Creamos recursion agregando espaciado (3 espacios)
            RecorrerDiccionario(diccionario[clave], sep+3)

#Peticion http
peticion=request.urlopen("https://jsonplaceholder.typicode.com/users")
#Leemos datos y codificados a utf-8
datos=peticion.read().decode("utf-8")
#Generamos un json a partir de los datos anteriores
GenerarJson=json.loads(datos)
#Recorremos la lista para posicionarnos en los distintos diccionarios
for x in range (len(GenerarJson)):
    #Llamamos a la funcion que los recorre
    RecorrerDiccionario(GenerarJson[x])
    #Agregamos separacion entre diccionarios
    print(100*"-")
