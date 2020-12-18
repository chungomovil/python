"""En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio."""

def cargasueldo():
    sueldos=[]
    x=1
    while x<=10:
        sueldo=float(input("Introducir sueldo [%s]: " % (x)))
        if sueldo>100:
            sueldos.append(round(sueldo, 2))
            x+=1
        else:
            print("--> El sueldo debe de ser superior a 100.")
    return sueldos

def sueldosmayores(lista):
    mayores=[]
    for x in range(len(lista)):
        if lista[x]>4000:
            mayores.append(lista[x])
    return mayores

def sueldospromedio(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    promedio=suma/len(lista)
    return round(promedio, 1)

def sueldosmenores(lista, promedio):
    menores=[]
    for x in range(len(lista)):
        if lista[x]<promedio:
            menores.append(lista[x])
    return menores

#ESTA FUNCION EQUIVALE AL APARTADO '2' DEL ENUNCIADO
def decorar(titulo, mensaje):
    print("*********************")
    print(titulo.upper())
    print(mensaje)
    print("*********************")


listasueldo=cargasueldo()
decorar("sueldos introducidos", listasueldo)
mayores=sueldosmayores(listasueldo)
decorar("SUELDOS mayores a 4.000", mayores)
prom=sueldospromedio(listasueldo)
decorar("El sueldo promedio es", prom)
menor=sueldosmenores(listasueldo, prom)
decorar("Sueldos menores al promedio (%s)" % (prom), menor)
