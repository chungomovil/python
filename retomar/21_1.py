"""
Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
c - Calcular la temperatura media trimestral de cada país.
c - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
b - Imprimir el nombre del pais con la temperatura media trimestral mayor.
"""

paises=[]
temperaturas=[]
medias=[]

for x in range(4):
    validar=False
    print("-------------------\nPAIS\n-------------------")
    while validar==False:
        pais=input("Nombre del pais: ")
        validar=pais.isalpha()
        if validar==False:
            print("--> Solo se admiten letras.")
    print("--------------------\nTEMPERATURAS\n--------------------")
    paises.append(pais)
    temperaturas.append([])
    for k in range(1, 4):
        while True:
            print("Temperatura",k,":", end="")
            temp=input(" ")
            try:
                temp=float(temp)
                break
            except ValueError:
                print("--> Solo valores numericos.")
        temperaturas[x].append(temp)

for x in range(len(temperaturas)):
    suma=0
    for k in range(len(temperaturas[x])):
        suma=suma+temperaturas[x][k]
    media=suma/(k+1)
    medias.append(round(media,1))

mayor=medias[0]
posmayor=0

for x in range(len(medias)):
    if mayor<medias[x]:
        mayor=medias[x]
        posmayor=x

print("\n-------------------\nDATOS\n-------------------")
for x in range(len(paises)):
    print("Pais:",paises[x])
    print("Temperaturas: ",end="")
    for k in range(len(temperaturas[x])):
        print(temperaturas[x][k],end="")
        if k<len(temperaturas[x])-1:
            print(", ",end="")
    print("\n-------------------")

print("-------------------\nMEDIA TIMESTRAL\n-------------------")
for x in range(len(paises)):
    print("Pais:",paises[x])
    print("Temperatura Media:",medias[x])

print("-------------------\nPAIS MAS CALUROSO\n-------------------")
print("Pais:",paises[posmayor])
print("Temperatura:",medias[posmayor])
