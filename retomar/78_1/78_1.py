#Importar librerias necesarias
import tkinter as tk
from tkinter import ttk
import os

#Ruta del archivo actual
carpeta=os.path.dirname(__file__)

#Creamos la clase
class Aplicacion:

    #Creamos el metodo constructor
    def __init__(self):
        #Creamos la ventana
        self.ventana=tk.Tk()
        self.ventana.title("Mover figuras con tkinter")
        #(EXTRA)Creamos el labelframe para las opciones del programa
        self.labelframe1=tk.LabelFrame(self.ventana, text="OPCIONES")
        self.labelframe1.grid(column=0, row=0, pady=20, sticky="we")
        #Importamos el metodo de las opciones del programa
        self.Contenido()
        #Creamos el lienzo
        self.lienzo1=tk.Canvas(self.ventana, width=1200, height=700, background="black")
        self.lienzo1.grid(column=0, row=1)
        #Importamos el metodo para crear figuras en el lienzo
        self.CrearFiguras()
        #Capturamos los eventos relacionados con las interacciones de las figuras etiquetadas como 'carta'
        self.lienzo1.tag_bind("carta","<ButtonPress-1>", self.Presionar)
        self.lienzo1.tag_bind("carta","<Button1-Motion>", self.MoverPresionado)
        #Incluimos la variable de seleccion de carta, vacia por el momento
        self.carta_seleccionada=None
        #Parametros de la ventana
        self.ventana.resizable(0, 0)
        self.ventana.mainloop()

    #(EXTRA)Metodo del contenido del labelframe
    def Contenido(self):
        self.boton1=ttk.Button(self.labelframe1, width=40, text="RESET", command=self.Reset)
        self.boton1.grid(column=0, row=0, padx=450)

    #Metodo para crear las figuras(imagen en este caso)
    def CrearFiguras(self):
        self.carta1=tk.PhotoImage(file=os.path.join(carpeta, "./carta1.png"))
        self.carta2=tk.PhotoImage(file=os.path.join(carpeta, "./carta2.png"))
        self.lienzo1.create_image(60, 60, image=self.carta1, anchor="nw", tag="carta")
        self.lienzo1.create_image(120, 120, image=self.carta2, anchor="nw", tag="carta")

    #Metodo para capturar en cual imagen se presiono
    def Presionar(self, evento):
        #Esta variable almacena cual de todas las imagenes con la misma etiqueta fue seleccionada
        carta=self.lienzo1.find_withtag(tk.CURRENT)
        #Ahora cambiamos el valor a la variable de INSTANCIA que definimos en el constructor
        #Se almacenaria una tupla con la imagen elegida, y las coordenadas del click
        self.carta_seleccionada=(carta, evento.x, evento.y)
    
    #Metodo para capturar el movimiento del cursor mientras esta pulsado el click
    def MoverPresionado(self, evento):
        #Coordenadas del movimiento
        mover_X=evento.x
        mover_Y=evento.y
        #Desempaquetamos tupla anterior
        carta, posicion_X, posicion_Y=self.carta_seleccionada
        #Movemos figura
        self.lienzo1.move(carta, mover_X-posicion_X, mover_Y-posicion_Y)
        #Refrescamos la posicion de la figura
        self.carta_seleccionada=(carta, mover_X, mover_Y)
    
    #(EXTRA)Metodo para resetear el lienzo
    def Reset(self):
        self.lienzo1.delete(tk.ALL)
        self.CrearFiguras()

#Bloque principal y creacion de objeto
iniciar=Aplicacion()

