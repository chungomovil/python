import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Practicando Scrolledtext")
        self.etiqueta1=ttk.Label(self.ventana, text="Texto Fuente", foreground="blue")
        self.etiqueta1.grid(column=0, row=0, padx=20, pady=10)
        #Creamos los scrolledtext
        self.scrolledtext1=st.ScrolledText(self.ventana, width=30, height=15)
        self.scrolledtext1.grid(column=0, row=1)
        self.etiqueta2=ttk.Label(self.ventana, text="Texto Copiado", foreground="red")
        self.etiqueta2.grid(column=0, row=3)
        #Iniciamos el metodo del labelframe de opciones
        self.Opciones()
        self.scrolledtext2=st.ScrolledText(self.ventana, width=30, height=15)
        self.scrolledtext2.grid(column=0, row=4, padx=20, pady=10)
        self.ventana.minsize(600, 500)
        self.ventana.mainloop()

    #Metodo del labelframe de opciones de copiado
    def Opciones(self):
        self.labelframe1=ttk.LabelFrame(self.ventana, text="Region")
        self.labelframe1.grid(column=0, row=2, padx=20, pady=10, sticky="w") #El sticky en este caso actua como un text-align
        self.etiqueta3=ttk.Label(self.labelframe1, text="Fila Inicial:")
        self.etiqueta3.grid(column=0, row=0, padx=10, pady=5, sticky="e")
        self.dato1=tk.StringVar()
        self.entrada1=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato1)
        self.entrada1.grid(column=1, row=0, padx=10, pady=5)
        self.etiqueta4=ttk.Label(self.labelframe1, text="Columna Inicial:")
        self.etiqueta4.grid(column=0, row=1, padx=10, pady=5, sticky="e")
        self.dato2=tk.StringVar()
        self.entrada2=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato2)
        self.entrada2.grid(column=1, row=1, padx=10, pady=5)
        self.etiqueta5=ttk.Label(self.labelframe1, text="Fila Final:")
        self.etiqueta5.grid(column=0, row=2, padx=10, pady=5, sticky="e")
        self.dato3=tk.StringVar()
        self.entrada3=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato3)
        self.entrada3.grid(column=1, row=2, padx=10, pady=5)
        self.etiqueta6=ttk.Label(self.labelframe1, text="Columna Final:")
        self.etiqueta6.grid(column=0, row=3, padx=10, pady=5, sticky="e")
        self.dato4=tk.StringVar()
        self.entrada4=ttk.Entry(self.labelframe1, width=20, textvariable=self.dato4)
        self.entrada4.grid(column=1, row=3, padx=10, pady=5)
        self.boton1=ttk.Button(self.labelframe1, width=20, text="Copiar", command=self.Copiar)
        self.boton1.grid(column=1, row=4, padx=10, pady=5)

    #Creamos el metodo para copiar de un scrolledtext a otro
    def Copiar(self):
        dato1=self.dato1.get()
        dato2=self.dato2.get()
        dato3=self.dato3.get()
        dato4=self.dato4.get()
        contenido=self.scrolledtext1.get(dato1+"."+dato2, dato3+"."+dato4) #Importamos rangos elegidos en el scrolledtext principal
        self.scrolledtext2.delete(1.0, tk.END) #Eliminamos todos los datos del scrolledtext objetivo
        self.scrolledtext2.insert(1.0, contenido) #Copiamos el contenido obtenido del scrolledtext principal al objetivo

#Bloque principal
iniciar=Aplicacion()
