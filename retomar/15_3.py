"""
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde). 
Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos.
"""

maniana=[]
tarde=[]

for x in range(8):
    if x<4:
        print("SUELDO TURNO DE MANIANA")
        valor=float(input("Introducir sueldo: "))
        maniana.append(valor)
    else:
        print("SUELDO TURNO DE TARDE")
        valor=float(input("Introducir sueldo: "))
        tarde.append(valor)

print("\n-------------------\nSueldos turno de maniana\n",maniana,"\n-------------------\n")
print("Sueldos turno de tarde\n",tarde,"\n-------------------")
