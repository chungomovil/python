"""
Implementaremos un programa que solicite el ingreso de un precio y luego nos muestre la descripción de todos los artículos con un precio inferior al ingresado.
"""

#Importamos librerias necesarias
import os
import sqlite3

#Ruta del archivo actual de python
ruta=os.path.dirname(__file__)

#Creamos la conexion
conexion=sqlite3.connect(os.path.join(ruta, "db1.db"))

#Algoritmo a procesar
try:
    #Introducimos precio
    precio=float(input("PRECIO LIMITE: "))
    #Realizamos la consulta con el precio
    cursor=conexion.execute("SELECT descripcion, precio FROM articulos WHERE precio<?", (precio, ))
    #Retornamos todas las filas de la consulta
    articulos=cursor.fetchall()
    #Filtramos si el resultado ha sido nulo
    if len(articulos)>0:
        for descripcion, precio in articulos:
            print("\n",15*"*",sep="")
            print("Descripcion:", descripcion)
            print("Precio:", precio)
            print(15*"*")
    else:
        print("No existen articulos con un precio inferior al introducido.")

#Procesamos la excepcion en caso de que se introduzca una string
except ValueError:
    print("Solo se admiten digitos.")

#Algoritmo incondicional
finally:
    #Cerramos la conexion con la base de datos
    conexion.close()
    print("Se ha cerrado la conexion con la base de datos.")

