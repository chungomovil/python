"""Las otras dos actividades fundamentales que podemos hacer con una tabla es borrar filas y modificar datos.
Desarrollaremos un pequeño programa que borre el artículo cuyo código sea el 1 y modifique el precio del artículo cuyo código sea 3."""

#Importamos el modulo necesario
import mysql.connector as mysql

#Creamos la conexion con la base de datos
conexion=mysql.connect(host="192.168.1.15", user="python", passwd="python", database="db1")

#Creamos el cursor para las consultas
cursor1=conexion.cursor()

#Borramos una fila
cursor1.execute("DELETE FROM articulos WHERE codigo='1';")

#Editamos una fila
cursor1.execute("UPDATE articulos SET precio='2.05' WHERE codigo='3';")

#Aplicamos los cambios
conexion.commit()

#Recorremos la tabla para ver los cambios
cursor1.execute("SELECT * FROM articulos;")
for item in cursor1:
    print(item)

#Cerramos la conexion con la base de datos
conexion.close()
