"""Leer el contenido del archivo de texto 'datos.txt' línea a línea."""

#Importamos libreria necesaria
import os

#Ruta absoluta del archivo pyton actual
carpeta=os.path.dirname(__file__)

#Abrimos el documento en cuestion
archivo1=open(os.path.join(carpeta, "datos.txt"), "r")

#Almacenamos la primera linea del documento
linea=archivo1.readline()

#Leemos linea por linea y mostramos resultado
while linea!="":
    print(linea, end="")
    linea=archivo1.readline()

#Liberamos el documento
archivo1.close()



