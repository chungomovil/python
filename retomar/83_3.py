"""
Se deberá crear una nueva base de datos y su respectiva tabla en MySQL.
"""

#Modulo necesario para MySQL
import mysql.connector as mysql

#Introducimos los datos del usuario administrador de la BD
print(5*"*"+"Usuario ADMINISTRADOR de la BD"+5*'*')
usuario=input("Usuario: ")
password=input("Password: ")

#Creamos la conexion con la BD
conexion=mysql.connect(host="192.168.1.15", user=usuario, passwd=password, database="db1")

#Creamos el cursor
cursor1=conexion.cursor()

#Creamos la base de datos
cursor1.execute("CREATE DATABASE db2")
print("--> Se ha creado la base de datod 'db2'")

#Nos posicionamos en la base de datos creada
cursor1.execute("USE db2")

#Creamos la tabla
cursor1.execute("CREATE TABLE usuarios (nombre varchar(30) primary key, clave varchar(30))")
print("--> Se ha creado la tabla 'usuarios'")

#Fijamos los cambios
conexion.commit()

#Cerramos conexion
cursor1.close()


