import tkinter as tk
from tkinter import ttk
import random

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Eliminando figuras con 'Id' y 'Tag'")
        self.labelframe1=ttk.LabelFrame(self.ventana, text="CREAR")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10, sticky="we")
        self.lienzo1=tk.Canvas(self.ventana, width=800, height=600, background="black")
        self.lienzo1.grid(column=0, row=1, pady=10)
        self.eleccion=0
        self.pulsacion=False
        self.ControlesRaton()
        self.OpcionesCrear()
        self.ventana.geometry("800x700")
        self.ventana.resizable(0, 0)
        self.ventana.mainloop()

    def OpcionesCrear(self):
        self.boton1=ttk.Button(self.labelframe1, width=20, text="Crear Linea", command=self.Linea)
        self.boton1.grid(column=0, row=0, padx=5, pady=10)
        self.boton2=ttk.Button(self.labelframe1, width=20, text="Crear Rectangulo", command=self.Rectangulo)
        self.boton2.grid(column=1, row=0, padx=5, pady=10)
        self.boton3=ttk.Button(self.labelframe1, width=20, text="Crear Cuadrado", command=self.Cuadrado)
        self.boton3.grid(column=2, row=0, padx=5, pady=10)
        self.boton4=ttk.Button(self.labelframe1, width=20, text="Crear Ovalo", command=self.Ovalo)
        self.boton4.grid(column=3, row=0, padx=5, pady=10)

    def ControlesRaton(self):
        self.lienzo1.bind("<Button-1>", self.Pulsar)
        self.lienzo1.bind("<ButtonRelease-1>", self.Soltar)
    
    def Pulsar(self, evento):
        self.pulsacion=True
        self.posicionx=evento.x
        self.posiciony=evento.y
        self.Dibujar()
        
    def Soltar(self, evento):
        self.pulsacion=False

    def Aleatorio(self):
        num=random.randint(10, 150)
        return num
    
    def Linea(self):
        self.eleccion=1
    
    def Rectangulo(self):
        self.eleccion=2
    
    def Cuadrado(self):
        self.eleccion=3
    
    def Ovalo(self):
        self.eleccion=4

    def Dibujar(self):
        #crear aleatorio solo al comenzar metodo y crear algoritmo para situar el cursor en medio del objetivo creado
        if self.pulsacion==True:
            if self.eleccion==1:
                self.lienzo1.create_line(self.posicionx-self.Aleatorio(), self.posiciony-self.Aleatorio(), self.posicionx+self.Aleatorio(), self.posiciony+self.Aleatorio(), fill="red")
            if self.eleccion==2:
                self.lienzo1.create_rectangle(self.posicionx-self.Aleatorio(), self.posiciony-self.Aleatorio(), self.posicionx+self.Aleatorio(), self.posiciony+self.Aleatorio(), fill="yellow")


iniciar=Aplicacion()


