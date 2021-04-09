import tkinter as tk
from tkinter import ttk
import random
#CREAR UN MENU PARA SALIR
class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Eliminando figuras con 'Id' y 'Tag'")
        self.labelframe1=ttk.LabelFrame(self.ventana, text="CREAR")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10, sticky="we")
        self.labelframe2=ttk.LabelFrame(self.ventana, text="ELIMINAR")
        self.labelframe2.grid(column=0, row=1, padx=10, pady=10, sticky="we")
        self.lienzo1=tk.Canvas(self.ventana, width=900, height=600, background="black")
        self.lienzo1.grid(column=0, row=2, pady=10)
        self.eleccion=0
        self.pulsacion=False
        self.ControlesRaton()
        self.OpcionesCrear()
        self.OpcionesEliminar()
        self.ventana.geometry("900x800")
        self.ventana.resizable(0, 0)
        self.ventana.mainloop()

    def OpcionesCrear(self):
        self.boton1=ttk.Button(self.labelframe1, width=20, text="Crear Linea", command=self.Linea_Crear)
        self.boton1.grid(column=0, row=0, padx=5, pady=10)
        self.boton2=ttk.Button(self.labelframe1, width=20, text="Crear Rectangulo", command=self.Rectangulo_Crear)
        self.boton2.grid(column=1, row=0, padx=5, pady=10)
        self.boton3=ttk.Button(self.labelframe1, width=20, text="Crear Cuadrado", command=self.Cuadrado_Crear)
        self.boton3.grid(column=2, row=0, padx=5, pady=10)
        self.boton4=ttk.Button(self.labelframe1, width=20, text="Crear Ovalo", command=self.Ovalo_Crear)
        self.boton4.grid(column=3, row=0, padx=5, pady=10)

    def OpcionesEliminar(self):
        self.boton5=ttk.Button(self.labelframe2, width=20, text="Borrar Linea (Tag)", command=self.Linea_Eliminar_Tag)
        self.boton5.grid(column=0, row=0, padx=5, pady=10)
        self.boton6=ttk.Button(self.labelframe2, width=20, text="Borrar Rectangulo", command=self.Rectangulo_Eliminar)
        self.boton6.grid(column=1, row=0, padx=5, pady=10)
        self.boton7=ttk.Button(self.labelframe2, width=20, text="Borrar Cuadrado", command=self.Cuadrado_Eliminar)
        self.boton7.grid(column=2, row=0, padx=5, pady=10)
        self.boton8=ttk.Button(self.labelframe2, width=20, text="Borrar Ovalo", command=self.Ovalo_Eliminar)
        self.boton8.grid(column=3, row=0, padx=5, pady=10)
        self.boton9=ttk.Button(self.labelframe2, width=20, text="BORRAR TODOS", command=self.Todos_Eliminar)
        self.boton9.grid(column=4, row=0, padx=5, pady=10)
        self.boton10=ttk.Button(self.labelframe2, width=20, text="Borrar Linea (Id)", command=self.Linea_Eliminar_Id)
        self.boton10.grid(column=5, row=0, padx=5, pady=10)


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
        num=random.randint(10, 100)
        return num
    
    def Linea_Crear(self):
        self.eleccion=1
    
    def Linea_Eliminar_Id(self):
        self.lienzo1.delete(self.linea)

    def Linea_Eliminar_Tag(self):
        self.lienzo1.delete("linea")
    
    def Rectangulo_Crear(self):
        self.eleccion=2
    
    def Rectangulo_Eliminar(self):
        self.lienzo1.delete("rectangulo")

    def Cuadrado_Crear(self):
        self.eleccion=3

    def Cuadrado_Eliminar(self):
        self.lienzo1.delete("cuadrado")
    
    def Ovalo_Crear(self):
        self.eleccion=4

    def Ovalo_Eliminar(self):
        self.lienzo1.delete("ovalo")

    def Todos_Eliminar(self):
        self.lienzo1.delete(tk.ALL)

    def Dibujar(self):
        aleatorio=self.Aleatorio()
        if self.pulsacion==True:
            if self.eleccion==1:
                self.linea=self.lienzo1.create_line(self.posicionx-aleatorio, self.posiciony-aleatorio, self.posicionx+aleatorio, self.posiciony+aleatorio, fill="red", tag="linea")
            if self.eleccion==2:
                self.lienzo1.create_rectangle(self.posicionx-aleatorio, self.posiciony-aleatorio+aleatorio, self.posicionx+aleatorio+aleatorio, self.posiciony+aleatorio, fill="yellow", tag="rectangulo")
            if self.eleccion==3:
                self.lienzo1.create_rectangle(self.posicionx-aleatorio, self.posiciony-aleatorio, self.posicionx+aleatorio+50, self.posiciony+aleatorio+50, fill="orange", tag="cuadrado")
            if self.eleccion==4:
                self.lienzo1.create_oval(self.posicionx-aleatorio, self.posiciony-aleatorio, self.posicionx+aleatorio, self.posiciony+aleatorio, fill="green", tag="ovalo")




iniciar=Aplicacion()


