"""
Disponer varios objetos de la clase Checkbutton con nombres de navegadores web. En el título de la ventana mostrar todos los nombres de navegadores seleccionados.
"""

import tkinter as tk

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Seleccionar navegadores:")
        self.etiqueta1=tk.Label(self.ventana, text="Seleccionar navegadores:", foreground="blue")
        self.etiqueta1.grid(column=0, row=0)
        self.valor1=tk.IntVar()
        self.nav1=tk.Checkbutton(self.ventana, text="Google Chrome", variable=self.valor1, command=self.Agregar)
        self.nav1.grid(column=0, row=1)
        self.valor2=tk.IntVar()
        self.nav2=tk.Checkbutton(self.ventana, text="Firefox", variable=self.valor2, command=self.Agregar)
        self.nav2.grid(column=0, row=2)
        self.valor3=tk.IntVar()
        self.nav3=tk.Checkbutton(self.ventana, text="Safari", variable=self.valor3, command=self.Agregar)
        self.nav3.grid(column=0, row=3)
        self.ventana.minsize(400, 200)
        self.ventana.mainloop()
    #AÑADIR EN FORMA DE TEXTO LOS NAVEGADORES SELECCIONADOS
    def Agregar(self):
        cadena=""
        if self.valor1.get()==1:
            cadena+="Google Chrome, "
        if self.valor2.get()==1:
            cadena+="Firefox, "
        if self.valor3.get()==1:
            cadena+="Safari"
        self.ventana.title(cadena)

Iniciar=Aplicacion()
