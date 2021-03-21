import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import sys

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Sumatorio de valores")
        #Creamos LabelFrame
        self.labelframe1=ttk.LabelFrame(self.ventana, text="Suma de numeros")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)
        #Importamos menu
        self.Menu()
        #Importamos elementos del LabelFrame
        self.Elementos()
        #Cerramos el bucle de la ventana
        self.ventana.mainloop()

    #Creamos elementos de LabelFrame
    def Elementos(self):
        self.etiqueta1=ttk.Label(self.labelframe1, text="Ingrese primer valor:")
        self.etiqueta1.grid(column=0, row=0, padx=10, pady=10)
        self.dato1=tk.StringVar()
        self.entrada1=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato1)
        self.entrada1.grid(column=1, row=0, padx=10, pady=10)
        self.etiqueta2=ttk.Label(self.labelframe1, text="Ingrese segundo valor:")
        self.etiqueta2.grid(column=0, row=1, padx=10, pady=10)
        self.dato2=tk.StringVar()
        self.entrada2=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato2)
        self.entrada2.grid(column=1, row=1, padx=10, pady=10)
        self.boton1=ttk.Button(self.labelframe1, width=20, text="SUMAR", command=self.Sumar)
        self.boton1.grid(column=1, row=2, padx=10, pady=20)

    #Funcion para sumar valores
    def Sumar(self):
        num1=self.dato1.get()
        num2=self.dato2.get()
        #Muestra mensaje de error si alguno esta vacio
        if num1=="" or num2=="":
            mb.showerror("ERROR","Ambos campos deben contener valores")
        #Sumar valores
        else:
            suma=int(num1)+int(num2)
            #Hay que pasarlos nuevamente a string para que no lo interprete mal al intentar concatenarlos
            self.ventana.title("Suma: "+str(num1)+" + "+str(num2)+" = "+str(suma))
    
    #Crear elementos del menu
    def Menu(self):
        menubar=tk.Menu()
        self.ventana.configure(menu=menubar)
        opciones1=tk.Menu(tearoff=0)
        opciones1.add_command(label="Acerca de...", command=self.Acerca)
        opciones1.add_command(label="Salir", command=self.Salir)
        menubar.add_cascade(label="Opciones", menu=opciones1)

    #Funcion para mostrar informacion del programa
    def Acerca(self):
        mb.showinfo("Informacion del programa","Creado para aprender a usar las ventanas de mensajes con tkinter.")

    #Funcion para cerrar el programa
    def Salir(self):
        sys.exit(0)

#Bloque principal
iniciar=Aplicacion()
