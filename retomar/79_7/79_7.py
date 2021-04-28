"""Crear un archivo de texto llamado 'datos.txt' con una codificación utf-8, almacenar tres líneas de texto. Abrir luego el archivo creado con el editor VS Code."""

#Importamos libreria necesaria
import os

#Ruta del script actual
carpeta=os.path.dirname(__file__)

#Abrimos el archivo en modo sobreescritura y codificacion utf-8 para las tildes y caracteres especiales
archivo1=open(os.path.join(carpeta, "datos.txt"), "w", encoding="UTF-8")

#Escribimos en el archivo
archivo1.write("Esta palabra esdrújula, por lo que lleva tilde.\n")
archivo1.write("Esta también debería mostrar una tilde justo AQUÍ.\n")

#Liberamos el archivo
archivo1.close()

#Abrimos el archivo en modo lectura y codificacion utf-8 para las tildes y caracteres especiales
archivo2=open(os.path.join(carpeta, "datos.txt"), "r", encoding="UTF-8")

#Leemos contenido
contenido=archivo2.read()

#Mostramos contenido
print(contenido)



