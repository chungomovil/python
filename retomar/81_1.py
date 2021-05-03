"""El primer programa que implementaremos nos conectaremos con el servidor de MySQL y mostraremos todas las bases de datos existentes (una de esas debería ser bd1)"""

#Importar libreria necesaria para la conexion con la base de datos
import mysql.connector as mysql

#Conectar con la base de datos
conexion=mysql.connect(host="192.168.1.15", user="python", passwd="python")

#Crear el cursor que se encargara de realizar las consultas
cursor1=conexion.cursor()

#Ejecutamos la consulta
cursor1.execute("SHOW DATABASES;")

#Recorremos cada una de las filas de la consulta
for base in cursor1:
    print(base)

#Liberamos la conexion con la base de datos
conexion.close()
