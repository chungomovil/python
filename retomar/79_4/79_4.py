"""Mediante el método 'readlines' podemos recuperar cada una de las líneas del archivo de texto y almacenarlas en una lista."""

#Importamos libreria necesaria
import os

#Ruta del script actual
carpeta=os.path.dirname(__file__)

#Abrir documento de datos
archivo1=open(os.path.join(carpeta, "datos.txt"), "r")

#Almacenar lineas de texto en una lista
lista_texto=archivo1.readlines()

#Imprimir y recorrer lista
print("El archivo tiene", len(lista_texto), "lineas")
print(20*"*")
print("CONTENIDO")
print(20*"*")
for linea in lista_texto:
    print(linea)

#Liberar documento
archivo1.close()

