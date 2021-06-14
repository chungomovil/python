#Libreria necesaria para postgresql
import psycopg2 as postgres

#Creamos la clase
class Consulta:

    #Metodo para conectarse a la BD
    def Abrir(self):
        conexion=postgres.connect(host="192.168.1.200", user="python", password="python", database="db1")
        return conexion

    #Metodo para crear un articulo
    def CrearArticulo(self, descripcion, precio):
        conexion=self.Abrir()
        datos=(descripcion, precio)
        sql="INSERT INTO articulos (descripcion, precio) VALUES (%s, %s)"
        cursor=conexion.cursor()
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()
    
    #Metodo para consultar un articulo
    def ConsultarCodigo(self, codigo):
        conexion=self.Abrir()
        sql="SELECT * FROM articulos WHERE codigo=%s"
        cursor=conexion.cursor()
        cursor.execute(sql, codigo)
        articulo=cursor.fetchone()
        conexion.close()
        return articulo

    #Metodo para listar todos los articulos ordenador por el codigo
    def ListarArticulos(self):
        conexion=self.Abrir()
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM articulos ORDER BY codigo ASC")
        articulos=cursor.fetchall()
        conexion.close()
        return articulos

    #Metodo para borrar un articulo
    def BorrarArticulo(self, codigo):
        conexion=self.Abrir()
        sql="DELETE FROM articulos WHERE codigo=%s"
        cursor=conexion.cursor()
        cursor.execute(sql, codigo)
        conexion.commit()
        conexion.close()

    #Metodo para modificar un articulo
    def ModificarArticulo(self, codigo, descripcion, precio):
        datos=(descripcion, precio, codigo)
        conexion=self.Abrir()
        sql="UPDATE articulos SET descripcion=%s, precio=%s WHERE codigo=%s"
        cursor=conexion.cursor()
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()
