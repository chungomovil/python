"""Cuando insertamos una fila en una tabla que contiene un campo que se auto incrementa podemos recuperar dicho valor en el mismo momento que efectuamos la inserción."""

#Importamos libreria necesaria
import mysql.connector as mysql

#Creamos la conexion con la BD
conexion=mysql.connect(host="192.168.1.15", user="python", passwd="python", database="db1")

#Creamos el cursor
cursor1=conexion.cursor()

#Ejecutamos la consulta
cursor1.execute("INSERT INTO articulos (descripcion, precio) VALUES ('vinagre', 2.57)")

#Aplicamos los cambios
conexion.commit()

#Imprimimos los mensajes en caso de haber ejecutado la consulta correctamente
if cursor1!="":
    print("La operacion se ha realizado correctamente")
    #Imprimimos el id de la ultima consulta realizada
    print("Numero de operacion:", cursor1.lastrowid)
#Imprimimos el mensaje de error en caso de no realizar la consulta correctamente.
else:
    print("La operacion no se ha podido realizar.")

#Cerramos conexion
conexion.close()


