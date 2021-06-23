#Importamos paquetes y modulos necesarios
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
from urllib import request
from urllib import error

#Creamos la clase
class Lector:

    #Creamos el metodo constructor
    def __init__(self):
        #Creamos la ventana
        self.ventana=tk.Tk()
        self.ventana.title("Lector de paginas web")
        #Creamos el formulario para insertar la url
        self.etiqueta=ttk.Label(self.ventana, text="Ingrese URL del sitio web:", font=("Arial", 16))
        self.etiqueta.grid(column=0, row=0, padx=10, pady=20)
        self.dato=tk.StringVar()
        self.entrada=ttk.Entry(self.ventana, width=70, textvariable=self.dato)
        self.entrada.grid(column=0, row=1, padx=10, pady=10)
        self.boton=ttk.Button(self.ventana, width=20, text="LEER WEB", command=self.MostrarURL)
        self.boton.grid(column=0, row=2, padx=10, pady=10)
        #Creamos el scrolledtext
        self.areatexto=st.ScrolledText(self.ventana, width=100, height=40)
        self.areatexto.grid(column=0, row=3, padx=10, pady=40)
        #Parametros de la ventana
        self.ventana.resizable(False, False)
        self.ventana.mainloop()
    
    #Metodo para analizar la url
    def ObtenerURL(self):
        #Capturamos los datos que ha ingresado el usuario por teclado
        entrada_usuario=self.dato.get().lower()
        datos=""
        #Algoritmo a intentar
        try:
            #Hacemos la peticion a la url
            peticion=request.urlopen(entrada_usuario)
            #La leemos y la codificamos
            datos=peticion.read().decode("utf-8")
        #Excepcion si el error esta dentro de una url existente
        except error.HTTPError as err:
            respuesta=err.code
            mb.showerror("ERROR",f"El servidor dice: error {respuesta}")
        #Excepcion si el error se trata de una url no existente
        except error.URLError as err:
            respuesta=err.reason
            mb.showerror("ERROR",f"{respuesta}: La direccion web no existe")
        #Si se trata de otra excepcion
        except:
            mb.showerror("ERROR","Formato de URL incorrecto.")
        #Devolvemos
        finally:
            return datos

    #Metodo para mostrar contenido en scrolledtext
    def MostrarURL(self):
        #Llamamos al metodo de obtener url
        datos=self.ObtenerURL()
        if datos!="":
            #Borramos y escribimos en el scrolledtext
            self.areatexto.delete(1.0, tk.END)
            self.areatexto.insert(1.0, datos)

#Bloque principal y creacion de objeto
ejecutar=Lector()
