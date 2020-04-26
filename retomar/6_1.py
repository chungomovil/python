"""Realizar un programa que solicite la carga por teclado de dos números, 
si el primero es mayor al segundo informar su suma y diferencia, 
en caso contrario informar el producto y la división del primero respecto al segundo."""

num1=int(input("introducir primer valor: "))
num2=int(input("introducir segundo valor: "))

if num1>num2:
    print("la suma de ambos valores es:",num1+num2)
    print("la resta de",num1, "menos",num2,"es",num1-num2)

else:
    print("la multiplicacion de ambos valores es:",num1*num2)
    print("la division de ambos valores es:",num1/num2)