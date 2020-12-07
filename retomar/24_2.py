"""Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primera función definida."""

def decorar(mensaje):
    print("***********************************")
    print(mensaje.upper())
    print("***********************************")

#SE DEBEN DE REALIZAR DOS BUCLES PARA QUE SE ORDENEN CORRECTAMENTE EN VARIAS PASADAS
def ordenar(valor1, valor2, valor3):
    numeros=[valor1, valor2, valor3]
    for x in range(len(numeros)-1):
        for y in range(len(numeros)-1):
            if numeros[y]>numeros[y+1]:
                aux=numeros[y+1]
                numeros[y+1]=numeros[y]
                numeros[y]=aux
    print(numeros)

def cargar():
    num1=int(input("Introducir PRIMER valor: "))
    num2=int(input("Introducir SEGUNDO valor: "))
    num3=int(input("Introducir TERCER valor: "))
    decorar("lista ordenada")
    ordenar(num1, num2, num3)

cargar()