"""Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc."""

"FORMA-1 USANDO MULTIPLICACION (MAS COMPLEJO)"
x=1
num=8
multi=0
print("primera forma (multiplicando)")

while multi<=500:
    print(multi)
    multi=num*x
    x+=1

"FORMA-2 SUMANDO 8 (SENCILLO)"

num=8
print("segunda forma (sumando 8)")

while num<=500:
    print(num)
    num+=8
