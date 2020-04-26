"""Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10,
imprimir en pantalla la leyenda "Todos los números son menores a diez"."""

num1=int(input("ingresar primer valor: "))
num2=int(input("ingresar segundo valor: "))
num3=int(input("ingresar tercer valor: "))

if num1<10 and num2<10 and num3<10:
    print("todos los numeros son inferiores a 10")

else:
    print("no todos los numeros son inferiores a 10: ",end="")
    if num1>=10:
        print(num1," ",end="")
    if num2>=10:
        print(num2," ",end="")
    if num3>=10:
        print(num3," ",end="")
