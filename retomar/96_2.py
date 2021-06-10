"""Implementaremos un programa que solicite ejecutar un 'select' en la tabla 'articulos' de la base de datos 'bd1' y nos retorne todas sus filas."""

#Modulo necesario para postgres
import psycopg2 as postgres

#Establecemos conexion
conexion=postgres.connect(host="192.168.1.200", user="python", password="python", database="db1")

#Creamos el cursor
cursor1=conexion.cursor()

#Ejecutamos la consulta
cursor1.execute("SELECT * FROM articulos")

#Capturamos todos los elementos de la consulta anterior
#Este paso se puede omitir y extraer los datos directamente del cursor,
#pero asi podemos cerrar antes la conexion y seguir utilizando los datos de la consulta
articulos=cursor1.fetchall()

#Cerramos la conexion
conexion.close()

#Encabezado de tabla
print("CODIGO"+10*" "+"DESCRIPCION"+10*" "+"PRECIO")

#Recorremos el resultado de la consulta anterior y los agregamos a la tabla
for codigo, descripcion, precio in articulos:
    print(f"{codigo:<16}{descripcion:<21}{precio}")
