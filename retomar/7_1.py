"""Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos."""

num1=int(input("introducir primer valor: "))
num2=int(input("introducir segundo valor: "))
num3=int(input("introducir tercer valor: "))

if num1 > num2 and num1 > num3:
    print("el numero mayor es el numero",num1)
else:
    if num2 > num3:
        print("el numero mayor es el numero",num2)
    else:
       print("el numero mayor es el numero",num3)