"""
Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla.
"""

paises=[]

for x in range(5):
    validar=False
    while validar==False:
        pais=input("Introducir pais: ")
        validar=pais.isalpha()
        if validar==False:
            print("--> Nombre incorrecto.")
    paises.append(pais)

print("\n-------------------------\nPAISES INTRODUCIDOS\n-------------------------\n")
print(paises)

for x in range(len(paises)-1):
    for k in range(len(paises)-1):
        if paises[k]>paises[k+1]:
            aux=paises[k]
            paises[k]=paises[k+1]
            paises[k+1]=aux


print("\n-------------------------\nPAISES ORDENADOS\n-------------------------\n")
print(paises)
