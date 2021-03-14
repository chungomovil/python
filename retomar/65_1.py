"""
Mediante dos controles de tipo Entry permitir el ingreso de dos números. Crear un menú que contenga una opción que cambie el tamaño de la ventana con los valores ingresados por teclado. Finalmente disponer otra opción que finalice el programa
"""

import tkinter as tk
from tkinter import ttk
import sys

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Medidas y colores")
        #CREACION DEL MENU
        menubar1=tk.Menu(self.ventana)
        self.ventana.configure(menu=menubar1)
        #CREACION DE LAS OPCIONES DEL MENU
        opciones1=tk.Menu(menubar1, tearoff=0) # Tearoff se emplea para que los menus no se puedan hacer ventanas flotantes
        opciones1.add_command(label="Rojo", command=self.C_Rojo)
        opciones1.add_command(label="Verde", command=self.C_Verde)
        opciones1.add_command(label="Blanco", command=self.C_Blanco)
        menubar1.add_cascade(label="Fondo", menu=opciones1)
        opciones2=tk.Menu(menubar1, tearoff=0)
        opciones2.add_command(label="800x600", command=self.VentanaPeque)
        opciones2.add_command(label="1200x800", command=self.VentanaMedia)
        opciones2.add_command(label="1400x900", command=self.VentanaGrande)
        opciones2.add_separator()
        menubar1.add_cascade(label="Medidas", menu=opciones2)
        #CREACION DE UN SUBMENU
        subopciones1=tk.Menu(menubar1, tearoff=0)
        subopciones1.add_command(label="Personalizada", command=self.VentanaCustom)
        opciones2.add_cascade(label="Otros", menu=subopciones1)
        opciones3=tk.Menu(menubar1, tearoff=0)
        opciones3.add_command(label="Salir", command=self.Salir)
        menubar1.add_cascade(label="Opciones", menu=opciones3)
        self.etiqueta1=ttk.Label(self.ventana, text="Medidas personalizadas", foreground="red")
        self.etiqueta1.grid(column=0, row=0)
        self.etiqueta2=ttk.Label(self.ventana, text="Ancho")
        self.etiqueta2.grid(column=0, row=1)
        self.etiqueta3=ttk.Label(self.ventana, text="Alto")
        self.etiqueta3.grid(column=1, row=1)
        self.dato1=tk.StringVar()
        self.dato2=tk.StringVar()
        self.teclado1=ttk.Entry(self.ventana, width=20, textvariable=self.dato1)
        self.teclado1.grid(column=0, row=2)
        self.teclado2=ttk.Entry(self.ventana, width=20, textvariable=self.dato2)
        self.teclado2.grid(column=1, row=2)
        self.ventana.minsize(300, 200)
        self.ventana.mainloop()

    def C_Rojo(self):
        self.ventana.configure(background="red")
    
    def C_Verde(self):
        self.ventana.configure(background="green")
    
    def C_Blanco(self):
        self.ventana.configure(background="white")

    def VentanaPeque(self):
        self.ventana.geometry("800x600") # Se emplea para asignar la medida a una ventana, debe estar en formato string
    
    def VentanaMedia(self):
        self.ventana.geometry("1200x800")
    
    def VentanaGrande(self):
        self.ventana.geometry("1400x900")
    
    def VentanaCustom(self):
        ancho=self.dato1.get()
        alto=self.dato2.get()
        fusion=str(ancho)+"x"+str(alto)
        self.ventana.geometry(fusion)

    def Salir(self):
        sys.exit(0)


#BLOQUE PRINCIPAL
iniciar=Aplicacion()