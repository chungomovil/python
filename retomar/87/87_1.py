"""En principio no se requiere tener más que Python instalado para poder trabajar con SQLite. Podemos desde nuestra propia aplicación crear la base de datos y sus tablas."""

#Importamos modulos necesarios
import sqlite3
import os

#Obtenemos ruta del archivo actual de python
ruta=os.path.dirname(__file__)

#Creamos la base de datos en la ruta
conexion=sqlite3.connect(os.path.join(ruta,"db1.db"))

#Algoritmo a procesar
try:
    #Ejecutamos la consulta
    conexion.execute("CREATE TABLE articulos (codigo INTEGER PRIMARY KEY AUTOINCREMENT, descripcion TEXT, precio REAL)") #integer es entero, text es texto y real es flotante
    #Fijamos cambios
    conexion.commit()
    print("Tablas creadas correctamente.")
#Procesamos la excepcion en caso que la haya
except sqlite3.OperationalError:
    print("La tabla ya existe.")
#Accion que se realizara incondicionalmente
finally:
    #Cerramos la conexion con la base de datos
    conexion.close()
    print("Se ha cerrado la conexion con la base de datos.")

