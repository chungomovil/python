"""
Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el método __init__, calcular su suma, resta, multiplicación y división, cada una en un método, imprimir dichos resultados.
"""

class Operaciones:

    def __init__(self):
        self.num1=int(input("Introducir primer valor: "))
        self.num2=int(input("Introducir segundo valor: "))
    
    def Suma(self):
        self.suma=self.num1+self.num2

    def Resta(self):
        self.resta=self.num1-self.num2
    
    def Multi(self):
        self.multi=self.num1*self.num2
    
    def Divi(self):
        self.divi=self.num1/self.num2
        self.divi=round(self.divi, 2)
    
    def Imprimir(self):
        print(20*"*")
        print("resultados".upper())
        print(20*"*")
        print("valores introducidos:".upper(),self.num1,"y",self.num2)
        print("Suma:", self.suma)
        print("Resta:", self.resta)
        print("Multiplicacion:",self.multi)
        print("Division:",self.divi)

iniciar=Operaciones()
iniciar.Suma()
iniciar.Resta()
iniciar.Multi()
iniciar.Divi()
iniciar.Imprimir()
