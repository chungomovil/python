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
        self.ventana.configure(bg="green")
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
                casilla=ttk.Button(self.ventana, width=7, command=lambda fila=x, columna=i: self.AnalizarTablero(fila, columna))
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
    
    def SeleccionCasilla(self, fila, columna):
        inicial=self.PisarBomba(fila, columna)
        if inicial==True:
            self.listacasillas[fila][columna].configure(image=self.bomba_imagen, compound="center")
        else:
            lista_recorrida=self.AnalizarTablero(fila, columna)
            """if self.bombacerca==0:
                for x in range(len(lista_recorrida)):
                    fila_actual=lista_recorrida[x][0]
                    columna_actual=lista_recorrida[x][1]
                    self.listacasillas[fila_actual][columna_actual].configure(text="0")"""
            self.listacasillas[fila][columna].configure(text=self.bombacerca)
            self.bombacerca=0

    def AnalizarTablero(self, fila, columna, limite=False, lista_recorrida=[]):
        if fila>=0 and fila<10 and columna>=0 and columna<10:
            resultado=self.PisarBomba(fila, columna)
            if resultado==True:
                self.bombacerca+=1
            if limite!=True:
                self.AnalizarTablero(fila-1, columna-1, True)
                self.AnalizarTablero(fila-1, columna, True)
                self.AnalizarTablero(fila-1, columna+1, True)
                self.AnalizarTablero(fila, columna+1, True)
                self.AnalizarTablero(fila+1, columna+1, True)
                self.AnalizarTablero(fila+1, columna, True)
                self.AnalizarTablero(fila+1, columna-1, True)
                self.AnalizarTablero(fila, columna-1, True)
        #self.listacasillas[fila][columna].configure(text=self.bombacerca)
        

        #return lista_recorrida


if __name__=="__main__":
    ejecutar=Buscaminas()


