"""Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados."""

def calcular_superficie(base, altura):
    superficie=base*altura
    return superficie

def mayor(objeto1, objeto2):
    if objeto1==objeto2:
        print("Ambos rectangulos son iguales.")
    else:
        if objeto1>objeto2:
            print("El primer rectangulo es el mayor.")
        else:
            print("El segundo rectangulo es el mayor.")

rectangulos=[]

for x in range(2):
    print("Rectangulo %s" % (x+1))
    base=int(input("Introducir longitud de la base: "))
    altura=int(input("Introducir altura: "))
    superficie=calcular_superficie(base, altura)
    rectangulos.append(superficie)

for x in range(2):
    print("La superficie del rectangulo %s es %s cm" % (x+1, rectangulos[x]))

mayor(rectangulos[0],rectangulos[1])