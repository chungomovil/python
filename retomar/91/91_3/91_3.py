import tkinter as tk
from tkinter import ttk
import random
import os

ruta=os.path.dirname(__file__)
ruta_bomba_imagen=os.path.join(ruta, "./imagenes/bomba.png")


class Buscaminas:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("BUSCAMINAS")
        self.listacasillas=[]
        self.bombacerca=0
        self.bomba_imagen=tk.PhotoImage(file=ruta_bomba_imagen)
        self.bomba_imagen=self.bomba_imagen.subsample(35)
        self.listabombas=self.ColocarBombas()
        self.CrearCasillas()
        self.ventana.mainloop()
 
    def CrearCasillas(self):
        for x in range(10):
            fila=[]
            for i in range(10):
                casilla=ttk.Button(self.ventana, width=7, command=lambda columna=x, fila=i: self.AnalizarTablero(columna, fila))
                casilla.grid(column=i, row=x, ipadx=0, ipady=5)
                fila.append(casilla)
            self.listacasillas.append(fila)

    def ColocarBombas(self):
        listabombas=[]
        total_bombas=0
        while total_bombas<10:
            similitud=False
            bomba_fila=random.randint(0, 9)
            bomba_columna=random.randint(0, 9)
            for x in range(len(listabombas)):
                if bomba_fila==listabombas[x][0] and bomba_columna==listabombas[x][1]:
                    similitud=True
            if similitud==False:
                listabombas.append([bomba_fila, bomba_columna])
                total_bombas+=1
        return listabombas

        
    def PisarBomba(self, fila, columna):
        similitud=False
        for x in range (len(self.listabombas)):
            if fila==self.listabombas[x][0] and columna==self.listabombas[x][1]:
                similitud=True
        return similitud
    """PROBAR HACER UN FUNCION APARTE PARA PULSAR, LLAMAR DESDE ÉSTA A LA RECURSIVA QUE ANALICE Y RETORNE EL TOTAL DE BOMBAS DE ALREDEDOR"""
    def AnalizarTablero(self, fila, columna, limite=False):
        resultado=self.PisarBomba(fila, columna)
        if resultado==True:
            self.bombacerca+=1
        else:
            if fila>0 and fila<9 and columna>0 and columna<9 and limite==False:
                self.AnalizarTablero(fila-1, columna-1, True)
                self.AnalizarTablero(fila-1, columna, True)
                self.AnalizarTablero(fila-1, columna+1, True)
                self.AnalizarTablero(fila, columna+1, True)
                self.AnalizarTablero(fila+1, columna+1, True)
                self.AnalizarTablero(fila+1, columna, True)
                self.AnalizarTablero(fila+1, columna-1, True)
                self.AnalizarTablero(fila, columna-1, True)
        self.listacasillas[fila][columna].configure(text=self.bombacerca)
        self.bombacerca=0



ejecutar=Buscaminas()


