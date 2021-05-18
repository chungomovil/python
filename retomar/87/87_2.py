"""Ahora implementaremos un programa que inserte un par de filas en la tabla 'articulos' de la base de datos 'bd1' que acabamos de crear con el programa anterior."""

#Importamos librerias necesarias
import sqlite3
import os

#Ruta del archivo actual de python
ruta=os.path.dirname(__file__)

#Creamos la conexion con la base de datos
conexion=sqlite3.connect(os.path.join(ruta, "db1.db"))

#Algoritmo a procesar
try:
    #Ejecutamos las consultas de inserción de filas
    conexion.execute("INSERT INTO articulos (descripcion, precio) VALUES (?, ?)", ("tomate", 1.50))
    conexion.execute("INSERT INTO articulos (descripcion, precio) VALUES (?, ?)", ("chocolate", 3))
    conexion.execute("INSERT INTO articulos (descripcion, precio) VALUES (?, ?)", ("pera", 0.89))
    #Fijamos cambios
    conexion.commit()
    print("Se han agregado los campos correctamente.")
#Procesamos la excepcion si se produce
except sqlite3.OperationalError:
    print("Error en la consulta.")
#Accion incondicional
finally:
    #Cerramos conexion con la base de datos
    conexion.close()
    print("Se ha cerrado la conexion.")

