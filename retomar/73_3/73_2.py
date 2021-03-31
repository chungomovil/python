import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Practicando canvas")
        #Creamos labelframe1 para formulario de entrada de datos
        self.labelframe1=ttk.LabelFrame(self.ventana, text="Partidos politicos")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10, sticky="w")
        #Llamamos al metodo del formulario de entrada de datos
        self.Opciones()
        #Creamos lienzo para canvas
        self.lienzo1=tk.Canvas(self.ventana, width=800, height=600, background="black")
        self.lienzo1.grid(column=0, row=1, pady=10)
        self.ventana.geometry("800x600")
        self.ventana.resizable(0, 0)
        self.ventana.mainloop()
    
    #Creamos metodo para formulario de entrada de datos
    def Opciones(self):
        self.etiqueta1=ttk.Label(self.labelframe1, text="PP:")
        self.etiqueta1.grid(column=0, row=0, padx=10, pady=5)
        self.dato1=tk.StringVar()
        self.entrada1=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato1)
        self.entrada1.grid(column=1, row=0, padx=10, pady=5)
        self.etiqueta2=ttk.Label(self.labelframe1, text="PSOE:")
        self.etiqueta2.grid(column=0, row=1, padx=10, pady=5)
        self.dato2=tk.StringVar()
        self.entrada2=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato2)
        self.entrada2.grid(column=1, row=1, padx=10, pady=5)
        self.etiqueta3=ttk.Label(self.labelframe1, text="Podemos:")
        self.etiqueta3.grid(column=0, row=2, padx=10, pady=5)
        self.dato3=tk.StringVar()
        self.entrada3=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato3)
        self.entrada3.grid(column=1, row=2, padx=10, pady=5)
        self.boton1=ttk.Button(self.labelframe1, width=20, text="Generar grafico", command=self.GenerarGrafico)
        self.boton1.grid(column=0, row=3, columnspan=2, padx=10, pady=5, sticky="we")
    
    #Creamos metodo para generar graficos
    def GenerarGrafico(self):
        #Obtenemos datos de los campos de entrada de datos
        dato1=self.dato1.get()
        dato2=self.dato2.get()
        dato3=self.dato3.get()
        #Revisamos si alguno esta vacio para mostrar error
        if dato1=="" or dato2=="" or dato3=="":
            mb.showerror("ERROR", "Se deben rellenar todos los campos.")
        else:
            #Calculamos el porcentaje de las barras
            dato1=int(dato1)
            dato2=int(dato2)
            dato3=int(dato3)
            total=dato1+dato2+dato3
            porcentaje1=round((dato1/total*100), 2)
            porcentaje2=round((dato2/total*100), 2)
            porcentaje3=round((dato3/total*100), 2)
            barra1=porcentaje1*7
            barra2=porcentaje2*7
            barra3=porcentaje3*7
            #Limpiamos el lienzo
            self.lienzo1.delete(tk.ALL)
            #Creamos barras con sus textos en el interior
            self.lienzo1.create_rectangle(20, 80, barra1, 160, fill="blue")
            self.lienzo1.create_text(20+50, 120, text="PP\n"+str(porcentaje1)+"%", fill="white", font="Arial")
            self.lienzo1.create_rectangle(barra1, 80, barra1+barra2, 160, fill="red")
            self.lienzo1.create_text(barra1+50, 120, text="PSOE\n"+str(porcentaje2)+"%", fill="white", font="Arial")
            self.lienzo1.create_rectangle(barra1+barra2, 80, barra1+barra2+barra3, 160, fill="purple")
            self.lienzo1.create_text(barra1+barra2+50, 120, text="Podemos\n"+str(porcentaje3)+"%", fill="white", font="Arial")

#Bloque principal
iniciar=Aplicacion()


