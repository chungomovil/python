"""Desarrollar un programa que solicite la carga de tres valores y muestre el menor. Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)"""

def elmenor():
    print("SELECCIONAR EL MENOR\n******************************************")
    numeros=[]
    posicion=["PRIMER","SEGUNDO","TERCER"]
    for x in range(3):
        numero=int(input("Introducir el %s valor: " % (posicion[x])))
        numeros.append(numero)
    menor=numeros[0]
    
    for y in range(len(numeros)):
        if menor>numeros[y]:
            menor=numeros[y]
    
    print("\nEl menor de los valores introducidos es %s \n" % (menor))


elmenor()
elmenor()