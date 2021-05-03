"""Ahora implementaremos un programa que recupere todas las tablas contenidos en una base de datos. Trabajaremos con la base de datos que creamos desde el PHPMyAdmin llamada 'bd1'."""
#Importar libreria necesaria
import mysql.connector as mysql

#Crear conexion con la base de datosa
conexion=mysql.connect(host="192.168.1.15", user="python", passwd="python", database="db1")

#Crear un cursor para las consultas
cursor1=conexion.cursor()

#Ejecutar consulta
cursor1.execute("SHOW TABLES;")

#Recorrer filas de la consulta
for tabla in cursor1:
    print(tabla)

#Cerrar la conexion
conexion.close()


