"""Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el número de documento del alumno. Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota.
Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas."""

def CargaAlumno():
    alumnos={}
    for x in range(3):
        print(15*"*")
        print("DATOS DEL ALUMNO: %s" % (x+1))
        print(15*"*")
        dni=""
        while dni=="":
            dni=input("DNI alumno: ").upper()
            if dni=="":
                print("ERROR: DNI del alumno incorrecto.")
        asignatura=""
        contador=1
        asignaturas=[]
        while asignatura!="Q":
            print("--> Asignatura numero [%s]: " % (contador))
            print(15*"-")
            asignatura=input("Nombre asignatura('Q' omitir): ").upper()
            if asignatura=="":
                print("ERROR: Nombre de asignatura o nota incorrecta.")
            else:
                if asignatura=="Q" and contador==1:
                    print("--> ERROR: Introducir como minimo una asignatura.")
                    asignatura=""
                else:
                    if asignatura!="Q":
                        nota=float(input("Nota: "))
                        nota=round(nota, 2)
                        if nota<0 or nota>10:
                            print("--> ERROR: La nota debe estar comprendida entre 0 y 10.")
                        else:
                            asignaturas.append((asignatura, nota)) #RECORDAR EMPAQUETAR EN UNA TUPLA YA QUE NO SE PUEDE HACER APPEND DE VARIOS VALORES SIN EMPAQUETAR
                            contador+=1
        alumnos[dni]=asignaturas
    return alumnos

def ListarAlumnos(alumnos):
    print(15*"*")
    print("LISTADO DE ALUMNOS")
    print(15*"*")
    for alumno in alumnos:
        print("DNI: %s" % (alumno))
        for asignatura,nota in alumnos[alumno]:
            print("Asignatura: %s" % (asignatura))
            print("Nota: %s" % (nota))
        print(15*"-")

def BuscarAlumno(alumnos):
    busqueda=""
    while busqueda!="Q":
        busqueda=input("Buscar por DNI ('Q' terminar): ").upper()
        if busqueda!='Q':
            if busqueda in alumnos:
                print("DNI: %s" % (busqueda))
                for asignatura,nota in alumnos[busqueda]:
                    print("Asignatura: %s" % (asignatura))
                    print("Nota: %s" % (nota))
            else:
                print("El usuario con DNI '%s' no se encuentra." % (busqueda))

estudiantes=CargaAlumno()
ListarAlumnos(estudiantes)
BuscarAlumno(estudiantes)