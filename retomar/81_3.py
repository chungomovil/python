"""Ahora implementaremos un programa que inserte un par de filas en la tabla 'articulos'.
(EXTRA) Mostrar los cambios realizados."""

#Importamos libreria necesaria
import mysql.connector as mysql

#Conectamos con la base de datos
conexion=mysql.connect(host="192.168.1.15", user="python", passwd="python", database="db1")

#Creamos el puntero para las consultas
cursor1=conexion.cursor()

#Creamos una variable con la sintaxis de la consulta de insercion de valores
consulta="INSERT INTO articulos (descripcion, precio) VALUES (%s, %s);"

#Creamos variables con los valores a agregar
valores1=("Manzana","0.80")
valores2=("Pitaya", "5")
valores3=("Tomate", "1.55")

#Ejecutamos las consultas
cursor1.execute(consulta, valores1)
cursor1.execute(consulta, valores2)
cursor1.execute(consulta, valores3)

#Hacemos los cambios efectivos (DE LO CONTRARIO NO SE AGREGARAN DEFINITIVAMENTE)
conexion.commit()

# (EXTRA) Recorremos la tabla articulos para comprobar las inseciones
cursor1.execute("SELECT * FROM articulos;")
for item in cursor1:
    print(item)

#Cerramos la conexion con la base de datos
conexion.close()



