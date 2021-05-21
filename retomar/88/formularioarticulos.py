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
        opciones2.add_command(label="800x500", command=self.VentanaMediana)
        opciones2.add_command(label="1000x600", command=self.VentanGrande)
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
        self.CajaBorradoArticulo()
        self.CajaModificarArticulo()
        #Parametros de la ventana
        self.ventana.minsize(600, 400)
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
    
    #Metodo para crear el formulario de consulta por codigo
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

    #Metodo para crear el formulario que mostrar todos los articulos en un scrolledtext
    def CajaListadoCompleto(self):
        self.frame3=ttk.Frame(self.notebook)
        self.notebook.add(self.frame3, text="Listado completo")
        self.labelframe3=ttk.Labelframe(self.frame3, text="Articulo")
        self.labelframe3.grid(column=0, row=0, padx=10, pady=10)
        self.boton3=ttk.Button(self.labelframe3, width=20, text="Listado completo", command=self.OperacionesListadoCompleto)
        self.boton3.grid(column=0, row=0, padx=10, pady=10)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=40, height=15)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)

    #Metodo para crear formulario de borrado de articulo
    def CajaBorradoArticulo(self):
        self.frame4=ttk.Frame(self.notebook)
        self.notebook.add(self.frame4, text="Borrado de articulos")
        self.labelframe4=ttk.Labelframe(self.frame4, text="Articulo")
        self.labelframe4.grid(column=0, row=0, padx=10, pady=10)
        self.etiqueta6=ttk.Label(self.labelframe4, text="Codigo:")
        self.etiqueta6.grid(column=0, row=0, padx=5, pady=10)
        self.dato6=tk.StringVar()
        self.entrada6=ttk.Entry(self.labelframe4, width=20, textvariable=self.dato6)
        self.entrada6.grid(column=1, row=0, padx=5, pady=10)
        self.boton4=ttk.Button(self.labelframe4, width=15, text="Borrar", command=self.OperacionesBorradoArticulo)
        self.boton4.grid(column=1, row=1, padx=5, pady=10)

    #Metodo para crear formulario de modificacion de un articulo
    def CajaModificarArticulo(self):
        self.frame5=ttk.Frame(self.notebook)
        self.notebook.add(self.frame5, text="Modificar articulo")
        self.labelframe5=ttk.Labelframe(self.frame5, text="Articulo")
        self.labelframe5.grid(column=0, row=0, padx=10, pady=10)
        self.etiqueta7=ttk.Label(self.labelframe5, text="Codigo:")
        self.etiqueta7.grid(column=0, row=0, padx=5, pady=10)
        self.dato7=tk.StringVar()
        self.entrada7=ttk.Entry(self.labelframe5, width=20, textvariable=self.dato7)
        self.entrada7.grid(column=1, row=0, padx=5, pady=10)
        self.etiqueta8=ttk.Label(self.labelframe5, text="Descripcion:")
        self.etiqueta8.grid(column=0, row=1, padx=5, pady=10)
        self.dato8=tk.StringVar()
        self.entrada8=ttk.Entry(self.labelframe5, width=20, textvariable=self.dato8)
        self.entrada8.grid(column=1, row=1, padx=5, pady=10)
        self.etiqueta9=ttk.Label(self.labelframe5, text="Precio:")
        self.etiqueta9.grid(column=0, row=2, padx=5, pady=10)
        self.dato9=tk.StringVar()
        self.entrada9=ttk.Entry(self.labelframe5, width=20, textvariable=self.dato9)
        self.entrada9.grid(column=1, row=2, padx=5, pady=10)
        self.boton5=ttk.Button(self.labelframe5, width=15, text="Consultar", command=self.OperacionesConsultaCodigo_2)
        self.boton5.grid(column=1, row=3, padx=5, pady=10)
        self.boton6=ttk.Button(self.labelframe5, width=15, text="Modificar", command=self.OperacionesModificarArticulo)
        self.boton6.grid(column=1, row=4, padx=5, pady=10)

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
            codigo=(codigo, )
            #Lo consultamos en la base de datos
            articulo=self.conexion.ConsultarCodigo(codigo)
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
            articulo="\n"+(4-len(str(codigo)))*" "+str(codigo)+10*" "+descripcion+(19-len(descripcion))*" "+str(precio)
            self.scrolledtext1.insert(tk.END, articulo)

    #Metodo para borrar un articulo
    def OperacionesBorradoArticulo(self):
        #Algoritmo a procesar
        try:
            #Convertimos el codigo a entero y posteriormente a una tupla
            codigo=int(self.dato6.get())
            codigo=(codigo, )
            #Retornamos los datos del articulo en cuestion
            articulo=self.conexion.ConsultarCodigo(codigo)
            #Si el retorno no esta vacio
            if articulo!=None:
                #Mostramos al usuario una confirmacion para su eliminacion
                confirmacion=mb.askokcancel("CUIDADO","Se eliminara el articulo '"+articulo[0]+"'.")
                #Si confirma
                if confirmacion==True:
                    #Eliminamos articulo de la BD e informamos al usuario
                    self.conexion.BorrarArticulo(codigo)
                    mb.showinfo("AVISO", "El articulo ha sido eliminado.")
            #Si el retorno esta vacio informamos al usuario
            else:
                mb.showinfo("AVISO", "Articulo no encontrado.")
        #Procesamos la excepcion del codigo no entero e informamos al usuario
        except ValueError:
            mb.showerror("ERROR", "Formato de codigo incorrecto.")

    #Metodo para modificar un articulo
    def OperacionesModificarArticulo(self):
        descripcion=self.dato8.get()
        #Algoritmo a procesar
        try:
            #Comprobamos que el codigo y el precio esten en formato correcto
            codigo=int(self.dato7.get())
            precio=self.dato9.get()
            if precio!="":
                precio=float(precio)
                precio=round(precio, 2)
            #Consultamos antes de modificar
            articulo=self.conexion.ConsultarCodigo((codigo, ))
            #Si retorna algo
            if articulo!=None:
                #Importamos valores actuales antes de modificar (basicamente por si el usuario deja un campo vacio no se agregue)
                antigua_descripcion, antiguo_precio=articulo
                #Informamos si todos los campos son vacios, asi no modificamos
                if descripcion=="" and precio=="":
                    mb.showwarning("CUIDADO", "Para modificar el articulo se debe rellenar al menos un campo.")
                #Modificamos segun cual no este vacio
                else:
                    if descripcion=="":
                        descripcion=antigua_descripcion
                    if precio=="":
                        precio=antiguo_precio
                    #Conectamos con la BD para modificarlo
                    self.conexion.ModificarArticulo(codigo, descripcion, precio)
                    #Informamos al usuario de la modificacion
                    mb.showinfo("AVISO","Se ha modificado el articulo numero '"+str(codigo)+"'")
            #Si no se encuentra el articulo informamos al usuario
            else:
                mb.showinfo("AVISO", "Articulo no encontrado.")
        #Procesamos la excepcion de formado de entrada e informamos al usuario
        except ValueError:
            mb.showerror("ERROR", "Formato de datos incorrecto.")
    
    #Metodo para consultar por codigo de articulo, similar al metodo de buscar por codigo anterior
    def OperacionesConsultaCodigo_2(self):
        try:
            codigo=int(self.dato7.get())
            codigo=(codigo, )
            articulo=self.conexion.ConsultarCodigo(codigo)
            if articulo!=None:
                descripcion, precio=articulo
                self.dato8.set(descripcion)
                self.dato9.set(precio)
            else:
                mb.showinfo("AVISO", "Articulo no encontrado.")
        except ValueError:
            mb.showerror("ERROR","Formato de codigo incorrecto.")

    #Metodo para redimensionar la ventana 
    def VentanaMediana(self):
        self.ventana.geometry("800x500")
    
    #Metodo para redimensionar la ventana
    def VentanGrande(self):
        self.ventana.geometry("1000x600")

    #Metod para salir del programa
    def Salir(self):
        sys.exit(0)
        
#Bloque principal y declaracion de objeto
Iniciar=Aplicacion()


