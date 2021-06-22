#Importamos modulos necesarios
from tkinter import messagebox as mb

#Metodo para mostrar aviso de informacion
def MostrarInfo(mensaje):
    mb.showinfo("Informacion", mensaje)

#Metodo para mostrar aviso de error
def MostrarError(mensaje):
    mb.showerror("ERROR", mensaje)


