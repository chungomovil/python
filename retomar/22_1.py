"""Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)"""

nombres=[]
sueldos=[]
numero=0
while numero<=0 or numero>=10:
    numero=int(input("Total de trabajadores: "))
    if numero<=0 or numero>=10:
        print("El rango debe de ser entre 1 y 10.")

for x in range(numero):
    print("<--DATOS DEL EMPLEADO (%s) -->" % (x+1))
    nombre=input("Nombre del empleado: ")
    sueldo=0
    while sueldo<=50:
        sueldo=float(input("Sueldo del empleado: "))
        if sueldo<=50:
            print("El sueldo debe de ser superior a 50.")
    sueldo=round(sueldo,2)
    nombres.append(nombre)
    sueldos.append(sueldo)

print("\n<--LISTA TOTAL DE EMPLEADOS Y SUELDOS-->")
print("Nombres: %s" % (nombres))
print("Sueldos: %s" % (sueldos))

posicion=0
while posicion<len(nombres):
    if sueldos[posicion]>10000:
        print("\nSe ha eliminado al trabajador %s con un sueldo de %s" % (nombres.pop(posicion),sueldos.pop(posicion)))
    else:
        posicion+=1
    
print("\n<--LISTA DE EMPLEADOS CON SUELDOS INFERIORES A 10.000-->")
print("Nombres: %s" %(nombres))
print("Sueldos: %s" % (sueldos))