#Importar librerias
import tkinter as tk
from tkinter import ttk
import random
import sys
#Creamos la clase
class Aplicacion:

    #Metodo constructor del programa
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Eliminando figuras con 'Id' y 'Tag'")
        #Creamos menu
        menubar=tk.Menu(self.ventana)
        self.ventana.configure(menu=menubar)
        opciones1=tk.Menu(menubar, tearoff=0)
        opciones1.add_command(label="SALIR", command=self.Salir)
        menubar.add_cascade(label="Opciones", menu=opciones1)
        #Creamos labelframe para opciones de crear y borrar
        self.labelframe1=ttk.LabelFrame(self.ventana, text="CREAR")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10, sticky="we")
        self.labelframe2=ttk.LabelFrame(self.ventana, text="ELIMINAR")
        self.labelframe2.grid(column=0, row=1, padx=10, pady=10, sticky="we")
        #Creamos lienzo
        self.lienzo1=tk.Canvas(self.ventana, width=900, height=600, background="black")
        self.lienzo1.grid(column=0, row=2, pady=10)
        #Creamos las variables que usaremos posteriormente 
        self.eleccion=0
        self.pulsacion=False
        #Llamamos a los metodos troncales (captura de raton y creacion de contenido de labelframes)
        self.ControlesRaton()
        self.OpcionesCrear()
        self.OpcionesEliminar()
        #Caracteristicas de la ventana
        self.ventana.geometry("900x800")
        self.ventana.resizable(0, 0)
        self.ventana.mainloop()

    #(EXTRA) Metodo de creacion de botones del labelframe de dibujar figuras
    def OpcionesCrear(self):
        self.boton1=ttk.Button(self.labelframe1, width=20, text="Crear Linea", command=self.Linea_Crear)
        self.boton1.grid(column=0, row=0, padx=5, pady=10)
        self.boton2=ttk.Button(self.labelframe1, width=20, text="Crear Rectangulo", command=self.Rectangulo_Crear)
        self.boton2.grid(column=1, row=0, padx=5, pady=10)
        self.boton3=ttk.Button(self.labelframe1, width=20, text="Crear Cuadrado", command=self.Cuadrado_Crear)
        self.boton3.grid(column=2, row=0, padx=5, pady=10)
        self.boton4=ttk.Button(self.labelframe1, width=20, text="Crear Ovalo", command=self.Ovalo_Crear)
        self.boton4.grid(column=3, row=0, padx=5, pady=10)
    
    #Metodo de creacion de botones del labelframe de borrar figuras
    def OpcionesEliminar(self):
        self.boton5=ttk.Button(self.labelframe2, width=20, text="Borrar Linea (Tag)", command=self.Linea_Eliminar_Tag)
        self.boton5.grid(column=0, row=0, padx=5, pady=10)
        self.boton6=ttk.Button(self.labelframe2, width=20, text="Borrar Rectangulo", command=self.Rectangulo_Eliminar)
        self.boton6.grid(column=1, row=0, padx=5, pady=10)
        self.boton7=ttk.Button(self.labelframe2, width=20, text="Borrar Cuadrado", command=self.Cuadrado_Eliminar)
        self.boton7.grid(column=2, row=0, padx=5, pady=10)
        self.boton8=ttk.Button(self.labelframe2, width=20, text="Borrar Ovalo", command=self.Ovalo_Eliminar)
        self.boton8.grid(column=3, row=0, padx=5, pady=10)
        self.boton9=ttk.Button(self.labelframe2, width=20, text="BORRAR TODOS", command=self.Todos_Eliminar)
        self.boton9.grid(column=4, row=0, padx=5, pady=10)
        self.boton10=ttk.Button(self.labelframe2, width=20, text="Borrar Linea (Id)", command=self.Linea_Eliminar_Id)
        self.boton10.grid(column=5, row=0, padx=5, pady=10)

    #Metodo de creacion de eventos del raton
    def ControlesRaton(self):
        #Evento de captura cuando se pulsa click izquierdo
        self.lienzo1.bind("<Button-1>", self.Pulsar)
        #Evento de captura cuando se suelta click izquierdo
        self.lienzo1.bind("<ButtonRelease-1>", self.Soltar)
    
    #Metodo de captura del click izquierdo cuando se pulsa
    def Pulsar(self, evento):
        #Cambia pulsacion a true (recordar que la creamos en el constructor como False)
        self.pulsacion=True
        #Guarda posicion del click en el espacio
        self.posicionx=evento.x
        self.posiciony=evento.y
        #Ejecuta Metodo de dibujado de figuras
        self.Dibujar()
    
    #Metodo de captura de click izquierdo cuando se suelta
    def Soltar(self, evento):
        #Cambia pulsacion a false
        self.pulsacion=False

    #Metodo de generar numero aleatorio y lo retorna
    def Aleatorio(self):
        num=random.randint(10, 100)
        return num
    
    #Metodo captura de eleccion
    def Linea_Crear(self):
        self.eleccion=1
    
    #Metodo eliminar linea por id-->(nombre de variable)
    #TENER EN CUENTA QUE CON EL METODO POR ID SOLO SE ELIMINA 1 LINEA
    def Linea_Eliminar_Id(self):
        self.lienzo1.delete(self.linea)

    #Metodo eliminar lineas por tag
    def Linea_Eliminar_Tag(self):
        self.lienzo1.delete("linea")
    
    #Metodo captura de eleccion
    def Rectangulo_Crear(self):
        self.eleccion=2
    
    #Metodo eliminar rectangulos por tag
    def Rectangulo_Eliminar(self):
        self.lienzo1.delete("rectangulo")

    #Metodo captura de eleccion
    def Cuadrado_Crear(self):
        self.eleccion=3

    #Metodo eliminar cuadrados por ag
    def Cuadrado_Eliminar(self):
        self.lienzo1.delete("cuadrado")
    
    #Metodo captura de eleccion
    def Ovalo_Crear(self):
        self.eleccion=4

    #Metodo eliminar ovalos por tag
    def Ovalo_Eliminar(self):
        self.lienzo1.delete("ovalo")

    #Metodo eliminar todas las figuras del lienzo
    def Todos_Eliminar(self):
        self.lienzo1.delete(tk.ALL)

    #Metodo para dibujar las figuras
    def Dibujar(self):
        #Generamos numero aleatorio para las medidas de las figuras
        aleatorio=self.Aleatorio()
        #Si la pulsacion es True crea la figura seleccionada
        if self.pulsacion==True:
            #Analiza que figura crear segun la opcion seleccionada
            if self.eleccion==1:
                #Para eliminar por id hay que crear la figura y asignarle una variable, tambien se le puede poner el atributo 'tag'
                self.linea=self.lienzo1.create_line(self.posicionx-aleatorio, self.posiciony-aleatorio, self.posicionx+aleatorio, self.posiciony+aleatorio, fill="red", tag="linea")
            if self.eleccion==2:
                self.lienzo1.create_rectangle(self.posicionx-aleatorio, self.posiciony-aleatorio+aleatorio, self.posicionx+aleatorio+aleatorio, self.posiciony+aleatorio, fill="yellow", tag="rectangulo")
            if self.eleccion==3:
                self.lienzo1.create_rectangle(self.posicionx-aleatorio, self.posiciony-aleatorio, self.posicionx+aleatorio+50, self.posiciony+aleatorio+50, fill="orange", tag="cuadrado")
            if self.eleccion==4:
                self.lienzo1.create_oval(self.posicionx-aleatorio, self.posiciony-aleatorio, self.posicionx+aleatorio, self.posiciony+aleatorio, fill="green", tag="ovalo")

    #Metodo para salir
    def Salir(self):
        sys.exit(0)

#Bloque principal y creacion de obtejo
iniciar=Aplicacion()


