import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import random
import sys

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Dia del Orgullo")
        self.ventana.geometry("400x300")
        self.EtiquetasPrincipales()
        self.EtiquetasLGTB()
        self.EtiquetaPersonasTotales()
        self.MostrarErroresEmergentes()
        self.Salir()
        self.ventana.mainloop()
    
    def EtiquetasPrincipales(self):
        self.etiqueta1=ttk.Label(self.ventana, text="Feliz", anchor="center", font=("Arial", 26), foreground="Green")
        self.etiqueta1.grid(column=0, row=0, padx=10, pady=50)
        self.Retardo(500)
        self.etiqueta2=ttk.Label(self.ventana, text="Día", anchor="center", font=("Arial", 26), foreground="Pink")
        self.etiqueta2.grid(column=1, row=0, padx=10, pady=50)
        self.Retardo(500)
        self.etiqueta3=ttk.Label(self.ventana, text="Del", anchor="center", font=("Arial", 26), foreground="Blue")
        self.etiqueta3.grid(column=2, row=0, padx=10, pady=50)
        self.Retardo(500)
        self.etiqueta4=ttk.Label(self.ventana, text="Orgullo", anchor="center", font=("Arial", 26), foreground="Orange")
        self.etiqueta4.grid(column=3, row=0, padx=10, pady=50)

    def EtiquetasLGTB(self):
        self.frame1=ttk.Frame(self.ventana)
        self.frame1.grid(column=0, row=1, columnspan=4)
        self.etiqueta5=ttk.Label(self.frame1, text="", anchor="center", font=("Arial", 40))
        self.etiqueta5.grid(column=0, row=0, padx=7)
        self.etiqueta6=ttk.Label(self.frame1, text="", anchor="center", font=("Arial", 40))
        self.etiqueta6.grid(column=1, row=0, padx=7)
        self.etiqueta7=ttk.Label(self.frame1, text="", anchor="center", font=("Arial", 40))
        self.etiqueta7.grid(column=2, row=0, padx=7)
        self.etiqueta8=ttk.Label(self.frame1, text="", anchor="center", font=("Arial", 40))
        self.etiqueta8.grid(column=3, row=0, padx=7)
        self.etiqueta9=ttk.Label(self.frame1, text="", anchor="center", font=("Arial", 40))
        self.etiqueta9.grid(column=4, row=0, padx=7)
        self.etiqueta10=ttk.Label(self.frame1, text="", anchor="center", font=("Arial", 40))
        self.etiqueta10.grid(column=5, row=0, padx=7)
        self.AleatorizarLetras(120)

    def AleatorizarLetras(self, contador):
        letra_inicio=ord("A")
        letra_fin=ord("Z")
        while contador>=0:
            eleccion=random.randint(letra_inicio, letra_fin)
            if contador>=100:
                self.etiqueta5.configure(text=chr(eleccion))
                if contador==100:
                    self.etiqueta5.configure(text="L")
            eleccion=random.randint(letra_inicio, letra_fin)
            if contador>=80:
                self.etiqueta6.configure(text=chr(eleccion))
                if contador==80:
                    self.etiqueta6.configure(text="G")
            eleccion=random.randint(letra_inicio, letra_fin)
            if contador>=60:
                self.etiqueta7.configure(text=chr(eleccion))
                if contador==60:
                    self.etiqueta7.configure(text="T")
            eleccion=random.randint(letra_inicio, letra_fin)
            if contador>=40:
                self.etiqueta8.configure(text=chr(eleccion))
                if contador==40:
                    self.etiqueta8.configure(text="B")
            if contador>=20:
                self.etiqueta9.configure(text=chr(eleccion))
                if contador==20:
                    self.etiqueta9.configure(text="I")
            eleccion=random.randint(letra_inicio, letra_fin)
            if contador>=0:
                self.etiqueta10.configure(text=chr(eleccion))
            self.Retardo(100)
            contador-=1
        contador=5
        while contador>=0:
            eleccion=random.randint(ord("P"), ord("R"))
            self.etiqueta10.configure(text=chr(eleccion))
            self.Retardo(500)
            if contador==0:
                self.etiqueta10.configure(text="Error", foreground="Red", font=("Arial", 50))
            contador-=1

    def EtiquetaPersonasTotales(self):
        self.frame2=ttk.Frame(self.ventana)
        self.frame2.grid(column=0, row=2, padx=10, pady=20, columnspan=4)
        self.etiqueta11=ttk.Label(self.frame2, text="Ya somos:", font=("Arial", 16))
        self.etiqueta11.grid(column=0, row=0)
        self.etiqueta12=ttk.Label(self.frame2, text="", font=("Arial", 16))
        self.etiqueta12.grid(column=1, row=0)
        self.AnimarNumeros()

    def AnimarNumeros(self):
        numero=5000
        while numero<=246000000:
            self.etiqueta12.configure(text=self.FormatearNumeros(numero))
            self.Retardo(100)
            if numero>=60000000:
                self.etiqueta12.configure(font=("Arial", 22), foreground="Orange")
            if numero>=200000000:
                self.etiqueta12.configure(font=("Arial", 28), foreground="Red")
            numero+=1847789
        self.etiqueta12.configure(text="XXXXXXXXXXXXXX")

    def FormatearNumeros(self, num):
        numero=str(num)
        pos=len(numero)-1
        numerocodificado=""
        punto=0
        while pos>=0:
            if punto==3:
                numerocodificado="."+numerocodificado
                punto=0
            numerocodificado=numero[pos]+numerocodificado
            punto+=1
            pos-=1
        return numerocodificado

    def MostrarErroresEmergentes(self):
        for x in range(30):
            self.emergente=tk.Toplevel()
            self.emergente.title("ERROR")
            self.etiqueta13=ttk.Label(self.emergente, text="ERROR CRÍTICO EN EL PROGRAMA, INVASIÓN LGTBIQ+ INMINENTE.", anchor="center", font=("Arial", 20), foreground="Red")
            self.etiqueta13.grid(column=0, row=0, padx=10, pady=10)
            self.etiqueta14=ttk.Label(self.emergente, text="ABORTANDO PROGRAMA", anchor="center", font=("Arial", 20), foreground="Red")
            self.etiqueta14.grid(column=0, row=1, padx=10, pady=10)
            self.Retardo(100)

    def Retardo(self, milisegundos):
        self.ventana.update()
        self.ventana.after(milisegundos)

    def Salir(self):
        self.Retardo(5000)
        sys.exit(0)

if __name__=="__main__":
    iniciar=Aplicacion()
    