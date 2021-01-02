"""Confeccionar una función que reciba una serie de edades y me retorne la cantidad que son mayores o iguales a 18 (como mínimo se envía un entero a la función)"""

def CalcularEdades(ed1, *lista):
    mayoredad=[]
    if ed1>=18:
        mayoredad.append(ed1)
    for x in range(len(lista)):
        if lista[x]>=18:
            mayoredad.append(lista[x])
    return mayoredad

print("Las edades mayores o iguales a 18 son: %s" % (CalcularEdades(1, 17, 22, 67, 50, 15, 18)))

