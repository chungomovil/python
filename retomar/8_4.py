"""Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, 
imprimir en pantalla la leyenda "Alguno de los números es menor a diez"."""

num1=int(input("ingresar primer valor: "))
num2=int(input("ingresar segundo valor: "))
num3=int(input("ingresar tercer valor: "))

if num1<10 or num2<10 or num3<10:
    print("alguno de los valores es menor a 10: ",end="")
    if num1<10:
        print(num1," ",end="")
    if num2<10:
        print(num2," ",end="")
    if num3<10:
        print(num3," ",end="")
else:
    print("todos los numeros son mayores a 10")