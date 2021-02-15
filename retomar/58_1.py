"""
Disponer dos objetos de la clase Button con las etiquetas: "varón" y "mujer", al presionarse mostrar en la barra de títulos de la ventana la etiqueta del botón presionado.
"""

import tkinter as tk

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Elegir Sexo")
        self.bthombre=tk.Button(self.ventana1, text="Hombre", command=self.Hombre)
        self.bthombre.grid(column=0, row=0)
        self.btmujer=tk.Button(self.ventana1, text="Mujer", command=self.Mujer)
        self.btmujer.grid(column=0, row=1)
        self.ventana1.minsize(300, 100)
        self.ventana1.mainloop()    #NO OLVIDAR ESTA LINEA (si no la ventana no se mostrara)
    
    def Hombre(self):
        self.ventana1.title("Hombre")

    def Mujer(self):
        self.ventana1.title("Mujer")

iniciar=Aplicacion()