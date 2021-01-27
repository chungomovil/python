"""
Confeccionar una programa con las siguientes funciones:
1) Generar una lista con 4 elementos enteros aleatorios comprendidos entre 1 y 3. Agregar un quinto elemento con un 1.
2) Controlar que el primer elemento de la lista sea un 1, en el caso que haya un 2 o 3 mezclar la lista y volver a controlar hasta que haya un 1.
3) Imprimir la lista.
"""

import random

def Imprimir(mensaje, numeros):
    print(len(mensaje)*"*")
    print(mensaje.upper())
    print(len(mensaje)*"*")
    print(numeros)

def GenerarNumeros():
    numeros=[]
    for x in range(4):
        numero=random.randint(1,3)
        numeros.append(numero)
    numeros.append(1)
    return numeros

def Mezclador(numeros):
    while numeros[0]!=1:
        random.shuffle(numeros)
    return numeros

valores=GenerarNumeros()
Imprimir("Valores iniciales",valores)
valores=Mezclador(valores)
Imprimir("Valores nuevos (debe comenzar la lista en 1)",valores)

