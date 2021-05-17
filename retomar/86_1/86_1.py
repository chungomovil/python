"""Almacenar una serie de string en un archivo de texto. Tratar de llamar al método 'write' pasando un entero, mostrar mensaje de error en lugar de cerrar por la excepcion.
Finalmente cerrar el programa indiferentemente de que se produzcan excepciones."""

#Importamos libreria necesaria
import os

#Obtenemos ruta absoluta del archivo python
ruta=os.path.dirname(__file__)

#Algoritmo a procesar
try:
    #Abrimos el documento (con la ruta absoluta del sistema) en modo lectura y codificado para caracteres especiales
    archivo1=open(os.path.join(ruta, "texto.txt"), "w", encoding="utf-8")
    #Escribimo en el archivo
    archivo1.write("Esto es una línea.\n")
    archivo1.write("Esta será la segunda.\n")
    archivo1.write("Añadimos otra frase aquí para ver si todo esta OK.\n")
    #Agregamos el ERROR
    archivo1.write(123)

#Creamos el mensaje para la excepcion
except TypeError:
    print("La entrada de datos no puede estar en formato 'INT'.")

#Fragmento que se ejecutara se produzca la excepcion o no
finally:
    archivo1.close()
    print("Se ha cerrado el archivo.")


