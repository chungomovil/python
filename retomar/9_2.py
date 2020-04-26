"""Se ingresan un conjunto de n alturas de personas por teclado. 
Mostrar la altura promedio de las personas."""

x=1
suma=0

while x<=5:
    altura=float(input("ingresar altura: "))
    suma=suma+altura
    x+=1

x-=1
promedio=suma/x

print("el promedio de las",x,"alturas introducidas es:",round(promedio,2))