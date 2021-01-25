"""
Cargar una cadena de caracteres por teclado. Mostrar la cadena del final al principio utilizando subíndices negativos.
"""

def OrdenInverso1(cadena):
    print(20*"*")
    print("Oracion inversa primera forma")
    print(20*"*")
    for x in range(len(cadena)-1, -1, -1): # Esta es una forma de hacerla con los indices del bucle for; parte de la longitud de la (cadena-1) y va restando -1 hasta llegar al numero -1
        print(cadena[x],end="")

def OrdenInverso2(cadena):
    print("\n")
    print(20*"*")
    print("Oracion inversa segunda forma")
    print(20*"*")
    orden=-1
    for x in range(len(cadena)):
        print(cadena[orden],end="")
        orden-=1


oracion=input("Introducir una oracion: ")
OrdenInverso1(oracion)
OrdenInverso2(oracion)