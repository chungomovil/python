"""Ahora implementaremos un programa que recupere todas las tablas contenidos en una base de datos. Trabajaremos con la base de datos que creamos desde el PHPMyAdmin llamada 'bd1'."""

import mysql.connector as mysql

conexion=mysql.connect(host="192.168.1.15", user="python", passwd="python", database="db1")
cursor1=conexion.cursor()
cursor1.execute("SHOW TABLES;")
for tabla in cursor1:
    print(tabla)
conexion.close()


