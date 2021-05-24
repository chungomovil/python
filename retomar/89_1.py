"""Ingresar por teclado dos enteros, calcular su suma y luego mostrar un mensaje de los dos valores ingresados y su suma. MOSTRAR SALIDA CON f-strings."""

num1=int(input("Ingresar primer valor: "))
num2=int(input("Ingresar segundo valor: "))
suma=num1+num2
#Formateamos con f-strings
print(f"La suma de {num1} + {num2} es igual a {suma}")

