"""
Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de "lista".
Volver a imprimir la lista.
"""

lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print("Valores de la lista:",lista)

for x in range(len(lista)):
    if lista[0][x]>50:
        print("--> El valor de la lista:",lista[0][x],"es mayor a 50.")
        lista[0][x]=0
        print("--> Se ha sustituido por:",lista[0][x])

print("\n---------------\nNueva lista:\n---------------\n",lista)
