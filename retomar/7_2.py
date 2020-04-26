"""Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo,
negativo o nulo (es decir cero)"""

num=int(input("introducir valor: "))

if num==0:
    print("el numero es igual a cero.")
else:
    if num<0:
        print("el numero es negativo.")
    else:
        print("el numero es positivo.")