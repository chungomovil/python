"""Desarrollar un programa que permita cargar n números enteros y luego nos informe 
cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional 
(este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):"""

num=0
pares=0
impares=0
x=1

while x<=6:
    num=int(input("introducir numero: "))
    if num%2==0:
        pares+=1
    else:
        impares+=1
    x+=1

if pares==0:
    print("todos los numeros introducidos son impares")
else:
    if impares==0:
        print("todos los numeros introducidos son pares")
    else:
        print("total pares:",pares)
        print("total impares:",impares)