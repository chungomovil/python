import tkinter as tk
from tkinter import ttk

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Administrador de disenio PLACE")
        self.boton1=ttk.Button(self.ventana, text="Cancelar")
        #En el administrador PLACE, el contenido se debe posicionar mediante coordenadas en el espacio de la ventana (con 'x' e 'y'), los atributos 'width' y 'height' especifican el ancho y alto del contenido en cuestion
        self.boton1.place(x=620, y=550, width=70, height=30)
        self.boton2=ttk.Button(self.ventana, text="Confirmar")
        self.boton2.place(x=700, y=550, width=70, height=30)
        self.ventana.geometry("800x600")
        #Es aconsejable bloquear el redimencionamiento de la ventana para que el contenido no se muestre incorrectamente, ya que no es responsivo
        self.ventana.resizable(False, False)
        self.ventana.mainloop()

iniciar=Aplicacion()
