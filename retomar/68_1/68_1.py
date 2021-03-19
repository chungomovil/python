import tkinter as tk
from tkinter import ttk

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Administrador de disenio PACK")
        #En el administrador pack, el atributo 'fill' se emplea para expandir el contanido a los lados seleccionados de la ventana
        self.boton1=ttk.Button(self.ventana, text="boton 1")
        self.boton1.pack(side=tk.TOP, fill=tk.BOTH)
        self.boton2=ttk.Button(self.ventana, text="boton 2")
        self.boton2.pack(side=tk.TOP, fill=tk.BOTH)
        self.boton3=ttk.Button(self.ventana, text="boton 3")
        self.boton3.pack(side=tk.TOP, fill=tk.BOTH)
        self.boton4=ttk.Button(self.ventana, text="boton 4")
        self.boton4.pack(side=tk.LEFT)
        self.boton5=ttk.Button(self.ventana, text="boton 5")
        self.boton5.pack(side=tk.RIGHT)
        self.boton6=ttk.Button(self.ventana, text="boton 6")
        self.boton6.pack(side=tk.RIGHT)
        self.boton7=ttk.Button(self.ventana, text="boton 7")
        self.boton7.pack(side=tk.RIGHT)
        self.ventana.mainloop()

iniciar=Aplicacion()
