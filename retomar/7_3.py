"""Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras 
y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. 
Mostrar un mensaje de error si el número de cifras es mayor."""

num=-1
while num<0 or num>999:
    num=int(input("introducir numero de 0 a 999: "))

if num<10:
    print("el numero tiene una cifra.")
else:
    if num<100:
        print("el numero tiene dos cifras.")
    else:
        if num<1000:
            print("el numero tiene tres cifras.")