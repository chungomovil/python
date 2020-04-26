"""Realizar la carga de dos nombres de personas distintos.
Mostrar por pantalla luego ordenados en forma alfabética."""

persona1=input("introducir primer nombre: ")
persona2=input("introducir segundo nombre: ")

if persona1>persona2:
    print("El nombre",persona1,"es mayor alfabeticamente.")
else:
    if persona1<persona2:
        print("El nombre",persona2,"es mayor alfabeticamente.")
    else:
        print("Los nombres introducir son iguales.")