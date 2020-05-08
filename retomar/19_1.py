"""
Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir los resultados. Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.
"""

paises=[]
habitantes=[]

for x in range(5):
    validar=False
    while validar==False:
        pais=input("Nombre del pais: ")
        validar=pais.isalpha()
        if validar==False:
            print("--> Formato del PAIS incorrecto.")
    while True:
        habitante=input("Numero de habitantes: ")
        try:
            habitante=int(habitante)
            break
        except ValueError:
            print("--> Introducir numeros enteros.")
    paises.append(pais)
    habitantes.append(habitante)

print("\n------------------\nPAISES Y POBLACION INTRODUCIDA\n------------------\n")

for x in range(len(paises)):
    print("Pais:",paises[x])
    print("Habitantes:",habitantes[x])
    print("-----------------------------")

for x in range(len(paises)):
    for k in range(len(paises)-1-x):
        if paises[k]>paises[k+1]:
            auxp=paises[k]
            paises[k]=paises[k+1]
            paises[k+1]=auxp
            auxh=habitantes[k]
            habitantes[k]=habitantes[k+1]
            habitantes[k+1]=auxh

print("ORDENADOS ALFABETICAMENTE\n------------------\n")

for x in range(len(paises)):
    print("Pais:",paises[x])
    print("Habitantes:",habitantes[x])
    print("-------------------------")

for x in range(len(paises)):
    for k in range(len(paises)-1-x):
        if habitantes[k]<habitantes[k+1]:
            auxh=habitantes[k]
            habitantes[k]=habitantes[k+1]
            habitantes[k+1]=auxh
            auxp=paises[k]
            paises[k]=paises[k+1]
            paises[k+1]=auxp

print("ORDENADOS POR POBLACION\n------------------\n")

for x in range(len(paises)):
    print("Pais:",paises[x])
    print("Habitantes:",habitantes[x])
    print("------------------------")
