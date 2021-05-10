"""La clase cursor a parte del método 'execute' cuenta con otro método llamado 'executemany' que tiene el objetivo de insertar múltiples filas de una tabla."""

#Importamos libreria necesaria
import mysql.connector as mysql

#Creamos la conexion con la BD
conexion=mysql.connect(host="192.168.1.15", user="python", passwd="python", database="db1")

#Creamos la consulta
consulta="INSERT INTO articulos (descripcion, precio) VALUES (%s, %s)"

#Creamos los datos que se ingresaran
datos=[("naranja", 0.88),
        ("aceite", 2.19),
        ("jamon", 3.70),
        ("gulas", 6.60),
        ("chicles", 1)]

#Creamos el cursor
cursor1=conexion.cursor()

#Ejecutamos la consulta (OJO: Se usa 'executemany' para ingresar varias filas simultaneamente)
cursor1.executemany(consulta, datos)

#Fijamos los cambios
conexion.commit()

#Cerramos conexion
conexion.close()


