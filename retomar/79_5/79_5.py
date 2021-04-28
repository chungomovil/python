"""Abrir el archivo de texto 'datos.txt' y luego agregar 2 líneas. Imprimir luego el archivo completo."""

#Importamos libreria necesaria
import os

#Ruta del script actual
carpeta=os.path.dirname(__file__)

#Abrimos documento en modo escritura SIN BORRAR CONTENIDO EXISTENTE
archivo1=open(os.path.join(carpeta, "datos.txt"), "a")

#Agregamos texto
archivo1.write("Agregamos una frase al final.\n")
archivo1.write("No se deberian borrar las frases anteriores del documento.\n")
archivo1.write("Pues eso es todo.\n")

#Liberamos documento
archivo1.close()

#Abrimos documento en modo lectura
archivo2=open(os.path.join(carpeta, "datos.txt"), "r")

#Leemos todo el texto
contenido=archivo2.read()

#Mostramos resultado
print(contenido)

#Liberamos documento
archivo2.close()
