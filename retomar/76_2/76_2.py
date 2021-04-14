#Importar librerias necesarias
import tkinter as tk
import sys

#Creacion de la clase
class Aplicacion:
    #Creamos el metodo constructor
    def __init__(self):
        #Creamos ventana
        self.ventana=tk.Tk()
        self.ventana.title("Moviendo figuras con Keypress evitando desbordamiento")
        #Creamos menu y sus opciones
        menubar=tk.Menu(self.ventana)
        self.ventana.configure(menu=menubar)
        opciones1=tk.Menu(menubar, tearoff=0)
        opciones1.add_command(label="SALIR", command=self.Salir)
        menubar.add_cascade(label="Opciones", menu=opciones1)
        opciones2=tk.Menu(menubar, tearoff=0)
        opciones2.add_command(label="Lento", command=self.Lento)
        opciones2.add_command(label="Normal", command=self.Normal)
        opciones2.add_command(label="Rapido", command=self.Rapido)
        opciones2.add_command(label="SUPERSONICO", command=self.Supersonico)
        menubar.add_cascade(label="Rapidez", menu=opciones2)
        #Creamos lienzo
        self.lienzo1=tk.Canvas(self.ventana, width=800, height=600, background="black")
        self.lienzo1.grid(column=0, row=0)
        #Creamos el cuadrado
        self.cuadrado=self.lienzo1.create_rectangle(50, 50, 150, 150, fill="yellow")
        #Creamos el evento que captura las teclas
        self.ventana.bind("<KeyPress>", self.Mover)
        #Creamos la variable estandar de velocidad
        self.velocidad=6
        #Parametros de la ventana
        self.ventana.resizable(0, 0)
        self.ventana.mainloop()

    #Metodo para mover el cuadrado
    def Mover(self, evento):
        #Llamamos al metodo que impide que se salga del lienzo al moverse
        self.AntiOverFlow()
        #Condiciones de movimiento segun la tecla pulsada
        if evento.keysym=="Right":
            self.lienzo1.move(self.cuadrado, self.velocidad, 0) #Empleamos la variable velocidad para que se mueva segun la opcion elegida
        if evento.keysym=="Left":
            self.lienzo1.move(self.cuadrado, -self.velocidad, 0)
        if evento.keysym=="Down":
            self.lienzo1.move(self.cuadrado, 0 , self.velocidad)
        if evento.keysym=="Up":
            self.lienzo1.move(self.cuadrado, 0, -self.velocidad)

    #Metodo para impedir que el cuadrado se salga del lienzo
    def AntiOverFlow(self):
        #Capturamos la posicion actual de la figura
        x1, y1, x2, y2=self.lienzo1.coords(self.cuadrado)
        #Condiciones que regresan al cuadrado al borde cuando se salga
        if x1<0+self.velocidad:
            self.lienzo1.move(self.cuadrado, self.velocidad+15, 0) #Empleamos la variable velocidad + otro valor para regresar el cuadrado a la casilla velocidad(equivaldria a 0) +15 casillas
        if y1<0+self.velocidad:
            self.lienzo1.move(self.cuadrado, 0, self.velocidad+15)
        if x2>800-self.velocidad:
            self.lienzo1.move(self.cuadrado, -self.velocidad-15, 0)
        if y2>600-self.velocidad:
            self.lienzo1.move(self.cuadrado, 0, -self.velocidad-15)

    #Metodo de movimiento lento
    def Lento(self):
        self.velocidad=2

    #Metodo de movimiento normal
    def Normal(self):
        self.velocidad=6
    
    #Metodo de movimiento rapido
    def Rapido(self):
        self.velocidad=20

    #Metodo de movimiento super rapido
    def Supersonico(self):
        self.velocidad=50

    #Metodo para salir
    def Salir(self):
        sys.exit(0)

#Bloque principal y creacion de objeto
iniciar=Aplicacion()
