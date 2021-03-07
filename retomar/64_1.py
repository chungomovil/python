"""
Solicitar el ingreso del nombre de una persona y seleccionar de un control Combobox un país. Al presionar un botón mostrar en la barra de la ventana el nombre ingresado y el país seleccionado."""

import tkinter as tk
from tkinter import ttk
import sys

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("PERSONA Y PAIS")
        self.etiqueta1=ttk.Label(self.ventana, text="Nombre:")
        self.etiqueta1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.persona=ttk.Entry(self.ventana, width=20, textvariable=self.dato1)
        self.persona.grid(column=1, row=0)
        self.etiqueta2=ttk.Label(self.ventana, text="Pais:")
        self.etiqueta2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.paises=("Espania","Alemania","Cuba","Marruecos","China","Japon","Noruega","Suecia","Estados Unidos","Colombia","Ecuador") #Listar valores del combobox
        self.pais=ttk.Combobox(self.ventana, width=20, value=self.paises, textvariable=self.dato2)
        self.pais.grid(column=1, row=1)
        self.boton1=ttk.Button(self.ventana, text="Validar", command=self.Validar)
        self.boton1.grid(column=0, row=2)
        self.boton2=ttk.Button(self.ventana, text="Salir", command=self.Salir)
        self.boton2.grid(column=0, row=3)
        self.ventana.minsize(400, 200)
        self.ventana.mainloop()

    #Funcion para obtener datos del combobox y mostrarlos en la barra de la ventana
    def Validar(self):
        nombre=self.dato1.get()
        pais=self.dato2.get()
        self.ventana.title("Nombre: "+nombre+" Pais: "+pais)
    
    def Salir(self):
        sys.exit(0)

iniciar=Aplicacion()
