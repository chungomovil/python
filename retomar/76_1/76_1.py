#Importamos libreria necesaria
import tkinter as tk

#Creamos la clase
class Aplicacion:

    #Creamos el constructor
    def __init__(self):
        #Creamos ventana
        self.ventana=tk.Tk()
        self.ventana.title("Mover figuras con KeyPress")
        #Creamos el lienzo
        self.lienzo1=tk.Canvas(self.ventana, width=800, height=600, background="black")
        self.lienzo1.grid(column=0, row=0)
        #Creamos el cuadrado en el lienzo
        self.cuadrado=self.lienzo1.create_rectangle(50, 200, 150, 300, fill="red")
        #Creamos el motodo de escucha al pulsar una tecla (OJO: el evento de escucha se lanza en toda la ventana, no solo en el lienzo)
        self.ventana.bind("<KeyPress>", self.Mover)
        #Parametros de la ventana
        self.ventana.resizable(0, 0)
        self.ventana.mainloop()

    #Metodo para mover la figura ante el evento de pulsar una tecla
    def Mover(self, evento):
        #Si el evento se corresponde con la tecla pulsada mueve la figura
        if evento.keysym=="Right":
            #Movemos la figura
            self.lienzo1.move(self.cuadrado, 10, 0)
        if evento.keysym=="Left":
            self.lienzo1.move(self.cuadrado, -10, 0)
        if evento.keysym=="Down":
            self.lienzo1.move(self.cuadrado, 0, 10)
        if evento.keysym=="Up":
            self.lienzo1.move(self.cuadrado, 0, -10)

#Bloque principal
#Creacion del objeto
iniciar=Aplicacion()


