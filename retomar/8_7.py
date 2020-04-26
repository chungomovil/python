"""Escribir un programa en el cual: dada una lista de tres valores numéricos distintos
se muestre solo el menor y el mayor de ellos"""

num1=int(input("ingresar primer valor: "))
num2=int(input("ingresar segundo valor: "))
num3=int(input("ingresar tercer valor: "))

if num1<=num2 and num1<=num3:
    print("numero menor:",num1)
else:
    if num2<=num3:
        print("numero menor:",num2)
    else:
        print("numero menor:",num3)

if num1>=num2 and num1>=num3:
    print("numero mayor:",num1)
else:
    if num2>=num3:
        print("numero mayor:",num2)
    else:
        print("numero mayor:",num3)