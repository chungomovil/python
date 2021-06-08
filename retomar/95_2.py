"""Realizar la carga de valores enteros y sumarlos, cada vez que se ingresa un valor preguntar al operador si desea ingresar otro valor.
Crear una estructura tipo conjunto que almacene las condiciones para seguir sumando."""

#Creamos la estructura tipo conjunto inmutable
opcion=frozenset(["no", "NO"])
suma=0

#Creamos el bucle
while True:
    num=int(input("Numero: "))
    print(f"{suma} + {num} = ", end="")
    suma=suma+num
    print(f"{suma}")
    continuar=input("Desea continuar, 'SI' o 'NO': ")
    #Busca si la opcion esta dentro del conjunto para romper el bucle
    if continuar in opcion:
        break

