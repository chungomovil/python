import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import random

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("LABERINTO")
        self.Casillas=[]
        self.CrearTablero()
        self.boton1=ttk.Button(self.ventana, width=15, text="Recorrer")
        self.boton1.grid(column=0, row=11, padx=10, pady=10, columnspan=5)
        self.boton2=ttk.Button(self.ventana, width=15, text="Generar otro")
        self.boton2.grid(column=5, row=11, padx=10, pady=10, columnspan=5)
        print(self.Casillas)
        self.ventana.mainloop()
    
    def CrearTablero(self):
        for x in range(10):
            linea=[]
            for columna in range(10):
                etiqueta=ttk.Label(self.ventana, text=self.Aleatorizar())
                etiqueta.grid(column=columna, row=x, padx=5, pady=5)
                linea.append(etiqueta)
            self.Casillas.append(linea)



    def Aleatorizar(self):
        num=random.randint(0,1)
        return num

        
        
iniciar=Aplicacion()



