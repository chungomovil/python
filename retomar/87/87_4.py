"""Implementaremos un programa que solicite el ingreso del código de un producto y luego nos muestre su descripción y precio."""

#Importamos librerias necesarias
import os
import sqlite3

#Ruta del archivo python actual
ruta=os.path.dirname(__file__)

#Creamos la conexion
conexion=sqlite3.connect(os.path.join(ruta, "db1.db"))


#Algoritmo a procesar
try:
    #Introduccion del codigo del articulo
    codigo=int(input("CODIGO DE PRODUCTO: "))
    #Consulta por codigo de articulo
    cursor=conexion.execute("SELECT descripcion, precio FROM articulos WHERE codigo=?", (codigo, )) #OJO: Recordar siempre convertir a tupla el parametro de entrada
    #Retornamos los datos de la fila
    fila=cursor.fetchone()
    #Si no esta vacio (si la consulta no devuelve un articulo)
    if fila!=None:
        print(fila)
    #Si esta vacio
    else:
        print("Articulo no encontrado.")

#Controlamos la excepcion de error al introducir string en vez de enteros
except ValueError:
    print("Solo se aceptan valores numericos enteros.")

#Accion incondicional
finally:
    #Cerramos la conexion con la base de datos
    conexion.close()
    print("Se ha cerrado la conexion con la base de datos.")

