#Importar librerias necesarias
import tkinter as tk
from tkinter import ttk
import os
import sys
import random

#Capturar ruta absoluta del archivo python actual
carpeta=os.path.dirname(__file__)

#Creamos la clase
class Aplicacion:

    #Creamos el metodo constructor
    def __init__(self):
        #Creamos la ventana
        self.ventana=tk.Tk()
        self.ventana.title("Mostrar imagen aleatoria con tkinter")
        #(EXTRA) Creamos el menu para salir
        menubar=tk.Menu(self.ventana)
        self.ventana.configure(menu=menubar)
        opciones1=tk.Menu(menubar, tearoff=0)
        opciones1.add_command(label="SALIR", command=self.Salir)
        menubar.add_cascade(label="Opciones", menu=opciones1)
        #Creamos el labelframe para la opcion de mezclar
        self.labelframe1=tk.LabelFrame(self.ventana, text="OPCIONES")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10, sticky="we")
        #Importamos el contenido del labelframe1
        self.Contenido()
        #Creamos el lienzo
        self.lienzo1=tk.Canvas(self.ventana, width=800, height=600, background="black")
        self.lienzo1.grid(column=0, row=1)
        #Parametros de la ventana
        self.ventana.resizable(0, 0)
        self.ventana.mainloop()

    #Metodo con el boton de mezclar
    def Contenido(self):
        self.boton1=ttk.Button(self.labelframe1, width=20, text="MEZCLAR", command=self.Mezclar)
        self.boton1.grid(column=0, row=0, padx=300, pady=10)

    #Metodo para mezclar
    def Mezclar(self):
        numero=random.randint(1, 3)
        self.MostrarCarta(numero)
    
    #Metodo para mostrar la carta segun el numero de la mezcla
    def MostrarCarta(self, num):
        #Recordar limpiar el lienzo para que no se superpongan las imagenes una sobre otra
        self.lienzo1.delete(tk.ALL)
        self.imagen=tk.PhotoImage(file=os.path.join(carpeta, "carta"+str(num)+".png")) #Agregamos el numero en formato de letra al nombre del archivo
        self.lienzo1.create_image(300, 150, image=self.imagen, anchor="nw")

    #Metodo para salir
    def Salir(self):
        sys.exit(0)

#Bloque principal y declaracion de objeto
iniciar=Aplicacion()
