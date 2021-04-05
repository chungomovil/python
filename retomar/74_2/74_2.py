import tkinter as tk
from tkinter import ttk
import sys

class Aplicacion:
    
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Tres en Raya")
        menubar=tk.Menu(self.ventana)
        #(EXTRA) Creamos el menu
        self.ventana.configure(menu=menubar)
        opciones1=tk.Menu(menubar, tearoff=0)
        opciones1.add_command(label="SALIR", command=self.Salir)
        menubar.add_cascade(label="Opciones", menu=opciones1)
        #Creamos el lienzo
        self.lienzo1=tk.Canvas(self.ventana, width=800, height=600, background="black")
        self.lienzo1.grid(column=0, row=0)
        #(EXTRA) Creamos el labelframe para la opcion de limpiar
        self.labelframe1=ttk.LabelFrame(self.ventana, text="HERRAMIENTAS")
        self.labelframe1.grid(column=0, row=1, padx=10, pady=10, sticky="w")
        #Llamamos al metodo que crea el tablero del juego
        self.CrearTablero()
        #(EXTRA) Llamamos al metodo de la opcion de limpiar
        self.Herramientas()
        #Creamos evento de captura de la posicion del raton
        self.lienzo1.bind("<Motion>", self.Posicion)
        #Creamos evento de captura del click izquierdo
        self.lienzo1.bind("<Button-1>", self.Pulsar)
        #Creamos evento de captura cuando se suelte el click izquierdo
        self.lienzo1.bind("<ButtonRelease-1>", self.Soltar)
        #Ponemos la variable de presionar en falso ya que aun no se ha presionado tecla
        self.presionar=False
        self.ventana.geometry("800x700")
        self.ventana.resizable(0, 0)
        self.ventana.mainloop()

    #Metodo para añadir el boton al labelframe
    def Herramientas(self):
        self.boton1=ttk.Button(self.labelframe1, width=20, text="LIMPIAR", command=self.Limpiar)
        self.boton1.grid(column=0, row=0, padx=10, pady=10)
    
    #Metodo para limpiar tablero con el boton
    def Limpiar(self):
        self.lienzo1.delete(tk.ALL)
        self.CrearTablero()

    #Metodo para crear tablero del juego
    def CrearTablero(self):
        self.lienzo1.create_line(250, 50, 250, 550, fill="yellow")
        self.lienzo1.create_line(550, 50, 550, 550, fill="yellow")
        self.lienzo1.create_line(50, 200, 750, 200, fill="yellow")
        self.lienzo1.create_line(50, 400,750, 400, fill="yellow")

    #Metodo de captura de posicion si se clickea y muestra true cuando se hace
    def Pulsar(self, evento):
        self.presionar=True
        #se toma primero esta posicion para dibujar linea a partir del click
        self.posicionx=evento.x
        self.posiciony=evento.y

    #Metodo para dibujar linea si se arrastra el cursor mientras esta pulsado
    def Posicion(self, evento):
        if self.presionar==True:
            #se debe renovar la posicion continuamente para que se muestra una linea continua
            self.lienzo1.create_line(self.posicionx, self.posiciony, evento.x, evento.y, fill="red")
            self.posicionx=evento.x
            self.posiciony=evento.y
    
    #Metodo para controlar si se suelta el cursor no dibuje
    def Soltar(self, evento):
        self.presionar=False

    #Metodo para salir
    def Salir(self):
        sys.exit(0)

#Bloque principal
iniciar=Aplicacion()
