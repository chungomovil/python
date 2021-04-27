"""Crear un archivo de texto llamado 'datos.txt', almacenar tres líneas de texto. Abrir luego el archivo creado con un editor de texto."""

#Importamos libreria necesaria
import os

#Obtenemos ruta absoluta de este script
carpeta=os.path.dirname(__file__)

#Abrimos o creamos el archivo en modo escritura
archivo1=open(os.path.join(carpeta, "datos.txt"), "w")

#Escribimos en el
archivo1.write("Esto es una frase.\n")
archivo1.write("Y esto es una segunda linea en el documento.\n")
archivo1.write("Pero esto tambies es otra linea y la ultima.\n")

#Lo liberamos
archivo1.close()
