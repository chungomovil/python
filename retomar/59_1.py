"""
Confeccionar un programa que permita ingresar dos números en controles de tipo Entry, luego sumar los dos valores ingresados y mostrar la suma en una Label al presionar un botón.
"""

import tkinter as tk

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Sumar numeros")
        self.num1=tk.StringVar()
        self.campo1=tk.Entry(self.ventana, width=10, textvariable=self.num1)
        self.campo1.grid(column=0, row=0)
        self.etiqueta1=tk.Label(self.ventana, text="+")
        self.etiqueta1.grid(column=1, row=0)
        self.num2=tk.StringVar()
        self.campo2=tk.Entry(self.ventana, width=10, textvariable=self.num2)
        self.campo2.grid(column=2, row=0)
        self.boton1=tk.Button(self.ventana, text="Sumar", command=self.Sumar)
        self.boton1.grid(column=0, row=1)
        self.etiqueta2=tk.Label(self.ventana)
        self.etiqueta2.grid(column=0, row=2)
        self.ventana.minsize(300, 150)
        self.ventana.mainloop()

    def Sumar(self):
        #Recordar pasar los valores a enteros
        num1=int(self.num1.get())
        num2=int(self.num2.get())
        suma=num1+num2
        self.etiqueta2.configure(text=suma, foreground="red")
    
iniciar=Aplicacion()
