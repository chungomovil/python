"""
Solicitar el ingreso del nombre de una persona y seleccionar de un control Listbox un país. Al presionar un botón mostrar en la barra de la ventana el nombre ingresado y el país seleccionado.
"""

import tkinter as tk
import sys

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Datos")
        self.etiqueta1=tk.Label(self.ventana, text="Nombre:")
        self.etiqueta1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.nombre=tk.Entry(self.ventana, width="20", textvariable=self.dato1)
        self.nombre.grid(column=1, row=0)
        self.etiqueta2=tk.Label(self.ventana, text="Pais")
        self.etiqueta2.grid(column=0, row=1)
        #CREAR LISTBOX CON SCROLL
        self.scroll1=tk.Scrollbar(self.ventana, orient=tk.VERTICAL)
        self.list1=tk.Listbox(self.ventana, yscrollcommand=self.scroll1.set)
        self.list1.grid(column=1, row=1)
        self.scroll1.configure(command=self.list1.yview)
        self.scroll1.grid(column=2, row=1, sticky="NS")
        self.list1.insert(0, "Alemania")
        self.list1.insert(1, "Cuba")
        self.list1.insert(2, "Suecia")
        self.list1.insert(3, "Marruecos")
        self.list1.insert(4, "Espania")
        self.list1.insert(5, "Estados Unidos")
        self.list1.insert(6, "Canada")
        self.list1.insert(7, "Chile")
        self.list1.insert(8, "Venezuela")
        self.list1.insert(9, "Japon")
        self.list1.insert(10, "India")
        self.list1.insert(11, "China")
        self.list1.insert(12, "Australia")
        self.boton1=tk.Button(self.ventana, text="Inscribir", command=self.validar)
        self.boton1.grid(column=1, row=2)
        self.boton2=tk.Button(self.ventana, text="Salir", command=self.salir)
        self.boton2.grid(column=1, row=3)
        self.ventana.minsize(400, 250)
        self.ventana.mainloop()

    def validar(self):
        nombre=self.dato1.get().capitalize()
        eleccion=self.list1.curselection()
        if len(eleccion)!=0:
            self.ventana.title("Nombre: "+nombre+", Pais: "+self.list1.get(eleccion))

    def salir(self):
        sys.exit(0)
    
iniciar=Aplicacion()
