#Importamos libreria necesaria para la conexion con mysql
import mysql.connector as mysql

#Funcion para conectar a la BD
def Conectar():
    conexion=mysql.connect(host="192.168.1.15", user="python", passwd="python", database="db1")
    return conexion

#Funcion para insertar nuevos articulos en la BD
def Insertar(descripcion, precio):
    #Conectamos con la BD
    conexion=Conectar()
    #Convertimos en tupla los datos recibidos
    producto=(descripcion, precio)
    #Creamos la consulta
    consulta="INSERT INTO articulos (descripcion, precio) VALUES (%s, %s)"
    #Creamos el cursor
    cursor1=conexion.cursor()
    #Ejecutamos la consulta con los valores recibidos
    cursor1.execute(consulta, producto)
    #Fijamos los cambios en la BD
    conexion.commit()
    #Cerramos conexion
    conexion.close()

#Funcion para buscar articulo por codigo en la BD
def Buscar(codigo):
    #Conectamos con la BD
    conexion=Conectar()
    #Creamos la consulta
    consulta="SELECT * FROM articulos WHERE codigo=%s"
    #Creamos el cursor
    cursor1=conexion.cursor()
    #Ejecutamos la consulta con el codigo recibido (OJO: Recordar que lo recibimos en una tupla)
    cursor1.execute(consulta, codigo)
    #Cerramos conexion
    conexion.close()
    #Retornamos todos los campos de la consulta
    return cursor1.fetchall()

#Funcion para mostrar todos los articulos de la BD
def Totalidad():
    #Conectamos con la BD
    conexion=Conectar()
    #Creamos cursor
    cursor1=conexion.cursor()
    #Ejecutamos la consulta
    cursor1.execute("SELECT * FROM articulos")
    #Cerramos conexion
    conexion.close()
    #Retornamos todos los campos de la consulta
    return cursor1.fetchall()

#Funcion para borrar los articulos de la BD
def Borrar(codigo):
    #Buscamos y almacenamos en una variable la informacion del articulo antes de que se elimine
    articulo=Buscar(codigo)
    #Conectamos con la BD
    conexion=Conectar()
    #Creamos la consulta de eliminacion
    consulta="DELETE FROM articulos WHERE codigo=%s"
    #Creamos el cursor
    cursor1=conexion.cursor()
    #Ejecutamos la consulta
    cursor1.execute(consulta, codigo)
    #Fijamos los cambios
    conexion.commit()
    #Cerramos conexion
    conexion.close()
    #Retornamos informacion del articulo eliminado
    return articulo

#Funcion para modificar articulo de la BD
def Modificar(codigo, descripcion, precio):
    #Conectamos con la BD
    conexion=Conectar()
    #Creamos el cursor
    cursor1=conexion.cursor()
    #Controlamos si no esta vacio el campo
    if descripcion!="":
        #Creamos la consulta de modificacion
        consulta="UPDATE articulos SET descripcion=%s WHERE codigo=%s"
        #Ejecutamos la consulta
        cursor1.execute(consulta, (descripcion, codigo))
    if precio!="":
        consulta="UPDATE articulos SET precio=%s WHERE codigo=%s"
        cursor1.execute(consulta,(precio, codigo))
    #Fijamos los cambios
    conexion.commit()
    #Cerramos la conexion
    conexion.close()
    #Buscamos y almacenamos los datos del articulo modificado
    articulo=Buscar((codigo, ))
    #Retornamos los datos del articulo modificado
    return articulo