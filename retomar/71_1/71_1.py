import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import random

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Ejemplo de Spinbox")
        self.etiqueta1=ttk.Label(self.ventana, text="Seleccione la cantidad de bultos:")
        self.etiqueta1.grid(column=0, row=0, padx=5, pady=10)
        #Definimos el spinbox con valores comprendidos entre 0 y 20
        self.spinbox1=ttk.Spinbox(self.ventana, width=10, from_=0, to=20, state="readonly") #Se pone en readonly para que el usuario solo pueda darle a las flechas
        self.spinbox1.set(0) #Establecemos valor por defecto
        self.spinbox1.grid(column=1, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.ventana, width=10, text="Sortear", command=self.Sortear)
        self.boton1.grid(column=0, row=1, padx=5)
        self.etiqueta2=ttk.Label(self.ventana)
        self.etiqueta2.grid(column=1, row=1, padx=5)
        self.ventana.mainloop()

    #Creamos metodo para calcular aleatoriamente si se debe revisar o no
    def Sortear(self):
        aleatorio=random.randint(1,3)
        bultos=int(self.spinbox1.get())
        if bultos==0:
            mb.showerror("ERROR","La cantidad de bultos debe ser superior a 0.")
        else:
            if aleatorio!=1:
                self.etiqueta2.configure(text="No se revisa", background="green")
            else:
                self.etiqueta2.configure(text="Se debe revisar", background="red")

#Bloque principal
iniciar=Aplicacion()



