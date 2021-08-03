#Importamos los modulos necesarios para crear el ".exe"
#Recordar que se deben importar todos los que se importaron en el programa original
from distutils.core import setup
import py2exe
import proyecto_estimaciones
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
import os
import sys

#Obtenemos la ruta del archivo actual
archivo=os.path.dirname(__file__)
#Obtenemos la ruta de la carpeta de las imagenes
imagenes=str(archivo)+"\\images"

#Creamos una lista vacio donde se insertaran las rutas de las imagenes
my_data_files=[]

#Recorremos el directorio de las imagenes
for archivo in os.listdir(imagenes):
    #Creamos una tupla con la ruta de la imagen (entre comillas ira la carpeta y entre corchetes su ruta)
    imagen=("images", [os.path.join(imagenes, archivo)])
    #La agregamos a la lista de las imagenes
    my_data_files.append(imagen)

#Establecemos los parametros de la creacion del ".exe"
setup(
    #Incluimos la carpeta de las imagenes
    data_files=my_data_files,
    #Indicamos que el programa se ejecutara en una ventana y no en consola (porque tiene interfaz visual)
    windows=["proyecto_estimaciones.py"],
    #Parametros adicionales en la creacion del ".exe" (con estos reducimos los archivos que tendra la carpeta del programa)
    options = {"py2exe": {"compressed": 1, "optimize": 2,"dll_excludes": "w9xpopen.exe", "ascii": 0, "bundle_files": 1}},
    zipfile = None)
