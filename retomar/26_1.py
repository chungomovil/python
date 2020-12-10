"""Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero. Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado."""

def decorar(mensaje):
    print("-------------------")
    print(mensaje.upper())
    print("-------------------")

def multiplicacion(numeros, factor):
    decorar("lista multiplicada por %s" % (factor))  
    for x in range(len(numeros)):
        multiplo=numeros[x]*factor
        decorar("%s X %s = %s" % (numeros[x], factor, multiplo))


valores=[5, 15, 1, -55, 107, 0]
decorar("lista introducida \n %s" % (valores))
multiplicacion(valores, 7)
