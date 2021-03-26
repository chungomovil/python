import tkinter as tk
from tkinter import ttk

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Practicando Canvas tipo Rectangle")
        #Creamos labelframe de entrada de datos
        self.labelframe1=ttk.LabelFrame(self.ventana, text="Partidos Politicos")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10, sticky="w")
        #Llamamos al metodo que crea campos para la entrada de datos
        self.EntradaDatos()
        #Creamos el lienzo para las formas
        self.lienzo1=tk.Canvas(self.ventana, width=800, height=600, background="black")
        self.lienzo1.grid(column=0, row=1, pady=10)
        self.ventana.geometry("800x600")
        self.ventana.resizable(0, 0)
        self.ventana.mainloop()

    #Metodo para crear campos de entrada de datos
    def EntradaDatos(self):
        self.etiqueta1=ttk.Label(self.labelframe1, text="PP:")
        self.etiqueta1.grid(column=0, row=0, padx=10, pady=5, sticky="w")
        self.dato1=tk.StringVar()
        self.entrada1=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato1)
        self.entrada1.grid(column=1, row=0, padx=10, pady=5)
        self.etiqueta2=ttk.Label(self.labelframe1, text="PSOE:")
        self.etiqueta2.grid(column=0, row=1, padx=10, pady=5, sticky="w")
        self.dato2=tk.StringVar()
        self.entrada2=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato2)
        self.entrada2.grid(column=1, row=1, padx=10, pady=5)
        self.etiqueta3=ttk.Label(self.labelframe1, text="Podemos:")
        self.etiqueta3.grid(column=0, row=2, padx=10, pady=5, sticky="w")
        self.dato3=tk.StringVar()
        self.entrada3=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato3)
        self.entrada3.grid(column=1, row=2, padx=10, pady=5)
        self.boton1=ttk.Button(self.labelframe1, width=20, text="Generar Grafico", command=self.Grafico)
        self.boton1.grid(column=0, row=3, columnspan=2, padx=10, pady=5, sticky="we")

    #Metodo para generar las graficas
    def Grafico(self):
        #Limpiamos todo el lienzo
        self.lienzo1.delete(tk.ALL)
        #Recibimos datos introducidos para calcular cual es el mayor
        dato1=int(self.dato1.get())
        dato2=int(self.dato2.get())
        dato3=int(self.dato3.get())
        if dato1>=dato2 and dato1>=dato3:
            mayor=dato1
        else:
            if dato2>=dato3:
                mayor=dato2
            else:
                mayor=dato3
        #Calculamos el porcentaje de la longitud de las barras respecto a la mayor de todas
        largo1=dato1/mayor*600
        largo2=dato2/mayor*600
        largo3=dato3/mayor*600
        #Creamos las barras con sus textos respectivos
        self.lienzo1.create_rectangle(10, 10, 10+largo1, 40, fill="red")
        self.lienzo1.create_text(60+largo1, 25, text="PP", fill="white", font="Arial")
        self.lienzo1.create_rectangle(10, 60, 10+largo2, 90, fill="green")
        self.lienzo1.create_text(60+largo2, 75, text="PSOE", fill="white", font="Arial")
        self.lienzo1.create_rectangle(10, 110, 10+largo3, 140, fill="blue")
        self.lienzo1.create_text(60+largo3, 125, text="Podemos" ,fill="white", font="Arial")

#Bloque principal
iniciar=Aplicacion()