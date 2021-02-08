"""
Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo. Definir los atributos y métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.
Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un plazo fijo añade un plazo de imposición en días y una tasa de interés. Hacer que la caja de ahorro no genera intereses.
En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.
"""

class Cuenta:

    def __init__(self):
        self.titular=""
        self.dni=""
        self.total=0
    
    def CargaDatos(self):
        condicion=False
        while condicion==False:
            print(30*"+")
            print("datos del titular".upper())
            print(30*"+")
            self.titular=input("Nombre: ")
            self.dni=input("DNI: ")
            self.total=float(input("Total a ingresar: "))
            self.total=round(self.total, 2)
            if self.titular=="" or self.dni=="" or self.total<=0:
                print("ERROR: Rellenar ambos campos.")
            else:
                condicion=True
                print("Usuario creado correctamente.")
    
    def Imprimir(self):
        print("Total acumulado en cuenta: %s €" % (self.total))
    
class CajaAhorro(Cuenta):

    def Cargar(self):
        print(30*"_")
        print("caja de ahorro".upper())
        print(30*"_")
        super().CargaDatos()
    
    def Imprimir(self):
        super().Imprimir()

class PlazoFijo(Cuenta):

    def Cargar(self):
        print(30*"_")
        print("plazo fijo".upper())
        print(30*"_")
        super().CargaDatos()
    
    def PlazoInteres(self):
        condicion=False
        while condicion==False:
            self.plazo=int(input("Plazo: "))
            self.interes=float(input("Interes: "))
            self.interes=round(self.interes, 2)
            if self.interes<=0 or self.plazo<=0:
                print("ERROR: Los valores deben ser mayores a 0.")
            else:
                condicion=True
    
    def Calcular(self):
        self.ganancia=(self.total/100)*self.interes
        self.total=self.total+self.ganancia
    
    def Imprimir(self):
        print("***resultado***".upper())
        print("Plazo: %s dias" % (self.plazo))
        print("Interes:",self.interes,"%") # lo puse asi porque no dejaba poner '%' despues de '%s'
        print("Capital inicial: %s €" % (self.total-self.ganancia)) # de esta forma no hace falta crear una nueva variable para mostrar el capital sin intereses
        super().Imprimir()

condicion=""
while condicion!="Q":
    print("***elegir opcion***".upper())
    condicion=input("Introducir 'A' para caja de ahorros o 'B' para plazo fijo ('Q' omitir): ")
    condicion=condicion.upper()
    if condicion!="Q":
        if condicion=="A":
            cliente=CajaAhorro()
            cliente.Cargar()
            cliente.Imprimir()
        elif condicion=="B":
            cliente=PlazoFijo()
            cliente.Cargar()
            cliente.PlazoInteres()
            cliente.Calcular()
            cliente.Imprimir()
        else:
            print("ERROR: Introducir una de las anteriores opciones...")