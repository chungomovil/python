"""Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos debe retornar la suma de dichos valores. Debe tener tres parámetros por defecto."""

def Sumar(num1, num2, num3=0, num4=0, num5=0):
    suma=num1+num2+num3+num4+num5
    return suma

print("SUMAR")
print("7 + 19 = %s" % (Sumar(7, 19)))
print("18 - 10 + 90 = %s" % (Sumar(18, -10, 90)))
print("-81 - 70 + 15 + 0 = %s" % (Sumar(-81, -70, 15, 0)))
print("1500 + 901 - 97 - 180 + 283 = %s" % (Sumar(1500, 901, -97, -180, 283)))
