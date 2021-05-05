import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
import articulos

class FormularioArticulos:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("MANTENIMIENTO DE ARTICULOS")
        self.notebook=ttk.Notebook(self.ventana)
        self.notebook.grid(column=0, row=0, padx=10, pady=10)
        self.CamposArticulo()
        self.CamposCodigo()
        self.CamposListado()
        self.ventana.mainloop()

    def CamposArticulo(self):
        self.frame1=ttk.Frame(self.notebook)
        self.notebook.add(self.frame1, text="Carga de Articulos")
        self.labelframe1=tk.LabelFrame(self.frame1, text="Articulo")
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
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", width=15, command=self.InsertarArticulo)
        self.boton1.grid(column=1, row=2, padx=5, pady=10)
    
    def CamposCodigo(self):
        self.frame2=ttk.Frame(self.notebook)
        self.notebook.add(self.frame2, text="Consulta por codigo")
        self.labelframe2=tk.LabelFrame(self.frame2, text="Articulo")
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
        self.boton2=ttk.Button(self.labelframe2, text="Consultar", width=10, command=self.BuscarCodigo)
        self.boton2.grid(column=1, row=3, padx=10, pady=10)

    def CamposListado(self):
        self.frame3=ttk.Frame(self.notebook)
        self.notebook.add(self.frame3, text="Listado Completo")
        self.labelframe3=tk.LabelFrame(self.frame3, text="Articulo")
        self.labelframe3.grid(column=0, row=0, padx=10, pady=10)
        self.boton3=ttk.Button(self.labelframe3, text="Listado completo", width=20)
        self.boton3.grid(column=0, row=0, padx=5, pady=10)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=35, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=5, pady=10)

    def InsertarArticulo(self):
        descripcion=self.dato1.get()
        precio=float(self.dato2.get())
        articulos.Insertar(descripcion, precio)
        mb.showinfo("Informacion", "Articulo agregado correctamente.")

    def BuscarCodigo(self):
        codigo=(self.dato3.get(), )
        producto=articulos.Buscar(codigo)
        if len(producto)>0:
            self.dato4.set(producto[0][1])
            self.dato5.set(producto[0][2])
        else:
            mb.showerror("ERROR", "El articulo no existe.")

iniciar=FormularioArticulos()

