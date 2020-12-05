"""Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores."""

numeros=[]
eliminados=[]

for x in range(5):
    numero=int(input("Introducir valor numerico: "))
    numeros.append(numero)

print("\nValores introducidos: %s" % (numeros))

posicion=0

while posicion<(len(numeros)):
    if numeros[posicion]>=10:
        print("\nSe ha eliminado el valor %s" % (numeros[posicion]))
        eliminados.append(numeros[posicion])
        numeros.pop(posicion)

    else:
        posicion+=1

print("\nValores menores a 10: %s" % (numeros))
print("\nValores iguales o mayores a 10: %s" % (eliminados))

