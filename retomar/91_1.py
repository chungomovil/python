"""Recorrer un árbol de directorios en forma recursiva. Mostrar de cada directorios los archivos y directorios, luego descender a cada directorio y hacer la misma actividad.
(EXTRA) Formateamos la cadena de caracteres para incluir una barra al final de la ruta.
(EXTRA) Creamos identacion de arbol de archivos gracias a la recursividad."""

#Importamos libreria necesaria
import os

#(EXTRA) Funcion incluir barra al final de la ruta en caso de no haberlas
def FormatoRuta(ruta):
    longitud=len(ruta)-1
    if ruta[longitud]!="\\":
        ruta+="\\"
    return ruta

#Funcion recursiva para recorrer carpetas y mostrar sus archivos
def Directorios(ruta, nivel):
    #Obtenemos ubicacion introducida y la formateamos
    ubicacion=FormatoRuta(ruta)
    #Almacenamos en una lista el contenido de dicha carpeta
    carpeta=os.listdir(ubicacion)
    #Recorremos el contenido de la lista
    for elemento in carpeta:
        #Si es un archivo
        if os.path.isfile(ubicacion+elemento):
            #(EXTRA) Creamos identacion en caso de haberla (nos favorecemos de la recursividad para ello)
            print(nivel*4*" ", end="")
            #Formateamos la salida de la informacion
            print(f"{'[ARCHIVO]':<12}{ubicacion+elemento}")
        #Si es una carpeta
        if os.path.isdir(ubicacion+elemento):
            #(EXTRA) Creamos nuevamente identacion
            print(nivel*4*" ",end="")
            #Formateamos la salida de la informacion
            print(f"{'[CARPETA]':<12}{ubicacion+elemento}")
            #Creamos recursion para los archivos de dicha carpeta
            Directorios(ubicacion+elemento, nivel+1)

#Introduccion de ruta por teclado
ruta=input("Ubicacion de la carpeta: ")
#Variable que hace referencia al nivel de la carpeta y subcarpeta
nivel=0
#Llamamos a la funcion con los parametros
Directorios(ruta, nivel)

