"""Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar 
un mensaje indicando si el número tiene uno o dos dígitos.
(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)"""

num=-1

while num<0 or num>99:
    num=int(input("Introducir valor del 1 al 99: "))

if num>=10:
    print("el numero tiene 2 cifras")

else:
    print("el numero tiene 1 cifra")