"""Desarrollar un programa con dos funciones. La primera que solicite el ingreso de un entero y muestre el cuadrado de dicho valor. La segunda que solicite la carga de dos valores y muestre el producto de los mismos. LLamar desde el bloque del programa principal a ambas funciones."""

def cuadrado():
    print("--CALCULAR CUADRADO--\n**************************************************")
    num1=int(input("Ingresar valor entero: "))
    result_cuadrado=num1*2
    print("El cuadrado de %s es %s \n" % (num1, result_cuadrado))

def multiplicacion():
    print("--CALCULAR MULTIPLICACION--\n**************************************************")
    num1=int(input("Ingresar PRIMER valor entero: "))
    num2=int(input("Ingresar SEGUNDO valor entero: "))
    result_multi=num1*num2
    print("%s x %s = %s" % (num1, num2, result_multi))

cuadrado()
multiplicacion()