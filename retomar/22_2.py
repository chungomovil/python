"""Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores."""

numeros=[]

for x in range(5):
    while True:
        numero=input("Introducir numero: ")
        try:
            numero=int(numero)
            break
        except ValueError:
            print("--> Solo valores numericos")
    numeros.append(numero)

posicion=0

while posicion<len(numeros):
    if numeros[posicion]>=10:
        print("--> Se ha eliminado el numero",numeros[posicion])
        numeros.pop(posicion)
    else:
        posicion+=1
            
print("-NUEVA LISTA-")
print(numeros)
