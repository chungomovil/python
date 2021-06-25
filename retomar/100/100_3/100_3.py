#Importamos librerias necesarias
import tkinter as tk
from tkinter import ttk
from urllib import request
import json

#Creamos la clase
class Buscador:

    #Creamos el metodo constructor
    def __init__(self):
        #Creamos la ventana
        self.ventana=tk.Tk()
        self.ventana.title("Navegador de articulos")
        #Creamos lo campos y botones
        self.etiqueta1=ttk.Label(self.ventana, text="Codigo:")
        self.etiqueta1.grid(column=0, row=0, padx=10, pady=10, columnspan=2, sticky="w")
        self.etiqueta2=ttk.Label(self.ventana, text="Descrpcion:")
        self.etiqueta2.grid(column=0, row=1, padx=10, pady=10, columnspan=2, sticky="w")
        self.etiqueta3=ttk.Label(self.ventana, text="Precio:")
        self.etiqueta3.grid(column=0, row=2, padx=10, pady=10, columnspan=2, sticky="w")
        self.etiqueta4=ttk.Label(self.ventana, text="", font=16)
        self.etiqueta4.grid(column=2, row=0, padx=10, pady=10, columnspan=2)
        self.etiqueta5=ttk.Label(self.ventana, text="", font=16)
        self.etiqueta5.grid(column=2, row=1, padx=10, pady=10, columnspan=2)
        self.etiqueta6=ttk.Label(self.ventana, text="", font=16)
        self.etiqueta6.grid(column=2, row=2, padx=10, pady=10, columnspan=2)
        #Posicion actual, sera empleada posteriormente
        self.posicion=0
        #Pasamos como parametro a la funcion la posicion inicial para que se inicie el programa mostrando un articulo
        self.Navegar(self.posicion)
        self.boton1=ttk.Button(self.ventana, width=25, text="Anterior", command=lambda: self.Navegar(self.posicion-1)) #Pasamos los parametros con lambda para ir recorriendo la lista de articulos
        self.boton1.grid(column=0, row=3, padx=10, pady=10, columnspan=2)
        self.boton2=ttk.Button(self.ventana, width=25, text="Siguiente", command=lambda: self.Navegar(self.posicion+1))
        self.boton2.grid(column=2, row=3, padx=10, pady=10, columnspan=2)
        #Parametro de la ventana
        self.ventana.mainloop()

    #Metodo para obtener los datos del archivo PHP y retornarlos en formato JSON
    def RetornarArticulos(self):
        #Hacemos la peticion http al servidor
        peticion=request.urlopen("http://web/retornararticulos.php")
        #Leemos la pagina web y la guardamos en una variable
        datos=peticion.read()
        #Codificamos el codigo fuente de la pagina
        datosutf8=datos.decode("utf-8")
        #Transformamos el codigo fuente a formato JSON
        datosjson=json.loads(datosutf8)
        #Retornamos
        return datosjson

    #Metodo para navegar por los articulos
    def Navegar(self, pos):
        #Llamamos al metodo anterior para obtener el conjunto de articulos en JSON
        datosjson=self.RetornarArticulos()
        #Cambiamos el valor a la posicion actual
        self.posicion=pos
        #Controlamos el desbordamiento
        if self.posicion>=len(datosjson) or self.posicion<=-len(datosjson):
            self.posicion=0
        #Mostramos la informacion del producto actual en las etiquetas
        self.etiqueta4.configure(text=datosjson[self.posicion]["codigo"])
        self.etiqueta5.configure(text=datosjson[self.posicion]["descripcion"])
        self.etiqueta6.configure(text=datosjson[self.posicion]["precio"])

#Bloque principal y creacion de objeto
iniciar=Buscador()

