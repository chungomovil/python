"""Implementar una función recursiva que imprima en forma descendente de 5 a 1 de uno en uno."""

#Crear funcion
def Entero(numero):
    #Crear caso base
    if numero>0:
        #Imprimir secuencia SIN orden de liberacion en la memoria
        print(numero)
        #Crear recursividad
        Entero(numero-1)

#Llamar a la funcion
Entero(5)

