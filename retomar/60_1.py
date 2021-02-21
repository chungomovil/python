"""
Disponer tres controles de tipo Radiobutton con las etiquetas 'Rojo', 'Verde' y 'Azul'. Cuando se presione un botón cambiar el color de fondo del formulario.
Si consideramos que la variable ventana1 es un objeto de la clase Tk, luego si queremos que el fondo sea de color rojo debemos llamar al método configure y en el parámetro bg indicar un string con el color a activar ("red", "green" o "blue"):
"""

import tkinter as tk

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Cambiar color")
        self.valor=tk.IntVar()
        self.color1=tk.Radiobutton(self.ventana, text="Rojo", variable=self.valor, value=1)
        self.color1.grid(column=0, row=0)
        self.color2=tk.Radiobutton(self.ventana, text="Verde", variable=self.valor, value=2)
        self.color2.grid(column=0, row=1)
        self.color3=tk.Radiobutton(self.ventana, text="Azul", variable=self.valor, value=3)
        self.color3.grid(column=0, row=2)
        self.boton1=tk.Button(self.ventana, text="Cambiar color", command=self.CambiarColor)
        self.boton1.grid(column=0, row=3)
        self.ventana.resizable(False, False)
        self.ventana.minsize(400, 200)
        self.ventana.mainloop()

    #Metodo cambiar color
    def CambiarColor(self):
        color=int(self.valor.get())
        if color==1:
            self.ventana.configure(bg="red")
            self.ventana.title("COLOR ROJO")
        elif color==2:
            self.ventana.configure(bg="green")
            self.ventana.title("COLOR VERDE")
        else:   #No hace falta hacer un elif color==3 debido a que no hay mas opciones
            self.ventana.configure(bg="blue")
            self.ventana.title("COLOR AZUL")

iniciar=Aplicacion()
