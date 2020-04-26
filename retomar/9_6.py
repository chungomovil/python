"""Realizar un programa que permita cargar dos listas de 15 valores cada una. 
Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor 
(mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo."""

lista1=0
lista2=0
suma1=0
suma2=0
x=1

while x<=3:
    lista1=int(input("ingresar valor a la lista 1: "))
    suma1=suma1+lista1
    x+=1

x=1

while x<=3:
    lista2=int(input("ingresar valor a la lista 2: "))
    suma2=suma2+lista2
    x+=1

print("suma de la lista 1:",suma1)
print("suma de la lista 2:",suma2)

if suma1<suma2:
    print("la lista 2 es mayor")
else:
    if suma1>suma2:
        print("la lista 1 es mayor")
    else:
        print("la dos listas son iguales")
