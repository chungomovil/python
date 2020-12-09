"""Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado."""

def calcular_perimetro(lado):
    perimetro=lado*4
    return perimetro

valor=int(input("Introducir longitud del lado: "))

perimetro=calcular_perimetro(valor)

print("El primetro del cuadrado es %s cm" % (perimetro))
