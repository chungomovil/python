"""Otro problema típico que se presenta para analizar la recursividad es el obtener el factorial de un número.
Recordar que el factorial de un número es el resultado que se obtiene de multiplicar dicho número por el anterior y así sucesivamente hasta llegar a uno.
Ej. el factorial de 4 es 4 * 3 * 2 * 1 es decir 24."""

#Creamos la funcion
def Factorial(numero):
    #Creamos el caso base
    if numero>0:
        #Creamos el algoritmo para calcular el factorial con recursividad
        factorial=numero*Factorial(numero-1)
        #Retornamos resultado
        return factorial
    #Controlamos que retorne 1 al ultimo frame (si no su valor seria 0 y daria error)
    else:
        return 1

#Llamamos a la funcion e imprimimos resultado
print(f"El factorial de 5 es {Factorial(5)}")


