"""Las otras dos actividades fundamentales que podemos hacer con una tabla es borrar filas y modificar datos.
Desarrollaremos un pequeño programa que borre el artículo cuyo código sea el 1 y modifique el precio del artículo cuyo código sea 5."""

#Importamos el modulo necesario para trabajar con postgres
import psycopg2 as postgres

#Creamos la conexion con la base de datos
conexion=postgres.connect(host="192.168.1.200", user="python", password="python", database="db1")

#Creamos el cursor
cursor1=conexion.cursor()

#Creamos las consultas
consulta_mod="UPDATE articulos SET precio=%s WHERE codigo=%s"
consulta_del="DELETE FROM articulos WHERE codigo=%s"

#Ejecutamos las consultas e informamos al usuario
cursor1.execute(consulta_mod, (2.40, 5))
print("--> El articulo se ha modificado correctamente.")
cursor1.execute(consulta_del, (1, ))
print("--> El articulo se ha eliminado correctamente.")

#Fijamos cambios
conexion.commit()

#Ejecutamos una consulta para visualizar los cambios
cursor1.execute("SELECT * from articulos")

#Extramos datos del cursor y los almacenamos en una lista
articulos=cursor1.fetchall()

#Cerramos la conexion
conexion.close()

#Creamos la tabla para los resultados obtenidos y los recorremos
print("CODIGO"+10*" "+"DESCRIPCION"+10*" "+"PRECIO")
for codigo, descripcion, precio in articulos:
    print(f"{codigo:<16}{descripcion:<21}{precio}")
