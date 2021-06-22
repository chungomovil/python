#Importamos modulos necesarios
import tkinter as tk
from tkinter import ttk
#Importamos los modulos que estan en el subdirectorio
import formularios.login as login
import formularios.mensaje as mensaje

#Creamos la clase
class Aplicacion():

    #Creamos el metodo constructor
    def __init__(self):
        #Creamos la ventana
        self.ventana=tk.Tk()
        self.ventana.title("ELEGIR OPCION")
        #Creamos los botones para llamar a los distintos modulos
        self.boton1=ttk.Button(self.ventana, width=30, text="Abrir Login", command=self.Validar)
        self.boton1.grid(column=0, row=0, padx=10, pady=10)
        self.boton2=ttk.Button(self.ventana, width=30, text="Mostrar Mensaje", command=self.MostrarMensaje)
        self.boton2.grid(column=0, row=1, padx=10, pady=10)
        self.ventana.mainloop()

    #Metodo para llamar al modulo de login
    def Validar(self):
        #Llamamos a la funcion que crea el objeto
        login.Mostrar()
    
    #Metodo para llamar al modulo que muestra mensajes
    def MostrarMensaje(self):
        mensaje.MostrarInfo("Esta es una forma de llamar a modulos desde archivos python.")
    
#Bloque principal y declaracion de objeto
iniciar=Aplicacion()
