"""Leer el contenido del archivo de texto 'datos.txt'."""

#Importamos libreria necesaria
import os

#Obtenemos ruta absoluta del script actual
carpeta=os.path.dirname(__file__)

#Abrimos el documento en cuestion en modo lectura
archivo1=open(os.path.join(carpeta, "datos.txt"), "r")

#Copiamos el contenido leido a una variable
contenido=archivo1.read()

#Mostramos el contenido leido
print(contenido)

#Liberamos el documento
archivo1.close()
