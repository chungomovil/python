#Importamos librerias necesarias
import tkinter as tk
from tkinter import ttk
import random

#Creamos la clase
class Aplicacion:

    #Creamos el metodo constructor
    def __init__(self):
        #Creamos la ventana
        self.ventana=tk.Tk()
        self.ventana.title("Mover figuras con tkinter parte II")
        #(EXTRA) Creamos el labelframe para las opciones del programa
        self.labelframe1=tk.LabelFrame(self.ventana, text="OPCIONES")
        self.labelframe1.grid(column=0, row=0)
        #Llamos al metodo de las opciones del labelframe
        self.Opciones()
        #Creamos el lienzo
        self.lienzo1=tk.Canvas(self.ventana, width=800, height=600, background="black")
        self.lienzo1.grid(column=0, row=1)
        #Creamos una variable vacia donde se almacenaran los datos de la figura seleccionada
        self.cuadrado_seleccionado=None
        #Llamamos a la funcion que crea los cuadrados con el parametro de cuantos deseamos crear
        self.CrearCuadrados(100)
        #Creamos los eventos que capturaran la pulsacion y movimiento mientras esta pulsado el click izquierdo
        self.lienzo1.tag_bind("cuadrado", "<ButtonPress-1>", self.Pulsar)
        self.lienzo1.tag_bind("cuadrado", "<Button1-Motion>", self.MoverPulsado)
        #Parametros de la ventana
        self.ventana.resizable(0, 0)
        self.ventana.mainloop()

    #Metodo para resetear el lienzo desde el labelframe1
    def Opciones(self):
        self.boton1=ttk.Button(self.labelframe1, width=30, text="RESETEAR", command=self.Resetear)
        self.boton1.grid(column=0, row=0, padx=250)

    #Metodo para crear los cuadrados en posiciones aleatorias del lienzo
    def CrearCuadrados(self, num):
        for x in range(num):
            coordenada_X=random.randint(1,750)
            coordenada_Y=random.randint(1,550)
            self.lienzo1.create_rectangle(coordenada_X, coordenada_Y, coordenada_X+50, coordenada_Y+50, fill="red", tag="cuadrado")

    #Metodo para capturar en cual cuadrado se hace click
    def Pulsar(self, evento):
        cuadrado=self.lienzo1.find_withtag(tk.CURRENT)
        self.cuadrado_seleccionado=(cuadrado, evento.x, evento.y)
    
    #Metodo para mover el cuadrado donde se realizo el click
    def MoverPulsado(self, evento):
        cuadrado, origen_X, origen_Y=self.cuadrado_seleccionado
        mover_X, mover_Y=evento.x, evento.y
        self.lienzo1.move(cuadrado, mover_X-origen_X, mover_Y-origen_Y)
        self.cuadrado_seleccionado=(cuadrado, mover_X, mover_Y)

    #Metodo para resetear lienzo
    def Resetear(self):
        self.lienzo1.delete(tk.ALL)
        self.CrearCuadrados(100)

#Bloque principal y creacion de objeto
iniciar=Aplicacion()

