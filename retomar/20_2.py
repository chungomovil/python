"""
Se tiene la siguiente lista:
lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 10 contenidos en todos los elementos de la variable "lista".
Volver a imprimir la lista.
"""

lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]

print("Valores de la lista:",lista)

for x in range(len(lista)):
    for k in range(len(lista[x])):
        if lista[x][k]>10:
            print("--> El valor '",lista[x][k],"' es mayor a 10",sep="")
            lista[x][k]=0
            print("--> Se ha sustituido por '",lista[x][k],"'",sep="")

print("\n----------------\nLISTA FINAL\n----------------\n",lista)
