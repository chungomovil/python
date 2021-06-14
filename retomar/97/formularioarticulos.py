#Importamos librerias necesarias
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
import articulos
import sys

#Creamos la clase
class Mercado:

    #Creamos el metodo constructor
    def __init__(self):
        #Importamos la clase del modulo articulos
        self.conexion=articulos.Consulta()
        #Creamos la ventana
        self.ventana=tk.Tk()
        self.ventana.title("Mantenimiento de articulos")
        #Creamos el menu para salir del programa
        menubar=tk.Menu(self.ventana)
        self.ventana.configure(menu=menubar)
        opciones1=tk.Menu(menubar, tearoff=0)
        opciones1.add_command(label="SALIR", command=self.Salir)
        menubar.add_cascade(label="Opciones", menu=opciones1)
        #Creamos el notebook
        self.notebook=ttk.Notebook(self.ventana)
        self.notebook.grid(column=0, row=0, padx=10, pady=10)
        #Importamos los metodos que crean los distintos formularios
        self.FormularioCargaArticulo()
        self.FormularioConsultaCodigo()
        self.FormularioListadoCompleto()
        self.FormularioBorrarArticulo()
        self.FormularioModificarArticulo()
        #Parametros de la ventana
        self.ventana.minsize(600, 400)
        self.ventana.mainloop()

    #Metodo para crear el formulario de carga de articulos
    def FormularioCargaArticulo(self):
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
        self.etiqueta2.grid(column=0, row=1, padx=5, pady=10)
        self.dato2=tk.StringVar()
        self.entrada2=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato2)
        self.entrada2.grid(column=1, row=1, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe1, width=10, text="Confirmar", command=self.InsertarArticulo)
        self.boton1.grid(column=1, row=2, padx=5, pady=10)
    
    #Metodo para crear el formulario de consulta por codigo de articulo
    def FormularioConsultaCodigo(self):
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
        #Empleamos la funcion 'lambda' para poner pasar parametros a la funcion en cuestion
        self.boton2=ttk.Button(self.labelframe2, width=10, text="Confirmar", command=lambda: self.ConsultarCodigo(1))
        self.boton2.grid(column=1, row=3, padx=5, pady=10)

    #Creamos el metodo para listar todos los articulos
    def FormularioListadoCompleto(self):
        self.frame3=ttk.Frame(self.notebook)
        self.notebook.add(self.frame3, text="Listado completo")
        self.labelframe3=ttk.Labelframe(self.frame3, text="Articulo")
        self.labelframe3.grid(column=0, row=0, padx=10, pady=10)
        self.boton3=ttk.Button(self.labelframe3, width=20, text="Listado completo", command=self.ListarArticulos)
        self.boton3.grid(column=0, row=0, padx=10, pady=10)
        self.scrolledtext=st.ScrolledText(self.labelframe3, width=45, height=15)
        self.scrolledtext.grid(column=0, row=1, padx=10, pady=10)

    #Creamos el metodo para el formulario de borrado de articulo
    def FormularioBorrarArticulo(self):
        self.frame4=ttk.Frame(self.notebook)
        self.notebook.add(self.frame4, text="Borrado de articulos")
        self.labelframe4=ttk.Labelframe(self.frame4, text="Articulo")
        self.labelframe4.grid(column=0, row=0, padx=10, pady=10)
        self.etiqueta6=ttk.Label(self.labelframe4, text="Codigo:")
        self.etiqueta6.grid(column=0, row=0, padx=5, pady=10)
        self.dato6=tk.StringVar()
        self.entrada6=ttk.Entry(self.labelframe4, width=20, textvariable=self.dato6)
        self.entrada6.grid(column=1, row=0, padx=5, pady=10)
        self.boton4=ttk.Button(self.labelframe4, width=10, text="Borrar", command=self.BorrarArticulo)
        self.boton4.grid(column=1, row=1, padx=5, pady=10)

    #Creamos el metodo para el formulario de modificar articulo
    def FormularioModificarArticulo(self):
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
        #Llamamos a otra funcion lambda para pasar parametros en las funciones
        self.boton5=ttk.Button(self.labelframe5, width=10, text="Consultar", command=lambda: self.ConsultarCodigo(2))
        self.boton5.grid(column=1, row=3, padx=5, pady=10)
        self.boton6=ttk.Button(self.labelframe5, width=10, text="Modificar", command=self.ModificarArticulo)
        self.boton6.grid(column=1, row=4, padx=5, pady=10)

    #Metodo para insertar articulo en la BD
    def InsertarArticulo(self):
        #Cargamos datos del nuevo articulo desde el formulario
        descripcion=self.dato1.get()
        precio=self.dato2.get()
        if descripcion!="" and precio!="":
            #Interpretamos excepcion
            try:
                #Pasamos a flotante
                precio=round(float(precio), 2)
                #Llamamos al metodo respectivo del modulo 'articulos' para insertar los datos en la BD
                self.conexion.CrearArticulo(descripcion, precio)
                #Informamos al usuario de la operacion exitosa
                mb.showinfo("Informacion", "Articulo creado correctamente.")
            #Informamos al usuario del error en la entrada por teclado
            except ValueError:
                mb.showerror("ERROR", "Formato de precio incorrecto.")
        #Informamos al usuario si hay campos vacios
        else:
            mb.showerror("ERROR", "Algun campo esta vacio.")
    
    #Metodo para consultar por codigo de articulo en la BD
    #Este metodo tiene un parametro como entrada (el que le otorgara la funcion lambda)
    def ConsultarCodigo(self, num):
        #Si lambda pasa como parametro '1'
        if num==1:
            #Capturamos codigo del articulo desde el formulario
            codigo=self.dato3.get()
            if codigo!="":
                #Interpretamos excepcion
                try:
                    #Pasamos a entero y convertimos en tupla para la consulta en la BD
                    codigo=int(codigo)
                    codigo=(codigo, )
                    #Retornamos datos del articulo de la BD
                    articulo=self.conexion.ConsultarCodigo(codigo)
                    if articulo!=None:
                        #Descromprimimos lista
                        descripcion, precio= articulo[1], articulo[2]
                        #Asignamos nuevos datos a la variables de datos de los 'Entry'
                        self.dato4.set(descripcion)
                        self.dato5.set(precio)
                    else:
                        #Vaciamos variables de datos de los 'Entry'
                        self.dato4.set("")
                        self.dato5.set("")
                        #Informamos al usuario que el articulo no existe
                        mb.showinfo("Informacion", "El articulo solicitado no se encuentra.")
                #Informamos de error de entrada por teclado
                except ValueError:
                    mb.showerror("ERROR", "Formato de codigo incorrecto.")
            #Informamos que el campo esta vacio
            else:
                mb.showerror("ERROR", "El campo codigo esta vacio.")
        #Si lambda pasa como parametro '2'
        if num==2:
            #Este algoritmo es similar al anterior
            codigo=self.dato7.get()
            if codigo!="":
                try:
                    codigo=int(codigo)
                    codigo=(codigo, )
                    articulo=self.conexion.ConsultarCodigo(codigo)
                    if articulo!=None:
                        descripcion, precio=articulo[1], articulo[2]
                        self.dato8.set(descripcion)
                        self.dato9.set(precio)
                    else:
                        self.dato8.set("")
                        self.dato9.set("")
                        mb.showinfo("Informacion", "El articulo solicitado no se encuentra.")
                except ValueError:
                    mb.showerror("ERROR", "Formato de codigo incorrecto.")
            else:
                mb.showerror("ERROR", "El campo codigo esta vacio")

    #Metodo para listar todos los articulos de la BD
    def ListarArticulos(self):
        #Consulta para importar todos los articulos de la BD
        articulos=self.conexion.ListarArticulos()
        #Vaciamos el scrolledtext
        self.scrolledtext.delete(0.0, tk.END)
        #Creamos encabezado de la tabla
        encabezado=f"{'CODIGO':<15}{'DESCRIPCION':<20}{'PRECIO'}\n"
        #Insertamos en el scrolledtext el encabezado (SIEMPRE PARTIENDO DESDE EL FINAL)
        self.scrolledtext.insert(tk.END, encabezado)
        #Recorremos resultados de la consulta
        for codigo, descripcion, precio in articulos:
            #Formateamos cada linea 
            linea=f"{codigo:<15}{descripcion:<20}{precio}\n"
            #Insertamos en el scrolledtext siempre partiendo desde el final
            self.scrolledtext.insert(tk.END, linea)

    #Metodo para borrar articulo
    def BorrarArticulo(self):
        #Obtenemos codigo de articulo desde el formulario
        codigo=self.dato6.get()
        if codigo!="":
            #Interpretamos excepcion
            try:
                #Pasamos codigo a entero y lo convertimos en tupla para la BD
                codigo=int(codigo)
                codigo=(codigo, )
                #Consultamos que el articulo existe
                articulo=self.conexion.ConsultarCodigo(codigo)
                if articulo!=None:
                    descripcion=articulo[1]
                    #Informamos al usuario si lo desea eliminar realmente
                    respuesta=mb.askyesno("CUIDADO", f"Se eliminara el articulo '{descripcion}'")
                    #Si afirma lo eliminamos
                    if respuesta==True:
                        self.conexion.BorrarArticulo(codigo)
                #Informamos al usuario que el articulo no se ha encontrado
                else:
                    mb.showinfo("Informacion", "Articulo no encontrado.")
            #Informamos del error de entrada por teclado
            except ValueError:
                mb.showerror("ERROR", "Formato de codigo incorrecto")
        #Informamos de campos vacios
        else:
            mb.showerror("ERROR", "El campo codigo esta vacio.")

    #Metodo para modificar un articulo
    def ModificarArticulo(self):
        #Obtenemos los valores del formulario
        codigo=self.dato7.get()
        descripcion=self.dato8.get()
        precio=self.dato9.get()
        if codigo!="":
            #Interpretamos la exepcion
            try:
                #Pasamos a entero y convertimos en tupla el codigo
                codigo=int(codigo)
                codigo=(codigo, )
                if precio!="":
                    #Convertimos a flotante el precio
                    precio=round(float(precio), 2)
                #Extraemos los datos del articulo antes de ser modificado
                articulo=self.conexion.ConsultarCodigo(codigo)
                if articulo!=None:
                    #Creamos variables de respaldo con valores sin modificar
                    descripcion_antiguo, precio_antiguo=articulo[1], articulo[2]
                    #Si estan vacios los campos a modificar se rellenan con el valor antiguo
                    if descripcion=="":
                        descripcion=descripcion_antiguo
                    if precio=="":
                        precio=precio_antiguo
                    #Consulta para modificar articulo
                    self.conexion.ModificarArticulo(codigo, descripcion, precio)
                    #Informamos al usuario de la operacion exitosa
                    mb.showinfo("Informacion", f"Se ha modificado el articulo '{descripcion}'.")
                #Informamos al usuario que el articulo no se encuentra
                else:
                    mb.showerror("ERROR", "Articulo no encontrado.")
            #Informamos al usuario del error de entrada por teclado
            except ValueError:
                mb.showerror("ERROR", "Formato de valores incorrecto.")
        #Informamos al usuario que hay campos vacios
        else:
            mb.showerror("ERROR","El campo codigo esta vacio.")        

    #Metodo para salir                
    def Salir(self):
        sys.exit(0)

#Bloque principal y declaracion de objeto
iniciar=Mercado()
