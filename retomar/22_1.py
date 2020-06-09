"""
Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)
"""

emples=[]
sueldos=[]
validar=False

while validar==False:
    num=input("Numero de trabajadores: ")
    validar=num.isdigit()
    if validar==True:
        num=int(num)
    else:
        print("--> Solo valores superiores a 0")

for x in range(num):
    validar=False
    print("- Empleado",x+1,"-")
    while validar==False:
        emple=input("Nombre de empleado: ")
        validar=emple.isalpha()
        if validar==False:
            print("--> Solo letras")
    validar=False
    while validar==False:
        sueldo=input("Sueldo: ")
        validar=sueldo.isdigit()
        if validar==True:
            sueldo=int(sueldo)
        else:
            print("--> Solo valores igual o supperiores a 0")
    emples.append(emple)
    sueldos.append(sueldo)

posicion=0

while posicion<len(emples):
    if sueldos[posicion]>10000:
        print("\n--> Se ha eliminado:")
        print("Empleado:",emples[posicion])
        print("Sueldo:",sueldos[posicion])
        emples.pop(posicion)
        sueldos.pop(posicion)
    else:
        posicion+=1

print("\n-PLANTILLA FINAL-")

for x in range(len(emples)):
    print("Nombre:",emples[x])
    print("Sueldo:",sueldos[x],"\n")
