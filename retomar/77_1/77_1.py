#Importamos librerias necesarias
import tkinter as tk
#Importamos la libreria 'os' para las rutas relativas
import os

#Capturamos la ruta absoluta de el directorio del archivo de python con el que se estra trabajando
directorio=os.path.dirname(__file__) #la constante __file__ se refiere al archivo de python actual

#Creamos la clase
class Aplicacion:
    #Creamos el metodo constructor
    def __init__(self):
        #Creamos la ventana
        self.ventana=tk.Tk()
        self.ventana.title("Mostar imagenes con tkinter")
        #Creamos el lienzo
        self.lienzo1=tk.Canvas(self.ventana, width=800, height=600, background="black")
        self.lienzo1.grid(column=0, row=0)
        #Importamos las imagenes y empleamos nuevamente la libreria 'os' para importarlas desde la ruta relativa
        self.carta1=tk.PhotoImage(file=os.path.join(directorio, "carta1.png"))
        self.carta2=tk.PhotoImage(file=os.path.join(directorio, "carta2.png"))
        self.carta3=tk.PhotoImage(file=os.path.join(directorio, "carta3.png"))
        #Plasmamos las imagenes en el lienzo
        self.lienzo1.create_image(50, 100, image=self.carta1, anchor="nw")  # 'Anchor' especifica desde que vertice se expandera la imagen en este caso desde el vertice superior izquierdo, por defecto es 'center'
        self.lienzo1.create_image(300, 100, image=self.carta2, anchor="nw")
        self.lienzo1.create_image(550, 100, image=self.carta3, anchor="nw")
        #Parametros de la ventana
        self.ventana.resizable(0, 0)
        self.ventana.mainloop()
        
#Bloque principal y creacion de obtejo
iniciar=Aplicacion()
