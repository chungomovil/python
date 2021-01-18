"""
Crear un diccionario en Python para almacenar los datos de empleados de una empresa. La clave será su número de legajo y en su valor almacenar una lista con el nombre, profesión y sueldo.
Desarrollar las siguientes funciones:
1) Carga de datos de empleados.
2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"""

def CargaEmple():
    cant_emple=0
    while cant_emple<=0:
        cant_emple=int(input("Numero de empleados: "))
        if cant_emple<=0:
            print("--> El valor debe de ser superior a 0.")
    empleados={}
    for x in range(cant_emple):
        print(15*"*")
        print("empleado numero [".upper(), x+1,"]",sep="")
        print(15*"*")
        dni=""
        while dni=="":
            dni=input("DNI: ").upper()
            if dni=="":
                print("--> Numero de DNI incorrecto.")
        condicion=False
        empleado=[]
        while condicion==False:
            emple_nom=input("Nombre: ").capitalize()
            emple_prof=input("Profesion: ").upper()
            emple_sueldo=float(input("Sueldo: "))
            emple_sueldo=round(emple_sueldo, 2)
            if emple_nom=="" or emple_prof=="" or emple_sueldo<50:
                print("ERROR: Uno de los datos introducidos es incorrecto (salario minimo: 50€).")
            else:
                empleado.append([emple_nom,emple_prof,emple_sueldo])
                condicion=True
        empleados[dni]=empleado
    return empleados

def ModificarSueldo(empleados):
    busqueda=""
    print(15*"*")
    print("modificar salario".upper())
    print(15*"*")
    while busqueda!="Q":
        busqueda=input("Buscar por DNI ('Q' omitir): ").upper()
        if busqueda!="Q":
            if busqueda in empleados:
                condicion=False
                while condicion==False:
                    nuevo_sueldo=float(input("Nuevo salario para %s: " % (empleados[busqueda][0][0]))) #DIRIGIRSE A UBICACION EN DICCIONARIO DONDE ESTA EL NOMBRE
                    nuevo_sueldo=round(nuevo_sueldo, 2)
                    if nuevo_sueldo<50:
                        print("--> Salario incorrecto (minimo 50€).")
                    else:
                        condicion=True
                        empleados[busqueda][0][2]=nuevo_sueldo
                        print(15*"-")
                        print("cambio realizado".upper())
                        print(15*"-")
                        print("DNI: ",busqueda,sep="")
                        for nombre,profesion,salario in empleados[busqueda]:
                            print("Nombre: ",nombre,sep="")
                            print("Profesion: ",profesion,sep="")
                            print("Salario: ",salario," €",sep="")
            else:
                print("El empleado con DNI ", busqueda, " no se encuentra.",sep="")

def ImprimirAnalista(empleados):
    print(15*"*")
    print("empleados analistas de sistemas".upper())
    print(15*"*")
    for empleado in empleados:
        if empleados[empleado][0][1]=="ANALISTA DE SISTEMAS":
            print("DNI: ",empleado,sep="")
            for nombre,profesion,sueldo in empleados[empleado]:
                print("Nombre: ",nombre,sep="")
                print("Profesion: ",profesion,sep="")
                print("Salario: ",sueldo," €",sep="")

plantilla=CargaEmple()
print(plantilla)
ModificarSueldo(plantilla)
ImprimirAnalista(plantilla)