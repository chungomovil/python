"""Definir una lista de enteros por asignación en el bloque principal. Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. Mostrar dicho producto en el bloque principal de nuestro programa."""

def MultiplicarLista(lista):
    x=0
    acumulado=1
    while x<(len(lista)):
        acumulado=acumulado*lista[x]
        x+=1
    return acumulado

numeros=[51, 7, 1, 56, -1, -70, 6]

print("La multiplicacion de los valores de la lista", numeros)
print("Es:", MultiplicarLista(numeros))
