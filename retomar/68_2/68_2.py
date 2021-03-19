import tkinter as tk
from tkinter import ttk

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Administrador de disenio GRID")
        self.boton1=ttk.Button(self.ventana, text="boton 1")
        self.boton1.grid(column=0, row=0)
        self.boton2=ttk.Button(self.ventana, text="boton 2")
        self.boton2.grid(column=1, row=0)
        self.boton3=ttk.Button(self.ventana, text="boton 3")
        #En el administrador GRID el atributo 'rowspan' expande la etiqueta un numero filas determinado mientras que el atributo 'sticky' rellena ese espacio con el contenido (ns -> norte a sur, we -> oeste a este)
        self.boton3.grid(column=2, row=0, rowspan=2, sticky="ns")
        self.boton4=ttk.Button(self.ventana, text="boton 4")
        self.boton4.grid(column=0, row=1)
        self.boton5=ttk.Button(self.ventana, text="boton 5")
        self.boton5.grid(column=1, row=1)
        self.boton6=ttk.Button(self.ventana, text="boton 6")
        #En el administrador GRID el atributo 'columnspan' expandela etiqueta un numero de columnas determinado
        self.boton6.grid(column=0, row=2, columnspan=3, sticky="we")
        self.ventana.mainloop()

iniciar=Aplicacion()
