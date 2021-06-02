"""
Confeccionar una función de orden superior que reciba una lista que almacena valores enteros y una función con un parámetro entero y que retorne un boolean.
La función debe analizar cada elemento de la lista llamando a la función que recibe como parámetro, si retorna un True se pasa a mostrar el elemento.

En el bloque principal definir una lista de enteros.

Imprimir de la lista:

Los valores múltiplos de 2
Los valores múltiplos de 3 o de 5
Los valores mayores o iguales a 50
Los valores comprendidos entre 1 y 50 o entre 70 y 100.
"""

#Creamos el metodo de orden superior
def Analizar(lista, fn):
    #Recorremos lista
    for numero in lista:
        #Retornamos booleano
        if fn(numero):
            #Imprimimos el resultado si es booleano es True
            print(numero)

#Creamos la lista
lista=[2, 18, 55, 100, 99, 1802, 567, 75]
#Creamos las diferentes lambdas para cada uno de los filtros
print("Multiplos de 2\n", 15*"-", sep="")
Analizar(lista, lambda x: x%2==0)
print("Multiplos de 3 o de 5\n", 15*"-", sep="")
Analizar(lista, lambda x: x%3==0 or x%5==0)
print("Mayores o iguales a 50\n", 15*"-", sep="")
Analizar(lista, lambda x: x>=50)
print("Comprendidos entre 1 y 50 y 70 y 100\n", 15*"-", sep="")
Analizar(lista, lambda x: x>=1 or x<=50 or x>=70 or x<=100)



