"""Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores a 7."""

valores=[1, 7, -5, 10, 2]
x=0

print("Los valores mayores o iguales a 7 son: ", end="")

while x<len(valores):
    if valores[x]>=7:
        print(valores[x], ", " , end="")
    x+=1
