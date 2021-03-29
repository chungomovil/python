import tkinter as tk
from tkinter import ttk

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Practicando Canvas tipo Arc")
        #Creamos labelframe para introducir datos
        self.labelframe1=ttk.LabelFrame(self.ventana, text="Partidos politicos")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10, sticky="w")
        #Llamamos al metodo para crear los campos del formulario de datos
        self.Opciones()
        #Creamos el lienzo de dibujo
        self.lienzo1=tk.Canvas(self.ventana, width="800", height="600", background="black")
        self.lienzo1.grid(column=0, row=1, pady=10)
        self.ventana.geometry("800x600")
        self.ventana.resizable(0, 0)
        self.ventana.mainloop()

    #Metodo para crear campos de formulario de datos
    def Opciones(self):
        self.etiqueta1=ttk.Label(self.labelframe1, text="PP")
        self.etiqueta1.grid(column=0, row=0, padx=10, pady=5)
        self.dato1=tk.StringVar()
        self.entrada1=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato1)
        self.entrada1.grid(column=1, row=0, padx=10, pady=5)
        self.etiqueta2=ttk.Label(self.labelframe1, text="PSOE")
        self.etiqueta2.grid(column=0, row=1, padx=10, pady=5)
        self.dato2=tk.StringVar()
        self.entrada2=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato2)
        self.entrada2.grid(column=1, row=1, padx=10, pady=5)
        self.etiqueta3=ttk.Label(self.labelframe1, text="Podemos")
        self.etiqueta3.grid(column=0, row=2, padx=10, pady=5)
        self.dato3=tk.StringVar()
        self.entrada3=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato3)
        self.entrada3.grid(column=1, row=2, padx=10, pady=5)
        self.boton1=ttk.Button(self.labelframe1, width=20, text="Generar grafico", command=self.GenerarGrafico)
        self.boton1.grid(column=0, row=3, columnspan=2, padx=10, pady=5, sticky="we")
    
    #Metodo para dibujar grafico en el lienzo
    def GenerarGrafico(self):
        #Limpiamos el area del lienzo
        self.lienzo1.delete(tk.ALL)
        #Obtenemos datos de formulario
        dato1=int(self.dato1.get())
        dato2=int(self.dato2.get())
        dato3=int(self.dato3.get())
        #Algoritmo para calcular el porcentaje de cada trozo
        suma=dato1+dato2+dato3
        final1=dato1/suma*360
        final2=dato2/suma*360
        final3=dato3/suma*360
        #Creamos los trozos en el lienzo
        self.lienzo1.create_arc(50, 50, 500, 400, fill="blue", start=0, extent=final1)
        self.lienzo1.create_arc(50, 50, 500, 400, fill="red", start=final1, extent=final2)
        self.lienzo1.create_arc(50, 50, 500, 400, fill="purple", start=final1+final2, extent=final3)
        #Textos aclaratorios de los trozos
        self.lienzo1.create_text(650, 100, text="PP: "+str(dato1)+" votos", font="Arial", fill="white")
        self.lienzo1.create_text(650,150, text="PSOE: "+str(dato2)+" votos", font="Arial", fill="white")
        self.lienzo1.create_text(650, 200, text="Podemos: "+str(dato3)+" votos", font="Arial", fill="white")

#Bloque principal
iniciar=Aplicacion()


