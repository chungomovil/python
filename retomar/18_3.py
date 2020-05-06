"""
Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y mostrarla por pantalla, luego ordenar de mayor a menor e imprimir nuevamente.
"""

numeros=[]

for x in range(5):
    while True:
        numero=input("Introducir numero: ")
        try:
            numero=int(numero)
            break
        except ValueError:
            print("--> Solo numeros enteros.")
    numeros.append(numero)

print("\n-------------------\nLISTA INTRODUCIDA\n-------------------\n",numeros)
print("\n-------------------\nLISTA DE MENOR A MAYOR\n-------------------\n")

for x in range(len(numeros)):
    for k in range(len(numeros)-1):
        if numeros[k]>numeros[k+1]:
            aux=numeros[k+1]
            numeros[k+1]=numeros[k]
            numeros[k]=aux

print(numeros)

print("\n-------------------\nLISTA DE MAYOR A MENOR\n-------------------\n")

for x in range(len(numeros)):
    for k in range(len(numeros)-1):
        if numeros[k]<numeros[k+1]:
            aux=numeros[k]
            numeros[k]=numeros[k+1]
            numeros[k+1]=aux

print(numeros)
