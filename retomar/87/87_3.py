"""Implementaremos un programa que solicite ejecutar un 'select' en la tabla 'articulos' y nos retorne todas sus filas."""

#Importamos librerias necesarias
import sqlite3
import os

#Ruta archivo python actual
ruta=os.path.dirname(__file__)

#Conexion con la base de datos
conexion=sqlite3.connect(os.path.join(ruta, "db1.db"))

#Creamos el cursor para almacenar resultado de la consulta
cursor1=conexion.execute("SELECT * FROM articulos")

#Recorremos las filas que ha retornado e imprimimos
for articulo in cursor1:
    print(articulo)

#Cerramos la conexion con la base de datos
conexion.close()

