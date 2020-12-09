"""Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'."""

def calcular_a(frase):
    frase=frase.lower()
    total=0
    for x in range(len(frase)):
        if frase[x]=="a":
            total+=1
    return total

print("CALCULAR TOTAL DE 'A'")
oracion=input("Introducir una frase: ")
total=calcular_a(oracion)
print("Hay un total de %s vocales 'A'" % (total))
