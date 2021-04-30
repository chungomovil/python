#Importamos librerias necesarias
import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import sys

#Creamos la clase
class Aplicacion:

    #Creamos el metodo constructor
    def __init__(self):
        #Creamos la ventana
        self.ventana=tk.Tk()
        self.ventana.title("Guardar y abrir archivos en modo grafico")
        #Agregamos el menu
        self.Menu()
        #Creamos el scrolledtext para escribir el texto
        self.scrolledtext1=st.ScrolledText(self.ventana, width=100, height=30)
        self.scrolledtext1.grid(column=0, row=0)
        #Parametros de la ventana
        self.ventana.mainloop()
        
    #Metodo que crea el menu con sus opciones
    def Menu(self):
        menubar=tk.Menu(self.ventana)
        self.ventana.configure(menu=menubar)
        opciones1=tk.Menu(menubar, tearoff=0)
        opciones1.add_command(label="Abrir", command=self.Abrir)
        opciones1.add_command(label="Guardar", command=self.Guardar)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.Salir)
        menubar.add_cascade(label="Opciones", menu=opciones1)

    #Metodo para guardar el archivo en formato .txt
    def Guardar(self):
        #Abrimos el dialogo para guardar el archivo
        nombre_archivo=fd.asksaveasfilename(initialdir="/", title="Guardar como...", filetypes=((".txt", "*.txt"), ("Todos los archivos", "*.*")))
        #Si el nombre esta en blanco no continua
        if nombre_archivo!="":
            #(EXTRA) Controlamos agregar al final la extension .txt en caso de no existir
            extension=nombre_archivo[len(nombre_archivo)-4:]
            if extension!=".txt":
                nombre_archivo+=".txt"
            #Creamos el archivo que vamos a guardar
            archivo=open(nombre_archivo, "w", encoding="utf-8")
            archivo.write(self.scrolledtext1.get(1.0, tk.END))
            #Liberamos el archivo
            archivo.close()
            #Mostramos mensaje de confirmacion
            mb.showinfo("Mensaje", "El archivo se ha guardado correctamente.")

    #Metodo para cargar el archivo
    def Abrir(self):
        #Abrimos el dialogo para cargar el archivo
        nombre_archivo=fd.askopenfilename(initialdir="/", title="Abrir...", filetypes=((".txt", "*.txt"), ("Todos los arhivos", "*.*")))
        #Si el nombre esta en blanco no continua
        if nombre_archivo!="":
            #Abrimos el archivo en modo lectura
            archivo=open(nombre_archivo, "r", encoding="utf-8")
            #Leemos todo el archivo
            contenido=archivo.read()
            #Borramos cualquier contenido existente en el scrolledtext
            self.scrolledtext1.delete(1.0, tk.END)
            #Agregamos el contenido leido al scrolledtext
            self.scrolledtext1.insert(1.0, contenido)
            #Mostramos mensaje de confirmacion
            mb.showinfo("Mensaje", "Se ha importado el contenido correctamente.")

    #Metodo para salir
    def Salir(self):
        sys.exit(0)

#Bloque principal y declaracion de objeto
iniciar=Aplicacion()