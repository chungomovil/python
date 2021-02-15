"""
Mostrar los botones del 1 al 5. Cuando se presiona mostrar en una Label todos los botones presionados hasta ese momento.
"""

import tkinter as tk
import sys

class Aplicacion:
    #Lista para agregar numeros
    numeros=[]

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Mostrar tecla pulsada")
        self.boton1=tk.Button(self.ventana, text="1", command=self.num1)
        self.boton1.grid(column=0, row=0)
        self.boton2=tk.Button(self.ventana, text="2", command=self.num2)
        self.boton2.grid(column=1, row=0)
        self.boton3=tk.Button(self.ventana, text="3", command=self.num3)
        self.boton3.grid(column=2, row=0)
        self.boton4=tk.Button(self.ventana, text="4", command=self.num4)
        self.boton4.grid(column=3, row=0)
        self.boton5=tk.Button(self.ventana, text="5", command=self.num5)
        self.boton5.grid(column=4, row=0)
        self.etiqueta1=tk.Label(self.ventana, foreground="blue")
        self.etiqueta1.grid(column=5, row=0)
        self.salir=tk.Button(self.ventana, text="Salir", command=self.salir)
        self.salir.grid(column=0, row=1)
        self.ventana.resizable(False, False)
        self.ventana.minsize(400, 100)
        self.ventana.mainloop()
    
    def num1(self):
        #Se agrega el numero pulsado a la lista y se imprime en el label
        Aplicacion.numeros.append(1)
        self.etiqueta1.configure(text=Aplicacion.numeros)
    
    def num2(self):
        Aplicacion.numeros.append(2)
        self.etiqueta1.configure(text=Aplicacion.numeros)
    
    def num3(self):
        Aplicacion.numeros.append(3)
        self.etiqueta1.configure(text=Aplicacion.numeros)

    def num4(self):
        Aplicacion.numeros.append(4)
        self.etiqueta1.configure(text=Aplicacion.numeros)

    def num5(self):
        Aplicacion.numeros.append(5)
        self.etiqueta1.configure(text=Aplicacion.numeros)
    #Salir del programa
    def salir(self):
        sys.exit(0)
    

iniciar=Aplicacion()
