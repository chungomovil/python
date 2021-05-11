"""No se puede crear una tabla con el mismo nombre de una existente, en esos casos debemos borrar la actual y crear una nueva."""

#Modulo necesario para MySQL
import mysql.connector as mysql

#Introducimos los datos del usuario administrador de la BD
print(5*"*"+"Usuario ADMINISTRADOR de la BD"+5*'*')
usuario=input("Usuario: ")
password=input("Password: ")

#Creamos la conexion con la BD
conexion=mysql.connect(host="192.168.1.15", user=usuario, passwd=password, database="db2")

#Creamos el cursor
cursor1=conexion.cursor()

#Eliminamos la tabla 
cursor1.execute("DROP TABLE IF EXISTS usuarios")
print("--> Se ha eliminado la tabla 'usuarios'")

#Creamos nuevamente la tabla
cursor1.execute("CREATE TABLE usuarios (nombre varchar(30) PRIMARY KEY, clave varchar(30))")
print("--> Se ha creado la tabla 'usuarios'")

#Fijamos los cambios
conexion.commit()

#Cerramos la conexion
conexion.close()

