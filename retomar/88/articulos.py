#Importamos modulos necesarios
import sqlite3
import os

#Creamos la clase
class BaseDatos:
    
    #Metodo para abrir la conexion
    def Abrir(self):
        #Obtenemos ruta del archivo actual de python
        ruta=os.path.dirname(__file__)
        #Creamos la conexion
        conexion=sqlite3.connect(os.path.join(ruta, "db1.db"))
        #Retornamos la conexion
        return conexion

    #Metodo para insertar un articulo nuevo
    def CrearArticulo(self, descripcion, precio):
        #Abrimos conexion
        conexion=self.Abrir()
        #Insertamos valores nuevos
        conexion.execute("INSERT INTO articulos (descripcion, precio) VALUES (?, ?)", (descripcion, precio))
        #Fijamos cambios
        conexion.commit()
        #Cerramos conexion
        conexion.close()
        
    #Metodo para consultar por codigo
    def ConsultarCodigo(self, codigo):
        #Abrimos conexion
        conexion=self.Abrir()
        #Buscamos por el codigo
        cursor=conexion.execute("SELECT descripcion, precio FROM articulos WHERE codigo=?", (codigo))
        #Capturamos la fila resultane
        articulo=cursor.fetchone()
        #Cerramos la conexion
        conexion.close()
        #Retornamos la fila
        return articulo
    
    #Metodo para listar todos los articulos
    def ArticulosTotal(self):
        #Abrimos conexion
        conexion=self.Abrir()
        #Listamos todos los articulos
        cursor=conexion.execute("SELECT * FROM articulos")
        #Capturamos todos los articulos
        articulo=cursor.fetchall()
        #Cerramos conexion
        conexion.close()
        #Retornamos los articulos
        return articulo


