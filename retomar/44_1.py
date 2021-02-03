"""
Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos: inicializar el valor del lado llegando como parámetro al método __init__ (definir un atributo llamado lado), imprimir su perímetro y su superficie.
"""

class Cuadrado:

    def __init__(self):
        self.lado=0
        while self.lado<=0:
            self.lado=float(input("Introducir lado del cuadrado (cm): "))
            self.lado=round(self.lado, 2)
            if self.lado<=0:
                print("ERROR: La longitud del lado debe de ser superior a 0.")
        print("El lado del cuadrado mide %s cm." % (self.lado))

    def Perimetro(self):
        self.perimetro=self.lado*4
        print("\nEl perimetro del cuadrado es %s cm." % (self.perimetro))
    
    def Superficie(self):
        self.superficie=self.lado*self.lado
        print("\nLa superficie del cuadrado es %s cm." % (self.superficie))


cuadrado1=Cuadrado()
cuadrado1.Perimetro()
cuadrado1.Superficie()