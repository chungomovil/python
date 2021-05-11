"""Cuando queremos crear una base de datos que ya existe se genera un error, podemos primero borrarla y luego ya si crearla sin problemas."""

#Modulo necesario para MySQL
import mysql.connector as mysql

#Introducimos los datos del usuario administrador de la BD
print(5*"*"+"Usuario ADMINISTRADOR de la BD"+5*'*')
usuario=input("Usuario: ")
password=input("Password: ")

#Conectamos con la BD
conexion=mysql.connect(host="192.168.1.15", user=usuario, password=password)

#Creamos el cursor
cursor1=conexion.cursor()

#Borramos la base de datos si existe
cursor1.execute("DROP DATABASE IF EXISTS db2")
print("--> Se ha eliminado la base de datos 'db2'")

#Creamos la base de datos
cursor1.execute("CREATE DATABASE db2")
print("--> Se ha creado la base de datos 'db2'")

#Nos posicionamos en la BD creada
cursor1.execute("USE db2")
print("--> Se ha creado la tabla 'usuarios'")

#Creamos una tabla dentro de ella
cursor1.execute("CREATE TABLE usuarios (nombre varchar(30) PRIMARY KEY, clave varchar(30))")

#Fijamos cambios
conexion.commit()

#Cerramos conexion
conexion.close()


