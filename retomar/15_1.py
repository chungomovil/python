"""
Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.
"""

sueldo=[]
suma=0

for x in range (5):
    valor=float(input("Introducir sueldo: "))
    sueldo.append(valor)
    suma=suma+valor

promedio=suma/len(sueldo)
print("Salarios introducidos: ",sueldo)
print("El promedio es:", round(promedio, 2))
