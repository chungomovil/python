"""Abrir un archivo de texto con el parámetro "r+", imprimir su contenido actual y agregar luego dos líneas al final."""

#Importamos libreria necesaria
import os

#Ruta del script actual
carpeta=os.path.dirname(__file__)

#Abrimos documento en modo lectura y escritura
archivo1=open(os.path.join(carpeta, "datos.txt"), "r+")

#Leemos el documento
contenido=archivo1.read()

#Mostramos su contenido actual
print(40*"*")
print("CONTENIDO ACTUAL")
print(40*"*")
print(contenido)
#Agregamos lineas al texto existente
archivo1.write("Hemos agregado una linea.\n")
archivo1.write("Y escribimos otra que sera la ultima.\n")

#Lo liberamos
archivo1.close()

#Abrimos nuevamente el documento (necesitamos abrirlo ya que no se puede leer nuevamente si no lo cerramos)
archivo2=open(os.path.join(carpeta, "datos.txt"), "r+")

#Leemos el documento
contenido_nuevo=archivo2.read()

#Mostramos su contenido
print(40*"*")
print("CONTENIDO NUEVO")
print(40*"*")
print(contenido_nuevo)

#Liberamos el documento
archivo1.close()


