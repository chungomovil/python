"""Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos."""

def mensaje(texto):
    print("******************************************")
    print(texto.upper())
    print("******************************************")

def promedio(valor1, valor2, valor3):
    resultado=(valor1+valor2+valor3)/3
    return round(resultado,2)

numero1=int(input("Introducir primer numero: "))
numero2=int(input("Introducir segundo numero: "))
numero3=int(input("Introducir tercer numero: "))

promediofinal=promedio(numero1, numero2, numero3)

mensaje("el promedio de %s, %s y %s es %s" % (numero1, numero2, numero3, promediofinal))
