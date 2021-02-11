"""
Desarrollar una clase llamada Lista, que permita pasar al método __init__ una lista de valores enteros.
Redefinir los operadores +,-,* y // con respecto a un valor entero.
"""

class Lista:
    #Iniciar atributos esenciales
    def __init__(self, valores):
        self.valores=valores
    #Metodo imprimir cadena
    def __str__(self):
        return "Lista: "+str(self.valores)
    #Metodo sumar
    def __add__(self, referencia):
        numeros=[]
        for valor in self.valores:
            numeros.append(valor+referencia)
        return numeros
    #Metodo restar
    def __sub__(self, referencia):
        numeros=[]
        for valor in self.valores:
            numeros.append(valor-referencia)
        return numeros
    #Metodo multiplicar
    def __mul__(self, referencia):
        numeros=[]
        for valor in self.valores:
            numeros.append(valor*referencia)
        return numeros
    #Metodo dividir sin resto
    def __floordiv__(self, referencia):
        numeros=[]
        for valor in self.valores:
            numeros.append(valor//referencia)
        return numeros
    #Metodo dividir
    def __truediv__(self, referencia):
        numeros=[]
        for valor in self.valores:
            numeros.append(valor/referencia)
        return numeros

#BLOQUE PRINCIPAL
ejecutar=Lista((10, 92, 16, -12, -23, 3))
print(30*"*")
print("LISTA")
print(ejecutar)
print(30*"_")
print("SUMATORIO + 10")
print(ejecutar+10)
print(30*"_")
print("RESTA - 23")
print(ejecutar-23)
print(30*"_")
print("MULTIPLICACION x 17")
print(ejecutar*17)
print(30*"_")
print("DIVISION SIN RESTO // 2")
print(ejecutar//2)
print(30*"_")
print("DIVISION / 4")
print(ejecutar/4)
