#Importamos librerias necesarias
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
import sys
#Importamos nuestro propio modulo para la sintaxis sql
import articulos

#Creamos la clase
class FormularioArticulos:

    #Creamos el metodo constructor
    def __init__(self):
        #Creamos la ventana
        self.ventana=tk.Tk()
        self.ventana.title("MANTENIMIENTO DE ARTICULOS")
        #Creamos el menu con la opcion de salir
        menubar=tk.Menu(self.ventana)
        self.ventana.configure(menu=menubar)
        opciones1=tk.Menu(menubar, tearoff=0)
        opciones1.add_command(label="SALIR", command=self.Salir)
        menubar.add_cascade(label="Opciones", menu=opciones1)
        #Creamos el notebook para las opciones
        self.notebook=ttk.Notebook(self.ventana)
        self.notebook.grid(column=0, row=0, padx=10, pady=10)
        #Cargamos los distintos metodos
        self.CamposArticulo()
        self.CamposCodigo()
        self.CamposListado()
        self.CamposBorrado()
        self.CamposModificar()
        #Propiedades de la ventana
        self.ventana.minsize(570,320)
        self.ventana.mainloop()

    #Metodo para crear formulario de ingresar articulo nuevo
    def CamposArticulo(self):
        #Creamos el frame y lo acoplamos al notebook
        self.frame1=ttk.Frame(self.notebook)
        self.notebook.add(self.frame1, text="Carga de Articulos")
        #Creamos el labelframe contenedor
        self.labelframe1=tk.LabelFrame(self.frame1, text="Articulo")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)
        #Creamos los distintos campos para ingresar propiedades del articulo
        self.etiqueta1=ttk.Label(self.labelframe1, text="Descripcion:")
        self.etiqueta1.grid(column=0, row=0, padx=5, pady=10)
        self.dato1=tk.StringVar()
        self.entrada1=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato1)
        self.entrada1.grid(column=1, row=0, padx=5, pady=10)
        self.etiqueta2=ttk.Label(self.labelframe1, text="Precio:")
        self.etiqueta2.grid(column=0, row=1, padx=5, pady=10)
        self.dato2=tk.StringVar()
        self.entrada2=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato2)
        self.entrada2.grid(column=1, row=1, padx=5, pady=10)
        #Boton para cargar a la base de datos los datos del articulo
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", width=15, command=self.InsertarArticulo)
        self.boton1.grid(column=1, row=2, padx=5, pady=10)
    
    #Metodo para crear formulario de busqueda por codigo
    def CamposCodigo(self):
        #Agregamos el frame al notebook
        self.frame2=ttk.Frame(self.notebook)
        self.notebook.add(self.frame2, text="Consulta por codigo")
        #Creamos el labelframe contenedor
        self.labelframe2=tk.LabelFrame(self.frame2, text="Articulo")
        self.labelframe2.grid(column=0, row=0, padx=10, pady=10)
        #Creamos los campos del formulario para buscar y mostrar el articulo en cuestion
        self.etiqueta3=ttk.Label(self.labelframe2, text="Codigo:")
        self.etiqueta3.grid(column=0, row=0, padx=5, pady=10)
        self.dato3=tk.StringVar()
        self.entrada3=ttk.Entry(self.labelframe2, width=20, textvariable=self.dato3)
        self.entrada3.grid(column=1, row=0, padx=5, pady=10)
        self.etiqueta4=ttk.Label(self.labelframe2, text="Descripcion:")
        self.etiqueta4.grid(column=0, row=1, padx=5, pady=10)
        self.dato4=tk.StringVar()
        self.entrada4=ttk.Entry(self.labelframe2, width=20, textvariable=self.dato4, state="readonly") #Lo ponemos en readonly para que solo sea posible editar el campo 'codigo'
        self.entrada4.grid(column=1, row=1, padx=5, pady=10)
        self.etiqueta5=ttk.Label(self.labelframe2, text="Precio:")
        self.etiqueta5.grid(column=0, row=2, padx=5, pady=10)
        self.dato5=tk.StringVar()
        self.entrada5=ttk.Entry(self.labelframe2, width=20, textvariable=self.dato5, state="readonly")
        self.entrada5.grid(column=1, row=2, padx=5, pady=10)
        #Boton para buscar por codigo
        self.boton2=ttk.Button(self.labelframe2, text="Consultar", width=10, command=self.BuscarCodigo)
        self.boton2.grid(column=1, row=3, padx=10, pady=10)

    #Metodo para crear el scrolledtext donde se mostraran todos los productos
    def CamposListado(self):
        #Agregamos un nuevo frame al notebook
        self.frame3=ttk.Frame(self.notebook)
        self.notebook.add(self.frame3, text="Listado Completo")
        #Creamos el labelframe contenedor
        self.labelframe3=tk.LabelFrame(self.frame3, text="Articulo")
        self.labelframe3.grid(column=0, row=0, padx=10, pady=10)
        #Boton para ingresar todo los articulos
        self.boton3=ttk.Button(self.labelframe3, text="Listado completo", width=20, command=self.MostrarTodo)
        self.boton3.grid(column=0, row=0, padx=5, pady=10)
        #Scrolledtext donde se ingresaran los articulos
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=35, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=5, pady=10)

    #Metodo para crear el formulario para borrar articulos
    def CamposBorrado(self):
        #Agreamos un nuevo frame al notebook
        self.frame4=ttk.Frame(self.notebook)
        self.notebook.add(self.frame4, text="Borrado de articulos")
        #Creamos el labelframe contenedor
        self.labelframe4=tk.LabelFrame(self.frame4, text="Articulo")
        self.labelframe4.grid(column=0, row=0, padx=10, pady=10)
        #Creamos los campos del formulario
        self.etiqueta6=ttk.Label(self.labelframe4, text="Codigo:")
        self.etiqueta6.grid(column=0, row=0, padx=5, pady=10)
        self.dato6=tk.StringVar()
        self.entrada6=ttk.Entry(self.labelframe4, width=20, textvariable=self.dato6)
        self.entrada6.grid(column=1, row=0, padx=5, pady=10)
        #Boton para borrar el articulo
        self.boton4=ttk.Button(self.labelframe4, width=10, text="Borrar", command=self.BorrarArticulo)
        self.boton4.grid(column=1, row=1, padx=5, pady=10)

    #Metodo para crear el formulario de modificar articulos
    def CamposModificar(self):
        #Agregamos un nuevo frame al notebook
        self.frame5=ttk.Frame(self.notebook)
        self.notebook.add(self.frame5, text="Modificar articulo")
        #Creamos el labelframe contenedor
        self.labelframe5=tk.LabelFrame(self.frame5, text="Articulo")
        self.labelframe5.grid(column=0, row=0, padx=10, pady=10)
        #Creamos los campos del formulario
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
        #Creamos los botones para modificar y consultar articulos
        self.boton5=ttk.Button(self.labelframe5, width=10, text="Consultar", command=self.ConsultarArticulo)
        self.boton5.grid(column=1, row=3, padx=5, pady=10)
        self.boton6=ttk.Button(self.labelframe5, width=10, text="Modificar", command=self.ModificarArticulo)
        self.boton6.grid(column=1, row=4, padx=5, pady=10)

    #Metodo para insertar un nuevo articulo en la BD
    def InsertarArticulo(self):
        #Obtenemos los datos del formulario
        descripcion=self.dato1.get()
        precio=float(self.dato2.get())
        #Los introducimos en la base de datos
        articulos.Insertar(descripcion, precio)
        #Mostramos mensaje de confirmacion
        mb.showinfo("Informacion", "Articulo agregado correctamente.")

    #Metodo para buscar por codigo en la BD
    def BuscarCodigo(self):
        #Obtenemos los datos del formulario (OJO: Hay que transformarlo en una tupla para que la base de datos lo interprete bien en la clausula 'WHERE')
        codigo=(self.dato3.get(), )
        #Retornamos el codigo que hemos buscado
        producto=articulos.Buscar(codigo)
        if len(producto)>0:
            #Fijamos nuevos valores a la variable de texto correspondiente de cada Entry
            self.dato4.set(producto[0][1])
            self.dato5.set(producto[0][2])
        #Mostramos error si el codigo del articulo no existe
        else:
            mb.showerror("ERROR", "El articulo no existe.")
    
    #Metodo para mostrar todos los articulos de la BD
    def MostrarTodo(self):
        #Vaciamos el scrolledtext
        self.scrolledtext1.delete(1.0, tk.END)
        #Recortamos todos los articulos
        Totalidad_Productos=articulos.Totalidad()
        #(EXTRA)Creamos encabezado para la tabla
        encabezado="Codigo"+" "*5+"Descripcion"+" "*5+"Precio"+"\n"
        self.scrolledtext1.insert(1.0, encabezado)
        #Recorremos los datos devueltos para insertarlos en el scrolledtext
        for codigo, nombre, precio in Totalidad_Productos:
            #(EXTRA)Formateamos datos para que se alineen en las colunmas correctamente
            producto=str(codigo)+" "*(11-len(str(codigo)))+str(nombre)+" "*(16-len(nombre))+str(precio)+"\n"
            #Insertamos articulos en el scrolledtext (OJO: partimos desde 'tk.END' para que se muestras en orden, de lo contrario se mostrarian a la inversa)
            self.scrolledtext1.insert(tk.END, producto)

    #Metodo para borrar articulos
    def BorrarArticulo(self):
        #Obtenemos el codigo del articulo y lo pasamos a una tupla para sql
        codigo=(self.dato6.get(), )
        #Retornamos los datos del articulo eliminado
        articulo=articulos.Borrar(codigo)
        #Mostramos los mensajes de confirmacion
        if len(articulo)>0:
            mb.showinfo("Informacion", "Se ha eliminado correctamente el articulo: '"+str(articulo[0][1])+"'.")
        else:
            mb.showerror("ERROR", "El articulo no existe.")

    #Metodo para modificar articulos
    def ModificarArticulo(self):
        #Obtenemos los datos del articulo
        codigo=self.dato7.get()
        descripcion=self.dato8.get()
        precio=self.dato9.get()
        #Mostramos mensajes de confirmacion
        if codigo=="":
            mb.showerror("ERROR", "El campo 'codigo' esta vacio.")
        else:
            articulo=articulos.Modificar(codigo, descripcion, precio)
            if len(articulo)>0:
                mb.showinfo("Informacion", "Se ha modificado correctamente el articulo: '"+str(articulo[0][1])+"'.")
            else:
                mb.showerror("ERROR", "El articulo no existe.")

    #Metodo para consultar articulo por su codigo
    def ConsultarArticulo(self):
        #Obtenemos el codigo del articulo y lo pasamos a una tupla para sql
        codigo=(self.dato7.get(), )
        #Obtenemos datos del articulo
        articulo=articulos.Buscar(codigo)
        #Insertamos datos en las variables de texto los distintos entry
        if len(articulo)>0:
            self.dato8.set(articulo[0][1])
            self.dato9.set(articulo[0][2])
        #Mostramos mensajes de confirmacion
        else:
            mb.showerror("ERROR", "El articulo no existe.")

    #Metodo para salir del programa
    def Salir(self):
        sys.exit()

#Bloque principal y creamos de objeto
iniciar=FormularioArticulos()
