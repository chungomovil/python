#Importamos librerias necesarias
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
import sys
import articulos

#Creamos la clase
class Aplicacion:

    #Creamos el metodo constructor
    def __init__(self):
        #Declaramos el modulo para la conexion con la base de datos
        self.conexion=articulos.BaseDatos()
        #Creamos la ventana
        self.ventana=tk.Tk()
        self.ventana.title("Mantenimiento de articulos")
        #Creamos el menu de opciones
        menubar=tk.Menu()
        self.ventana.configure(menu=menubar)
        opciones1=tk.Menu(tearoff=0)
        opciones2=tk.Menu(tearoff=0)
        opciones2.add_command(label="600x500", command=self.VentanaMediana)
        opciones2.add_command(label="800x600", command=self.VentanGrande)
        opciones1.add_cascade(label="Dimensiones", menu=opciones2)
        opciones1.add_separator()
        opciones1.add_command(label="SALIR", command=self.Salir)
        menubar.add_cascade(label="Opciones", menu=opciones1)
        #Creamos el notebook
        self.notebook=ttk.Notebook(self.ventana)
        self.notebook.grid(column=0, row=0, padx=10, pady=10)
        #Cargamos los metodos que crear los distintos formularios
        self.CajaCargaArticulo()
        self.CajaConsultaCodigo()
        self.CajaListadoCompleto()
        #Parametros de la ventana
        self.ventana.minsize(400, 400)
        self.ventana.mainloop()
    
    #Metodo para crear el formulario de carga de articulo nuevo
    def CajaCargaArticulo(self):
        self.frame1=ttk.Frame(self.notebook)
        self.notebook.add(self.frame1, text="Carga de articulos")
        self.labelframe1=ttk.Labelframe(self.frame1, text="Articulo")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)
        self.etiqueta1=ttk.Label(self.labelframe1, text="Descripcion:")
        self.etiqueta1.grid(column=0, row=0, padx=5, pady=10)
        self.dato1=tk.StringVar()
        self.entrada1=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato1)
        self.entrada1.grid(column=1, row=0, padx=5, pady=10)
        self.etiqueta2=ttk.Label(self.labelframe1, text="Precio:")
        self.etiqueta2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entrada2=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato2)
        self.entrada2.grid(column=1, row=1, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe1, width=15, text="Confirmar", command=self.OperacionesCargaArticulo)
        self.boton1.grid(column=1, row=2, padx=5, pady=10)
    
    #Metodo para consultar articulo por codigo
    def CajaConsultaCodigo(self):
        self.frame2=ttk.Frame(self.notebook)
        self.notebook.add(self.frame2, text="Consulta por codigo")
        self.labelframe2=ttk.Labelframe(self.frame2, text="Articulo")
        self.labelframe2.grid(column=0, row=0, padx=10, pady=10)
        self.etiqueta3=ttk.Label(self.labelframe2, text="Codigo:")
        self.etiqueta3.grid(column=0, row=0, padx=5, pady=10)
        self.dato3=tk.StringVar()
        self.entrada3=ttk.Entry(self.labelframe2, width=20, textvariable=self.dato3)
        self.entrada3.grid(column=1, row=0, padx=5, pady=10)
        self.etiqueta4=ttk.Label(self.labelframe2, text="Descripcion:")
        self.etiqueta4.grid(column=0, row=1, padx=5, pady=10)
        self.dato4=tk.StringVar()
        self.entrada4=ttk.Entry(self.labelframe2, width=20, textvariable=self.dato4, state="readonly")
        self.entrada4.grid(column=1, row=1, padx=5, pady=10)
        self.etiqueta5=ttk.Label(self.labelframe2, text="Precio:")
        self.etiqueta5.grid(column=0, row=2, padx=5, pady=10)
        self.dato5=tk.StringVar()
        self.entrada5=ttk.Entry(self.labelframe2, width=20, textvariable=self.dato5, state="readonly")
        self.entrada5.grid(column=1, row=2, padx=5, pady=10)
        self.boton2=ttk.Button(self.labelframe2, width=15, text="Consultar", command=self.OperacionesConsultaCodigo)
        self.boton2.grid(column=1, row=3, padx=5, pady=10)

    #Metodo para mostrar todos los articulos en un scrolledtext
    def CajaListadoCompleto(self):
        self.frame3=ttk.Frame(self.notebook)
        self.notebook.add(self.frame3, text="Listado completo")
        self.labelframe3=ttk.Labelframe(self.frame3, text="Articulo")
        self.labelframe3.grid(column=0, row=0, padx=10, pady=10)
        self.boton3=ttk.Button(self.labelframe3, width=20, text="Listado completo", command=self.OperacionesListadoCompleto)
        self.boton3.grid(column=0, row=0, padx=10, pady=10)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=40, height=15)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)

    #Metodo de operaciones para crear un nuevo articulo en la BD
    def OperacionesCargaArticulo(self):
        #Capturamos descripcion del articulo
        descripcion=self.dato1.get()
        #Pasamos por un try el algoritmo para controlar valores flotantes
        try:
            #Capturamos el precio de articulo y lo pasamos a flotante
            precio=float(self.dato2.get())
            precio=round(precio, 2)
            #Enviamos datos a la base de datos para ingresarlos
            self.conexion.CrearArticulo(descripcion, precio)
            #Informamos al usuario sobre la operacion
            mb.showinfo("AVISO","El articulo '"+descripcion+"' se ha creado correctamente.")
        #Procesamos la excepcion en caso que se inserte string en el precio
        except ValueError:
            #Informamos al usuario del error
            mb.showerror("ERROR", "Formato de precio incorrecto.")

    #Metodo de operaciones para consultar articulo en la BD
    def OperacionesConsultaCodigo(self):
        #Pasamos el algoritmo por un try para controlar que el codigo sea entero
        try:
            #Transformamos el codigo a entero
            codigo=int(self.dato3.get())
            #Lo consultamos en la base de datos
            articulo=self.conexion.ConsultarCodigo((codigo, ))
            #Controlamos que exista el articulo con dicho codigo
            if articulo!=None:
                #Agregamos a los entrys los nuevos valores
                descripcion, precio=articulo
                self.dato4.set(descripcion)
                self.dato5.set(precio)
            #Si el articulo no existe informamos al usuario
            else:
                mb.showinfo("AVISO", "Articulo no encontrado.")
        #Controlamos la excepcion si el codigo no es entero
        except ValueError:
            #Informamos al usuario
            mb.showerror("ERROR","Formato de codigo incorrecto.")
    
    #Metodo para listar todos los productos de la BD
    def OperacionesListadoCompleto(self):
        #Retornamos todos los productos de la BD
        listado=self.conexion.ArticulosTotal()
        #Vaciamos scrolledtext
        self.scrolledtext1.delete(1.0, tk.END)
        #Creamos el encabezado de la tabla  y lo insertamos SIEMPRE empezando por el FINAL
        encabezado="CODIGO"+7*" "+"DESCRIPCION"+7*" "+"PRECIO"
        self.scrolledtext1.insert(tk.END, encabezado)
        #Recorremos el listado de productos y los insertamos SIEMPRE empezando por el FINAL
        for codigo, descripcion, precio in listado:
            articulo="\n"+2*" "+str(codigo)+10*" "+descripcion+(19-len(descripcion))*" "+str(precio)
            self.scrolledtext1.insert(tk.END, articulo)

    #Metodo para redimensionar la ventana 
    def VentanaMediana(self):
        self.ventana.geometry("600x500")
    
    #Metodo para redimensionar la ventana
    def VentanGrande(self):
        self.ventana.geometry("800x600")

    #Metod para salir del programa
    def Salir(self):
        sys.exit(0)
        
#Bloque principal y declaracion de objeto
Iniciar=Aplicacion()


