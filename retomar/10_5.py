"""Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), 
isósceles (dos lados iguales), o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo."""

equi=0
isos=0
esca=0

for x in range(1,7):
    ultimo=0
    print("\n---------------------\ntriangulo numero:",x)
    primer=int(input("Primer lado (cm): "))
    segundo=int(input("Segundo lado (cm): "))
    tercero=int(input("Tercer lado (cm): "))

    if primer==segundo and primer==tercero:
        equi+=1
        ultimo+=1
        if ultimo==1:
            print("conclucion: equilatero")
    else:
        if primer==segundo or primer==tercero or segundo==tercero:
            isos+=1
            ultimo+=1
            if ultimo==1:
                print("conclusion: isosceles")
        else:
            esca+=1
            ultimo+=1
            if ultimo==1:
                print("conclusion: escaleno")

print("\nRESUMEN")
print("------------------------")
print("equilatero:",equi)
print("isosceles:",isos)
print("escaleno:",esca)
    