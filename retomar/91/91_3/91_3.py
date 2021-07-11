import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import random
import os
import sys

ruta=os.path.dirname(__file__)
ruta_bomba_imagen=os.path.join(ruta, "./imagenes/bomba.png")


class Buscaminas:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("BUSCAMINAS")
        menu=tk.Menu(self.ventana)
        self.ventana.configure(bg="#14A9A4", menu=menu)
        opciones=tk.Menu(menu, tearoff=0)
        opciones.add_command(label="Reiniciar", command=self.Reiniciar)
        opciones.add_command(label="Salir", command=self.Salir)
        menu.add_cascade(label="Opciones", menu=opciones)
        self.listacasillas=[]
        self.listabombas=[]
        self.destapadas=[]
        self.bombacerca=0
        self.jugando=True
        self.bomba_imagen=tk.PhotoImage(file=ruta_bomba_imagen)
        self.bomba_imagen=self.bomba_imagen.subsample(20)
        self.ColocarBombas()
        self.CrearCasillas()
        self.ventana.geometry("700x700")
        self.ventana.mainloop()
 
    def CrearCasillas(self):
        for z in range(10):
            fila=[]
            for i in range(10):
                casilla=ttk.Button(self.ventana, command=lambda fila=z, columna=i: self.SeleccionCasilla(fila, columna))
                casilla.place(x=i*70, y=z*70, width=70, height=70)
                fila.append(casilla)
            self.listacasillas.append(fila)

    def ColocarBombas(self):
        total_bombas=0
        while total_bombas<10:
            similitud=0
            bomba_fila=random.randint(0, 9)
            bomba_columna=random.randint(0, 9)
            for x in range(len(self.listabombas)):
                if bomba_fila==self.listabombas[x][0] and bomba_columna==self.listabombas[x][1]:
                    similitud+=1
            if similitud==0:
                self.listabombas.append([bomba_fila, bomba_columna])
                total_bombas+=1

        
    def PisarBomba(self, fila, columna):
        similitud=0
        for x in range (len(self.listabombas)):
            if fila==self.listabombas[x][0] and columna==self.listabombas[x][1]:
                similitud+=1
        if similitud>0:
            return True
        else:
            return False
    
    def AnalizarDestapadas(self, fila, columna):
        similitud=0
        for x in range(len(self.destapadas)):
            if fila==self.destapadas[x][0] and columna==self.destapadas[x][1]:
                similitud+=1
        if similitud>0:
            return True
        else:
            return False
    
    def AnalizarAlrededor(self, fila, columna, limite=False):
        if fila>=0 and fila<10 and columna>=0 and columna<10:
            bomba=self.PisarBomba(fila, columna)
            if bomba==True:
                self.bombacerca+=1
            if limite!=True:
                self.AnalizarAlrededor(fila-1, columna-1, True)
                self.AnalizarAlrededor(fila-1, columna, True)
                self.AnalizarAlrededor(fila-1, columna+1, True)
                self.AnalizarAlrededor(fila, columna+1, True)
                self.AnalizarAlrededor(fila+1, columna+1, True)
                self.AnalizarAlrededor(fila+1, columna, True)
                self.AnalizarAlrededor(fila+1, columna-1, True)
                self.AnalizarAlrededor(fila, columna-1, True)
    
    def EliminarCasilla(self, fila, columna):
        self.listacasillas[fila][columna].destroy()
        self.listacasillas[fila][columna]=None

    def SeleccionCasilla(self, fila, columna):
        inicial=self.PisarBomba(fila, columna)
        if self.jugando:
            if inicial==True:
                self.listacasillas[fila][columna].configure(image=self.bomba_imagen, compound="center")
                self.jugando=False
                self.RevelarBombas()
                mb.showwarning("DERROTA","LO SIENTO. ¡HAS PISADO UNA BOOOMBA!")
            else:
                self.AnalizarTablero(fila, columna)
            if len(self.destapadas)>=90:
                self.jugando=False
                mb.showinfo("FELICIDADES","¡FELICIDADES, HAS GANADO!")

    def AnalizarTablero(self, fila, columna):
        if fila>=0 and fila<10 and columna>=0 and columna<10:
            destapada=self.AnalizarDestapadas(fila, columna)
            if destapada==False:
                self.destapadas.append([fila, columna])
                self.AnalizarAlrededor(fila, columna, False)
                self.listacasillas[fila][columna].configure(text=self.bombacerca)
                if self.bombacerca==0:
                    self.EliminarCasilla(fila, columna)
                    self.AnalizarTablero(fila-1, columna-1)
                    self.AnalizarTablero(fila-1, columna)
                    self.AnalizarTablero(fila-1, columna+1)
                    self.AnalizarTablero(fila, columna+1)
                    self.AnalizarTablero(fila+1, columna+1)
                    self.AnalizarTablero(fila+1, columna)
                    self.AnalizarTablero(fila+1, columna-1)
                    self.AnalizarTablero(fila, columna-1)
        self.bombacerca=0

    def Reiniciar(self):
        self.LimpiarTablero()
        self.listacasillas.clear()
        self.listabombas.clear()
        self.destapadas.clear()
        self.jugando=True
        self.CrearCasillas()
        self.ColocarBombas()


    def LimpiarTablero(self):
        for x in range(len(self.listacasillas)):
            for i in range(len(self.listacasillas[x])):
                if self.listacasillas[x][i]!=None:
                    self.listacasillas[x][i].destroy()
                    self.listacasillas[x][i]=None
    
    def RevelarBombas(self):
        for x in range(len(self.listabombas)):
            fila=self.listabombas[x][0]
            columna=self.listabombas[x][1]
            self.listacasillas[fila][columna].configure(image=self.bomba_imagen)

    def Salir(self):
        sys.exit(0)


if __name__=="__main__":
    ejecutar=Buscaminas()


