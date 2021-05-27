import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import random

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("LABERINTO")
        self.Estado=False
        self.Casillas=[]
        self.CrearTablero()
        self.boton1=ttk.Button(self.ventana, width=15, text="Recorrer", command=self.IniciarRecorrido)
        self.boton1.grid(column=0, row=11, padx=10, pady=10, columnspan=5)
        self.boton2=ttk.Button(self.ventana, width=15, text="Generar otro", command=self.VaciarTablero)
        self.boton2.grid(column=5, row=11, padx=10, pady=10, columnspan=5)
        self.ventana.mainloop()
    
    def CrearTablero(self):
        self.Casillas=[]
        for x in range(10):
            linea=[]
            for columna in range(10):
                etiqueta=ttk.Label(self.ventana, text=self.Aleatorizar(), foreground="blue")
                etiqueta.grid(column=columna, row=x, padx=10, pady=10)
                linea.append(etiqueta)
            self.Casillas.append(linea)
        self.Casillas[0][0].configure(text="0")
        self.Casillas[9][9].configure(text="5")

    def VaciarTablero(self):
        for x in range(len(self.Casillas)):
            for i in range(len(self.Casillas[x])):
                self.Casillas[x][i].configure(text=self.Aleatorizar(), background="white")
        self.Casillas[0][0].configure(text="0")
        self.Casillas[9][9].configure(text="5")

    def IniciarRecorrido(self):
        self.Recorrer(0, 0)
        self.Estado=False

    def Recorrer(self, fila, columna):
        if columna>=0 and columna<10 and fila>=0 and fila<10 and self.Estado==False:
            casilla=str(self.Casillas[fila][columna].cget("text"))
            if casilla=="5":
                self.Estado=True
                mb.showinfo("FELICIDADES", "El laberinto tiene salida.")
            else:
                if casilla=="0":
                    self.Casillas[fila][columna].configure(text="9", background="yellow")
                    self.Recorrer(fila, columna+1)
                    self.Recorrer(fila+1, columna)
                    self.Recorrer(fila, columna-1)
                    self.Recorrer(fila-1, columna)
        
    

    def Aleatorizar(self):
        num=random.randint(0, 2)
        if num==1:
            return 1
        else:
            return 0

        
        
iniciar=Aplicacion()



