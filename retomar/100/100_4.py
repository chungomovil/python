"""Convertir los datos recuperados a una lista y mediante un for mostrar los atributos "userID", "id", "title" y "body"."""

#Llamos a los modulos necesarios
from urllib import request
import json

#Realizamos la peticion http
peticion=request.urlopen("https://jsonplaceholder.typicode.com/posts")

#Leemos datos de la web y codificidamos a utf-8
datos=peticion.read().decode("utf-8")

#Transformamos los datos a formato Json
GenerarJson=json.loads(datos)

#Recorremos la lista
for elemento in GenerarJson:
    #Descomprimos cada diccionario de la lista
    idusuario=elemento['userId']
    identrada=elemento['id']
    titulo=elemento['title']
    cuerpo=elemento['body']
    
    #Mostramos resultado
    print(f"Usuario ID: {idusuario}\nEntrada ID: {identrada}\nTitulo: {titulo}\nNoticia: {cuerpo}\n"+100*"-")




