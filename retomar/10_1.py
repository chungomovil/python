"""Confeccionar un programa que lea n pares de datos, 
cada par de datos corresponde a la medida de la base y la altura de un triángulo. 
El programa deberá informar:
a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12."""

mayores=0

for x in range(1,4):
    base=int(input("Longitud de la base (cm): "))
    altura=int(input("Altura (cm): "))
    superficie=base*(altura/2)
    
    if superficie>12:
        mayores+=1

    print("------------------------")
    print("Triangulo:",x)
    print("Longitud de la base: ",base,"cm",sep="")
    print("Altura: ",altura,"cm",sep="")
    print("Superficie: ",superficie,"cm",sep="")

print("+++++++++++++++++++++")
if mayores==0:
    print("Ningun triangulo tiene la superficie superior a 12.")
else:
    if mayores==1:
        print(mayores,"triangulo tiene la superficie superior a 12.")
    else:
        print(mayores,"triangulos tienen la superficie superior a 12.")
        

