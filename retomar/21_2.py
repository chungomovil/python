"""
Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días.
"""

emple=[]
falta=[]
menores=[]

for x in range(3):
    validar=False
    while validar==False:
        nombre=input("Nombre de empleado: ")
        validar=nombre.isalpha()
        if validar==False:
            print("--> Solo se admiten letras.")
    emple.append(nombre)
    falta.append([])
    dias=""
    while dias!="q" and dias!="Q":
        while True:
            dias=input("Dias que falto ('Q' omitir): ")
            try:
                if dias.lower()=="q":
                    break
                else:
                    dias=int(dias)
                    if dias>0:
                        falta[x].append(dias)
                    else:
                        print("--> Solo se aceptan valores superiores a 0.")
                    break
            except ValueError:
                print("--> Solo valores numericos.")

menor=len(falta[0])
print("\n--------------------\nDATOS INTRODUCIDOS\n--------------------\n")
for x in range(len(emple)):
    print("Empleado:",emple[x])
    print("Faltas: ",end="")
    if len(falta[x])==0:
        print("Sin faltas.")
    else:
        for k in range(len(falta[x])):
            print(falta[x][k],end="")
            if k<len(falta[x])-1:
                print(", ",end="")
    total=len(falta[x])
    print("\nTotal inasistencias:",total)
    if menor>=total:
        menor=total
    print("-------------------------")

for x in range(len(emple)):
    total=len(falta[x])
    if menor==total:
        menores.append(emple[x])

print("\n----------------------\nEMPLEADOS CON MENOS FALTAS\n----------------------\n")
for x in range(len(menores)):
    print("Nombre:",menores[x])