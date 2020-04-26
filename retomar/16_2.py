"""
Cargar una lista con 5 elementos enteros. 
Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)
"""

numeros=[]

for x in range(5):
    numero=int(input("Introducir numero: "))
    numeros.append(numero)

mayor=0

for x in range(len(numeros)):
    if numeros[x]>mayor:
        mayor=numeros[x]

repeticion=-1

for x in range(len(numeros)):
    if mayor==numeros[x]:
        repeticion+=1

print("\n--------------------\nNUMEROS INTRODUCIDOS")
print(numeros)
print("\n--------------------\nNUMERO MAYOR")
print(mayor, end="")
if repeticion>0:
    print(" y tiene un numero de repeticiones de:", repeticion)
    