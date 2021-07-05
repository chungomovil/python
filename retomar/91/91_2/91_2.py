#Importamos modulos necesarios
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import random

#Creamos la clase
class Aplicacion:
    
    #Creamos metodo constructor
    def __init__(self):
        #Creamos la ventana
        self.ventana=tk.Tk()
        self.ventana.title("LABERINTO")
        #Asignamos variables que usaremos posteriormente
        self.Estado=False
        self.controlador=True
        #Creamos la lista que almacenara las casillas
        self.Casillas=[]
        #Llamamos al metodo que construye el laberinto
        self.CrearTablero()
        #Creamos los botones de resetear y recorrer laberinto
        self.boton1=ttk.Button(self.ventana, width=15, text="Recorrer", command=self.AnalizarRecorrido)
        self.boton1.grid(column=0, row=11, padx=10, pady=10, columnspan=5)
        self.boton2=ttk.Button(self.ventana, width=15, text="Generar otro", command=self.VaciarTablero)
        self.boton2.grid(column=5, row=11, padx=10, pady=10, columnspan=5)
        #Parametro de la ventana
        self.ventana.mainloop()
    
    #Metodo para construir el tablero del laberinto
    def CrearTablero(self):
        #Creamos el primer bucle
        for x in range(10):
            #Creamos una lista por cada fila de casillas
            linea=[]
            #Creamos el conjunto de casillas
            for columna in range(10):
                #Creamos la casilla con un valor aleatorio
                etiqueta=ttk.Label(self.ventana, text=self.Aleatorizar(), foreground="blue")
                etiqueta.grid(column=columna, row=x, padx=10, pady=10)
                #Agregamos la etiqueta a la lista de su propia linea
                linea.append(etiqueta)
            #Agregamos la linea al conjunto de casillas del tablero
            self.Casillas.append(linea)
        #Establecemos el valor fijo de la primera y la ultima casilla
        self.Casillas[0][0].configure(text="0")
        self.Casillas[9][9].configure(text="5")

    def Aleatorizar(self):
        num=random.randint(0, 2)
        if num==1:
            return 1
        else:
            return 0

    #Metodo para resetear el tablero
    def VaciarTablero(self):
        #Recorremos todas las casillas
        for x in range(len(self.Casillas)):
            #Recorremos las filas
            for i in range(len(self.Casillas[x])):
                #En lugar de eliminarla, generamos otros valor aleatorio a la casilla anterior
                self.Casillas[x][i].configure(text=self.Aleatorizar(), background="white")
        #Establecemos el valor fijo de la primera y la ultima casilla
        self.Casillas[0][0].configure(text="0")
        self.Casillas[9][9].configure(text="5")
        self.controlador=True

    #Metodo que analiza el recorrido del laberinto
    def AnalizarRecorrido(self):
        #Controlar para que no se muestren avisos erroneos al pulsar varias veces sobre el boton "Recorrer" sin darle antes al boton "Generar otro"
        if self.controlador!=False:
            #Reiniciamos el estado de la variable que indica si ha encontrado o no la salida
            self.Estado=False
            #Lanzamos el metodo que recorre el laberinto con la posicion inicial
            self.Recorrer(0, 0)
            #Si se encuentra la salida informamos al usuario
            if self.Estado==True:
                mb.showinfo("AVISO", "El laberinto tiene salida.")
            #En caso contrario lo informamos nuevamente
            else:
                mb.showwarning("AVISO", "El laberinto NO tiene salida.")
        #si el usuario pulsa varias veces el boton "Recorrer" y no el boton "Generar otro", se muestra un mensaje de error
        else:
            mb.showerror("ERROR", "Reinicie el tablero.")
        #Reestablecemos el estado del controlador para la siguiente ejecucion
        self.controlador=False

    #Metodo para recorrer las casillas del laberinto
    #Se recibe la fila y la columna definidas en el metodo anterior (se empieza por la columna 0 fila 0)
    def Recorrer(self, fila, columna):
        #Condiciones para entrar en recursividad (OJO: la variable 'self.Estado' debe ser global para que la recursividad la tenga en cuenta en todas sus iteraciones)
        if columna>=0 and columna<10 and fila>=0 and fila<10 and self.Estado==False:
            #Obtenemos numero de la casilla actual
            casilla=str(self.Casillas[fila][columna].cget("text"))
            #Si es 5 rompemos las iteraciones (RECORDAR) aun asi se procede a liberar la memoria de instancias anteriores
            if casilla=="5":
                self.Estado=True
            #Bucle alternativo
            else:
                #Si la casilla es 0 se modifica su valor como 9
                if casilla=="0":
                    self.Casillas[fila][columna].configure(text="9", background="yellow")
                    #Una vez posicionados en esta casilla (ahora con valor de 9) buscara que la siguiente casilla sea 0 en las 4 direcciones siguientes
                    #<--RECURSIVIDAD-->
                    self.Recorrer(fila, columna+1)
                    self.Recorrer(fila+1, columna)
                    self.Recorrer(fila, columna-1)
                    self.Recorrer(fila-1, columna)

#Bloque principal y declaracion de objeto
iniciar=Aplicacion()
