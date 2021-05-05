import tkinter as tk
from tkinter import ttk

class FormularioArticulos:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("MANTENIMIENTO DE ARTICULOS")
        self.notebook=ttk.Notebook(self.ventana)
        self.notebook.grid(column=0, row=0, padx=10, pady=10)
        self.CargaArticulo()
        self.ventana.mainloop()

    def CargaArticulo(self):
        self.frame1=ttk.Frame(self.notebook)
        self.notebook.add(self.frame1, text="Carga de Articulos")
        self.labelframe1=tk.LabelFrame(self.frame1, text="Articulo")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)
        self.etiqueta1=ttk.Label(self.labelframe1, text="Descripcion:")
        self.etiqueta1.grid(column=0, row=0, padx=5, pady=10)
        self.dato1=tk.StringVar()
        self.entrada1=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato1)
        self.entrada1.grid(column=1, row=0, padx=5, pady=10)
        self.etiqueta2=ttk.Label(self.labelframe1, text="Precio:")
        self.etiqueta2.grid(column=0, row=1, padx=5, pady=10)
        self.dato2=tk.StringVar()
        self.entrada2=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato2)
        self.entrada2.grid(column=1, row=1, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", width=15)
        self.boton1.grid(column=1, row=2, padx=5, pady=10)

iniciar=FormularioArticulos()

