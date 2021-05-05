import mysql.connector as mysql

    
conexion=mysql.connect(host="192.168.1.15", user="python", passwd="python", database="db1")


def Insertar(descripcion, precio):
    producto=(descripcion, precio)
    consulta=("INSERT INTO articulos (descripcion, precio) VALUES (%s, %s)")
    cursor1=conexion.cursor()
    cursor1.execute(consulta, producto)
    conexion.commit()
    conexion.close()

def Buscar(codigo):
    consulta=("SELECT * FROM articulos WHERE codigo=%s")
    cursor1=conexion.cursor()
    cursor1.execute(consulta, codigo)
    conexion.close()
    return cursor1.fetchall()


