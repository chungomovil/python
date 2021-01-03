"""Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor."""

def CargaDatos():
    numeros=[]
    for x in range(1, 6):
        num=int(input("Introducir numero [%s]: " % (x)))
        numeros.append(num)
    return numeros

def CalcularExtremos(lista):
    menor=lista[0]
    mayor=lista[0]
    for x in range(len(lista)):
        if menor>lista[x]:
            menor=lista[x]
        else:
            if mayor<lista[x]:
                mayor=lista[x]
    return (menor,mayor)    #CONVERTIR A TUPLA


numeros=CargaDatos()
menor,mayor=CalcularExtremos(numeros) #DESEMPAQUETAR TUPLA
print("\nLa lista ingresada es: %s" % (numeros))
print("\nEl valor menor es: %s" % (menor))
print("\nEl valor mayor es: %s" % (mayor))