"""Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100."""

lista=[109, 75, 1, 901, 9871, 54, 6, 540]
mayores=0
x=0

while x<len(lista):
    if lista[x]>=100:
        mayores+=1
    x+=1

print("En la lista de valores",lista)
print("Hay un total de",mayores,"valores iguales o mayores a 100.")
