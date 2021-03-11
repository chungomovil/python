"""
Confeccionar una aplicación que muestre un cuaderno con tres pestañas. Los títulos de cada pestaña deben ser 'Button', 'Label' y 'Entry'. Según la pestaña seleccionada mostrar un mensaje informando el objetivo de la clase y un ejemplo de la misma.
"""

import tkinter as tk
from tkinter import ttk
import random
import sys

class Aplicacion():

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Notebook y Frame")
        #CREACION DEL MENU
        self.menubar1=tk.Menu(self.ventana)
        self.ventana.configure(menu=self.menubar1)
        self.opcion1=tk.Menu(self.menubar1, tearoff=0)
        self.opcion1.add_command(label="Salir", command=self.Salir)
        self.menubar1.add_cascade(label="Opciones", menu=self.opcion1)
        #CREACION DEL NOTEBOOK
        self.notebook1=ttk.Notebook(self.ventana)
        #CREACION DE LOS FRAME
        self.frame1=ttk.Frame(self.notebook1)
        self.notebook1.add(self.frame1, text="Label")
        self.etiqueta1=ttk.Label(self.frame1, text="La clase Label en Python sirve para mostrar salida de texto en las ventanas del entorno grafico tkinter.")
        self.etiqueta1.grid(column=0, row=0)
        self.etiqueta2=ttk.Label(self.ventana, text="Pueden tener saltos de linea en su interior \n o incluso tener la letra de un color personalizado.", foreground="blue")
        self.etiqueta2.grid(column=0, row=1)
        self.frame2=ttk.Frame(self.notebook1)
        self.notebook1.add(self.frame2, text="Button")
        self.etiqueta2=ttk.Label(self.frame2, text="La clase Button en Python sirven para ejecutar una accion al hacer click sobre ellos.\n Por defecto se crean en estado 'activado'.")
        self.etiqueta2.grid(column=0, row=0)
        self.boton1=ttk.Button(self.frame2, text="Pulsame", command=self.Colores)
        self.boton1.grid(column=0, row=1)
        self.etiqueta4=ttk.Label(self.frame2, text="Pero tambien pueden crearse desactivados.")
        self.etiqueta4.grid(column=0, row=2)
        self.boton2=ttk.Button(self.frame2, text="No me puedes pulsar", state="disabled")
        self.boton2.grid(column=0, row=3)
        self.frame3=ttk.Frame(self.notebook1)
        self.notebook1.add(self.frame3, text="Entry")
        self.etiqueta5=ttk.Label(self.frame3, text="La clase Entry en Python nos permite ingresar valores por teclado para ser procesados por el programa.")
        self.etiqueta5.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entrada1=ttk.Entry(self.frame3, width=20, textvariable=self.dato1)
        self.entrada1.grid(column=0, row=1)
        self.boton3=ttk.Button(self.frame3, text="Mostrar resultado", command=self.MostrarTexto)
        self.boton3.grid(column=0, row=2)
        self.etiqueta6=ttk.Label(self.frame3)
        self.etiqueta6.grid(column=0, row=3)
        self.ventana.minsize(400, 300)
        self.notebook1.grid(column=0, row=0)
        self.ventana.mainloop()

    #CAMBIAR COLORES DEL LABEL AL PULSAR BOTON
    def Colores(self):
        lista_colores=("red","blue","orange","green","pink","brown")
        numero=random.randint(0, 5)
        self.etiqueta2.configure(foreground=lista_colores[numero])

    #MOSTRAR SALIDA DE TEXTO INTRODUCIDO EN UNA LABEL
    def MostrarTexto(self):
        texto=self.dato1.get()
        if texto=="":
            textomod="Has dejado el campo vacio"
        else:
            textomod="Has introducido: "+texto
        self.etiqueta6.configure(text=textomod)

    #SALIR
    def Salir(self):
        sys.exit(0)

#BLOQUE PRINCIPAL
iniciar=Aplicacion()
