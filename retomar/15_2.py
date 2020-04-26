"""
Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.
"""

altura=[]
suma=0
altas=0
bajas=0

for x in range(5):
    medida=float(input("Introducir altura: "))
    altura.append(medida)
    suma=suma+medida 

promedio=suma/len(altura)

for x in range(len(altura)):
    if altura[x]>=promedio:
        altas+=1
    else:
        bajas+=1

print("Las alturas ingresadas son:",altura,"\n--------------------------------")
print("El promedio de altura es:",round(promedio,2),"\n--------------------------------")
print("Personas superiores o iguales al promedio:",altas,"\n--------------------------------")
print("Personas inferiores al promedio:",bajas)