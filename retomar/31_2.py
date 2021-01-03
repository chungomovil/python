"""Confeccionar un programa con las siguientes funciones:
1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores
2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos de empleados y muestre el nombre del empleado con sueldo mayor.
En el bloque principal del programa llamar dos veces a la función de carga y seguidamente llamar a la función que muestra el nombre de empleado con sueldo mayor."""

def CargarEmpleado(num):
    print("Datos el empleado numero [%s]" % (num))
    nom=input("Introducir nombre del empleado: ")
    sueldo=0
    while sueldo<=100:
        sueldo=float(input("Introducir salario: "))
        sueldo=round(sueldo, 2)
        if sueldo<=100:
            print("---> El sueldo debe de ser superior a 100.")
    return (nom,sueldo)

def MejorPagado(empleado1, empleado2):
    print("\nEmpleado con sueldo mayor")
    if empleado1[1]>empleado2[1]:
        print("Nombre: %s" % (empleado1[0]))
        print("Salario: %s" % (empleado1[1]))
    else:
        if empleado1[1]<empleado2[1]:
            print("nombre: %s" % (empleado2[0]))
            print("Salario: %s" % (empleado2[1]))
        else:
            print("Ambos empleados poseen el mismo sueldo.")

emple1=CargarEmpleado(1)
emple2=CargarEmpleado(2)
MejorPagado(emple1, emple2)