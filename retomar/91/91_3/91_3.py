#Importamos librerias necesarias
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import random
import os
import sys

#Obtenemos la ruta de la imagen de la bomba
ruta=os.path.dirname(__file__)
ruta_bomba_imagen=os.path.join(ruta, "./imagenes/bomba.png")

#Creamos la clase
class Buscaminas:

    #Creamos el metodo constructor
    def __init__(self):
        #Creamos la ventana
        self.ventana=tk.Tk()
        self.ventana.title("BUSCAMINAS")
        #Creamos el menu
        menu=tk.Menu(self.ventana)
        #Damos color de fondo a la ventana
        self.ventana.configure(bg="#14A9A4", menu=menu)
        #Creamos las opciones del menu
        opciones=tk.Menu(menu, tearoff=0)
        #Opcion para reiniciar el tablero
        opciones.add_command(label="Reiniciar", command=self.Reiniciar)
        #Opcion para salir del programa
        opciones.add_command(label="Salir", command=self.Salir)
        #Agregamos las opciones al menu
        menu.add_cascade(label="Opciones", menu=opciones)
        #Creamos las listas que serán usadas posteriormente
        self.listacasillas=[]
        self.listabombas=[]
        self.destapadas=[]
        #Creamos la variable que almacenará las bombas cercanas
        self.bombacerca=0
        #Esta variable indica si estamos jugando o hemos perdido
        self.jugando=True
        #Almacenamos la imagen de la bomba
        self.bomba_imagen=tk.PhotoImage(file=ruta_bomba_imagen)
        #Redimensionamos la imagen de la bomba
        self.bomba_imagen=self.bomba_imagen.subsample(20)
        #Llamamos a los métodos principales
        self.ColocarBombas()
        self.CrearCasillas()
        #Tamaño de la ventana
        self.ventana.geometry("700x700")
        #No se podrá cambiar el tamaño
        self.ventana.resizable(False, False)
        #Bucle de la ventana
        self.ventana.mainloop()
 
    #Método para crear el tablero
    def CrearCasillas(self):
        #Bucle para crear las 100 casillas
        for z in range(10):
            fila=[]
            for i in range(10):
                #La función lamba debe almacenar en dos variables las posiciones, para que se envíen correctamente en cada iteración
                #De si enviamos directamente 'z' e 'i' se enviara siempre el ultimo valor de la iteracion
                casilla=ttk.Button(self.ventana, command=lambda fila=z, columna=i: self.SeleccionCasilla(fila, columna))
                #Posicionamos los botones con el administrador de diseño 'place' para que se le pueda dar el alto y ancho correctamente
                casilla.place(x=i*70, y=z*70, width=70, height=70)
                fila.append(casilla)
            #Las agregamos todas a la lista principal de casillas
            self.listacasillas.append(fila)

    #Método para colocar las bombas
    def ColocarBombas(self):
        total_bombas=0
        #Creamos un bucle para colocar 10 bombas
        while total_bombas<10:
            similitud=0
            #Creamos la bomba en una fila y columna aleatoria
            bomba_fila=random.randint(0, 9)
            bomba_columna=random.randint(0, 9)
            #Controlamos que no se repita la misma ubicación
            for x in range(len(self.listabombas)):
                if bomba_fila==self.listabombas[x][0] and bomba_columna==self.listabombas[x][1]:
                    similitud+=1
            #Agregamos ubicación de la bomba a la lista principal de bombas
            if similitud==0:
                self.listabombas.append([bomba_fila, bomba_columna])
                total_bombas+=1

    #Método que informa si pisamos una bomba
    def PisarBomba(self, fila, columna):
        similitud=0
        #Analiza si en nuestra posición hay una bomba
        for x in range (len(self.listabombas)):
            if fila==self.listabombas[x][0] and columna==self.listabombas[x][1]:
                similitud+=1
        #Devuelve el resultado
        if similitud>0:
            return True
        else:
            return False
    
    #Mótodo que informa las casillas que ya han sido destapadas
    def AnalizarDestapadas(self, fila, columna):
        similitud=0
        #Verificamos si la casilla ha sido destapada
        for x in range(len(self.destapadas)):
            if fila==self.destapadas[x][0] and columna==self.destapadas[x][1]:
                similitud+=1
        #Retornamos el resultado
        if similitud>0:
            return True
        else:
            return False

    #Método que elimina la casilla
    def EliminarCasilla(self, fila, columna):
        #Eliminamos gráficamente el botón (no elimina el valor del array)
        self.listacasillas[fila][columna].destroy()
        #Establecemos el valor 'None' en la lista principal de casillas para saber que ha sido eliminada
        #Se puede hacer de esta forma ya que al eliminarla gráficamente no elimina el valor del array
        self.listacasillas[fila][columna]=None

    #Método que analiza todo lo relacionado con la casilla que clickeamos
    #Recibe la fila y la columna por medio de lamba
    def SeleccionCasilla(self, fila, columna):
        #Verificamos que no hemos pisado una bomba nada más clickear
        inicial=self.PisarBomba(fila, columna)
        #Analizamos que aun no hayamos perdido
        #Si hemos perdido no dejará pulsar más casillas
        if self.jugando:
            #En caso de SI haber pisado una bomba
            if inicial==True:
                #Mostramos la imagen de la bomba en la casilla seleccionada
                self.listacasillas[fila][columna].configure(image=self.bomba_imagen, compound="center") #El atributo 'compound' sirve para alinear la imagen en el espacio del botón
                #Establecemos 'jugando' como False, es decir, hemos perdido
                self.jugando=False
                #Revelamos la ubicación de todas las bombas
                self.RevelarBombas()
                #Mostramos un aviso de que el jugador ha perdido
                mb.showwarning("DERROTA","LO SIENTO. ¡HAS PISADO UNA BOOOMBA!")
            #En caso de NO pisar bomba
            else:
                #Llamamos al método recursivo que analiza el tablero
                self.AnalizarTablero(fila, columna)
            #Si hay 90 o más destapadas
            if len(self.destapadas)>=90:
                #Ponemos 'jugando' en False, es decir, hemos ganado
                self.jugando=False
                #Informamos al jugador de que ha ganado
                mb.showinfo("FELICIDADES","¡FELICIDADES, HAS GANADO!")

    #Método recursivo para analizar las 8 casillas circundantes
    #En la primera iteración se calcularía la central de todas ellas
    def AnalizarAlrededor(self, fila, columna, limite=False):
        #Controlamos que no se salga de los límites del tablero
        if fila>=0 and fila<10 and columna>=0 and columna<10:
            #Verificamos si en la casilla hay una bomba
            bomba=self.PisarBomba(fila, columna)
            #Si es True incrementamos en 1 el valor global de la bomba
            if bomba==True:
                #OJO: Al ser recursivo se crearán diversas instancias con el mismo valor y se sumarán al terminar la recursividad
                self.bombacerca+=1
            #Controlamos que solo se calcula 1 casilla alrededor, de lo contrario seguirá hasta los bordes del tablero
            if limite!=True:
                #Analizamos todas las direcciones
                self.AnalizarAlrededor(fila-1, columna-1, True)
                self.AnalizarAlrededor(fila-1, columna, True)
                self.AnalizarAlrededor(fila-1, columna+1, True)
                self.AnalizarAlrededor(fila, columna+1, True)
                self.AnalizarAlrededor(fila+1, columna+1, True)
                self.AnalizarAlrededor(fila+1, columna, True)
                self.AnalizarAlrededor(fila+1, columna-1, True)
                self.AnalizarAlrededor(fila, columna-1, True)
    
    #Método recursivo para analizar todas las casillas del tablero que tengan 0 y sean contiguas
    def AnalizarTablero(self, fila, columna):
        #Controlamos que no se desborde
        if fila>=0 and fila<10 and columna>=0 and columna<10:
            #Almacenamos las que han sido ya destapadas
            destapada=self.AnalizarDestapadas(fila, columna)
            #Si NO esta destapada
            if destapada==False:
                #La agregamos a la lista
                self.destapadas.append([fila, columna])
                #Llamamos al método recursivo anterior para capturar cuantas bombas hay alrededor de la casilla actual
                self.AnalizarAlrededor(fila, columna)
                #Mostramos cuantas bombas hay alrededor de la casilla actual
                self.listacasillas[fila][columna].configure(text=self.bombacerca)
                #Si no hay bombas, en caso de no haber se rompe la recursividad en este punto
                #De esta forma solo calcularán los '0' que esten unos junto a otros
                if self.bombacerca==0:
                    #Eliminamos la casilla
                    self.EliminarCasilla(fila, columna)
                    #Recorremos en todas las direcciones para seguir calculando
                    self.AnalizarTablero(fila-1, columna-1)
                    self.AnalizarTablero(fila-1, columna)
                    self.AnalizarTablero(fila-1, columna+1)
                    self.AnalizarTablero(fila, columna+1)
                    self.AnalizarTablero(fila+1, columna+1)
                    self.AnalizarTablero(fila+1, columna)
                    self.AnalizarTablero(fila+1, columna-1)
                    self.AnalizarTablero(fila, columna-1)
        #Reseteamos la variable global de las bombas
        self.bombacerca=0

    #Método para reiniciar el tablero
    def Reiniciar(self):
        #Llamamos al método que limpia de casillas el tablero, así eliminamos los conflictos al reiniciar el tablero
        self.LimpiarTablero()
        #Vaciamos las listas globales
        self.listacasillas.clear()
        self.listabombas.clear()
        self.destapadas.clear()
        #Establecemos 'jugando' como True para que nos deje pulsar casillas nuevamente
        self.jugando=True
        #Llamamos a los método principales para que se ejecuten nuevamente y creen el nuevo tablero
        self.CrearCasillas()
        self.ColocarBombas()

    #Método para limpiar el tablero
    #OJO: Necesitamos limpiar todas las casillas gráficamente ya que si no lo hacemos se quedarán y al reiniciar el tablero creará anomalías debido a que no se encontrarán en la lista pero estarán gráficamente
    def LimpiarTablero(self):
        #Recorremos la lista global de las casillas
        for x in range(len(self.listacasillas)):
            for i in range(len(self.listacasillas[x])):
                #Verificamos que no ha sido ya eliminada
                if self.listacasillas[x][i]!=None:
                    #La destruímos
                    self.listacasillas[x][i].destroy()
                    #Le cambiamos el valor a 'None'
                    self.listacasillas[x][i]=None
    
    #Método para revelar la posición de todas las bombas
    def RevelarBombas(self):
        #Recorremos la lista principal de bombas
        for x in range(len(self.listabombas)):
            #Capturamos la fila y columna de la bomba
            fila=self.listabombas[x][0]
            columna=self.listabombas[x][1]
            #La mostramos en el tablero
            self.listacasillas[fila][columna].configure(image=self.bomba_imagen)

    #Método para cerrar el programa
    def Salir(self):
        sys.exit(0)

#Bloque principal y creación de objeto
#Esta forma es similar a crear el objeto directamente, la diferencia es que se ejecuta solo si estamos ejecutándola desde este mismo archivo, ya que es el "__main__"
if __name__=="__main__":
    ejecutar=Buscaminas()
