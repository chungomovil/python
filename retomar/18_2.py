"""
Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear y cargar una lista con todos los sueldos de dichos empleados. Imprimir la lista de sueldos ordenamos de menor a mayor.
"""

nombres=[]
sueldos=[]
numeroemple=True

while True:
    numeroemple=input("Total empleados: ")
    try:
        numeroemple=int(numeroemple)
        if numeroemple>0:
            break
        else:
            print("--> El valor debe de ser superior a 0")
    except ValueError:
        print("--> Introducir valor numerico entero.")

print("\n-----------------\nDATOS DE LOS EMPLEADOS\n-----------------\n")

for x in range(numeroemple):
    validar=False
    while validar==False:
        nombre=input("Introducir nombre: ")
        validar=nombre.isalpha()
        if validar==False:
            print("--> Nombre incorrecto.")
    while True:
        sueldo=input("Introducir sueldo: ")
        try:
            sueldo=float(sueldo)
            if sueldo>0:
                break
            else:
                print("--> El sueldo debe de ser superior a 0.")
        except ValueError:
            print("--> Introducir valor numerico.")
    nombres.append(nombre)
    sueldos.append(sueldo)

print("\n-----------------\nPLANTILLA DE LA EMPRESA\n-----------------\n")
for x in range(len(nombres)):
    print("Trabajador numero ",x," --> ",nombres[x]," (",sueldos[x]," euros)",sep="")

for x in range(len(sueldos)-1):
    for k in range(len(sueldos)-1):
        if sueldos[k]>sueldos[k+1]:
            auxsueldo=sueldos[k]
            sueldos[k]=sueldos[k+1]
            sueldos[k+1]=auxsueldo
            auxnombre=nombres[k]
            nombres[k]=nombres[k+1]
            nombres[k+1]=auxnombre

print("\n-----------------\nPLANTILLA ORDENADA\n-----------------\n")

for x in range(len(nombres)):
    print("Trabajador numero ",x," --> ",nombres[x]," (",sueldos[x]," euros)",sep="")

