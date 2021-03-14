
import tkinter as tk
from tkinter import ttk

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Almacen de articulos")
        #Agregar labelframe
        self.labelframe1=ttk.LabelFrame(self.ventana, text="Articulo")
        self.labelframe1.grid(column=0, row=0, padx=20, pady=10)
        #Agregar items del labelframe
        self.Articulo()
        self.labelframe2=ttk.LabelFrame(self.ventana, text="Operaciones")
        self.labelframe2.grid(column=0, row=1, padx=20, pady=20)
        self.Operaciones()
        self.ventana.geometry("300x250")
        self.ventana.resizable(False, False)
        self.ventana.mainloop()

    #Items del labelframe
    def Articulo(self):
        self.etiqueta1=ttk.Label(self.labelframe1, text="Codigo de articulo:")
        self.etiqueta1.grid(column=0, row=0, padx=5, pady=5)
        self.entrada1=ttk.Entry(self.labelframe1)
        self.entrada1.grid(column=1, row=0, padx=5, pady=5)
        self.etiqueta2=ttk.Label(self.labelframe1, text="Descripcion:")
        self.etiqueta2.grid(column=0, row=1, padx=5, pady=5)
        self.entrada2=ttk.Entry(self.labelframe1)
        self.entrada2.grid(column=1, row=1, padx=5, pady=5)
        self.etiqueta3=ttk.Label(self.labelframe1, text="Precio:")
        self.etiqueta3.grid(column=0, row=2, padx=5, pady=5)
        self.entrada3=ttk.Entry(self.labelframe1)
        self.entrada3.grid(column=1, row=2, padx=5, pady=5)

    def Operaciones(self):
        self.boton1=ttk.Button(self.labelframe2, text="Agregar")
        self.boton1.grid(column=0, row=0, padx=5, pady=5)
        self.boton2=ttk.Button(self.labelframe2, text="Eliminar")
        self.boton2.grid(column=1, row=0, padx=5, pady=5)
        self.boton3=ttk.Button(self.labelframe2, text="Modificar")
        self.boton3.grid(column=2, row=0, padx=5, pady=5)

iniciar=Aplicacion()
