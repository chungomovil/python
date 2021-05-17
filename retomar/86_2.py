"""Conectarse a una base de datos de MySQL y ejecutar un comando SQL incorrecto."""

#importamos modulo necesario
import mysql.connector as mysql

#Creamos la conexion con la base de datos
conexion=mysql.connect(host="192.168.1.15", user="python", passwd="python")

#Algoritmo a procesar
try:
    #Creamos el cursor
    cursor1=conexion.cursor()
    #Ejecutamos la consulta con el ERROR
    cursor1.execute("SHOW DATABASESSSSSS")

#Creamos el mensaje para la excepcion, debemos especificar el modulo, ya que el modulo importa sus propias excepciones
except mysql.errors.ProgrammingError:
    print("Fallo en la sintaxis de la consulta.")

#Fragmento que se ejecutara incondicionalmente
finally:
    conexion.close()
    print("Se ha cerrado la conexion con la base de datos.")



