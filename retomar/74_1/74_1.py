import tkinter as tk
from tkinter import ttk
import sys

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("COORDENADAS")
        #(EXTRA) Creamos menu
        menubar1=tk.Menu(self.ventana)
        self.ventana.configure(menu=menubar1)
        opciones1=tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="SALIR", command=self.Salir)
        menubar1.add_cascade(label="Opciones", menu=opciones1)
        #Creamos lienzo
        self.lienzo1=tk.Canvas(self.ventana, width=800, height=600, background="black")
        self.lienzo1.grid(column=0, row=0)
        #Creamos el evento de capturar posicion del cursor
        self.lienzo1.bind("<Motion>", self.Mover_Raton)
        #Creamos el evento de capturar click izquierdo
        self.lienzo1.bind("<Button-1>", self.Pulsar_Izq_Raton)
        self.ventana.geometry("800x600")
        self.ventana.resizable(0, 0)
        self.ventana.mainloop()

    #Metodo para mostrar en la barra de la ventana la posicion del cursor
    def Mover_Raton(self, evento):
        self.ventana.title("COORDENADAS: "+str(evento.x)+"-"+str(evento.y))
    
    #Metodo para crear un circulo en la posicion del click izquierdo
    def Pulsar_Izq_Raton(self, evento):
        self.lienzo1.create_oval(evento.x-10, evento.y-10, evento.x+10, evento.y+10, fill="red")

    #Metodo para salir desde la opcion del menu
    def Salir(self):
        sys.exit(0)

#Bloque principal
iniciar=Aplicacion()
