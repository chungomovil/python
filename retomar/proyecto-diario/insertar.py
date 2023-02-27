#<---Version 1.0---> Posible actualizacion para crear copias del documento de claves anterior
#Modulos necesarios
import os
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb

#Creamos la clase
class Aplicacion:

    ruta=os.path.dirname(__file__)+"/almacen.txt"

    #Metodo constructor
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("INSERTAR")
        self.etiqueta=ttk.Label(self.ventana, text="AGREGAR CLAVES", font=("Arial", 14))
        self.etiqueta.grid(column=0, row=0, padx=10, pady=10)
        self.nuevalinea=ttk.Entry(self.ventana, font=("Arial", 10))
        self.nuevalinea.grid(column=0, row=1, padx=10, pady=10, sticky="we")
        self.nuevalinea.bind("<Return>", self.Desencadenar)
        self.nuevalinea.focus_set()
        self.scrolledtext=st.ScrolledText(self.ventana, width=200, height=30)
        self.scrolledtext.grid(column=0, row=2, padx=10, pady=10)
        self.ventana.columnconfigure(0, weight=1) #Para expandirlo hasta los bordes de la ventana
        self.ventana.geometry("1000x600")
        #Buscamos si existe el documento antes de hacer operaciones en el
        try:
            lineas=self.RescatarDatos()
            self.estado=1
        except:
            self.estado=0
            mb.showerror(title="ERROR", message="Poner el documento de claves en la carpeta del programa")
        self.ventana.mainloop()

    #Metodo para iniciar los demas procesos
    def Desencadenar(self, event):
        if self.estado==1:
            lineas=self.RescatarDatos()
            self.AgregarLinea(lineas)
            self.nuevalinea.delete(0, tk.END)
            self.MostrarDocumentoFinal()
        else:
            mb.showerror(title="ERROR", message="Poner el documento de claves en la carpeta del programa")

    #Metodo para obtener los datos del documento de claves
    def RescatarDatos(self):
        archivo=open(Aplicacion.ruta, "r+")
        lineas=archivo.readlines()
        archivo.close()
        return lineas

    #Metodo para agregar datos al documento de claves
    def AgregarLinea(self, lineas):
        lineasmod=self.QuitarVacias(lineas)
        lineasmod.append(self.nuevalinea.get()+"\n")
        archivo=open(Aplicacion.ruta, "w")
        archivo.writelines(lineasmod)
        archivo.close()

    #Metodo para mostrar el resultado final del documento de claves en el scrolledtext
    def MostrarDocumentoFinal(self):
        lineas=self.RescatarDatos()
        self.scrolledtext.delete(1.0, tk.END)
        for x in range(len(lineas)):
            self.scrolledtext.insert(tk.END, lineas[x])

    #Metodo para quitar las lineas vacias al final del documento de claves
    def QuitarVacias(self, lineas):
        x=0
        while x<len(lineas):
            if lineas[x]=="\n":
                lineas.pop(x)
            else:
                x+=1
        return lineas

#Bucle principal
inicio=Aplicacion()
