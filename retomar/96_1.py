"""El primer programa que implementaremos nos conectaremos con el servidor de PostgreSQL e insertaremos un par de filas en la tabla 'articulos' que creamos desde el programa 'pgAdmin'."""

#Importamos el modulo necesario para establecer conexion con postgresql
import psycopg2 as postgres

#Creamos la conexion con la base de datos
conexion=postgres.connect(host="192.168.1.200", user="python", password="python", database="db1")

#Creamos la consulta de insercion
consulta="INSERT INTO articulos (descripcion, precio) VALUES (%s, %s)"

#Creamos el cursor
cursor1=conexion.cursor()

#Ejecutamos consulta con los datos
cursor1.execute(consulta, ('lechuga', 1.05))
cursor1.execute(consulta, ('apio', 1))
cursor1.execute(consulta, ('chocolate', 3.1))

#Fijamos los cambios en la base de datos
conexion.commit()

#Informamos al usuario
print("--> Datos almacenados correctamente.")

#Cerramos conexion con la base de datos
conexion.close()
