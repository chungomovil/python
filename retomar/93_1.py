"""
Definir una función de orden superior llamada operar. Llegan como parámetro dos enteros y una función. En el bloque de la función llamar a la función que llega como parámetro y enviar los dos primeros parámetros.

Desde el bloque principal llamar a operar y enviar distintas expresiones lambdas que permitan sumar, restar, multiplicar y dividir.
"""

#Creamos la funcion de orden superior
def operar(num1, num2, fn):
    return fn(num1, num2)
    
#Creamos las lambdas e imprimimos el resultado
sumar=operar(10, 88, lambda valor1, valor2: valor1+valor2)
print(f"La suma es {sumar}")
restar=operar(178, 55, lambda valor1, valor2: valor1-valor2)
print(f"La resta es {restar}")
dividir=operar(90, 9, lambda valor1, valor2: valor1/valor2)
print(f"La division es {dividir}")
multiplicar=operar(5, 78, lambda valor1, valor2: valor1*valor2)
print(f"La multiplicacion es {multiplicar}")
