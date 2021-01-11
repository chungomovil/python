"""Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en la primer componente el nombre del candidato y en la segunda componente cargar una lista con componentes de tipo tupla con el nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado, pero si se cargaran por asignación tendría una estructura similar a esta:
candidatos=[ ("juan",[("cordoba",100),("buenos aires",200)]) , ("ana", [("cordoba",55)]) , ("luis", [("buenos aires",20)]) ]
1) Función para cargar todos los candidatos, sus nombres y las provincias con los votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias."""

def Decorar(mensaje):
    print(len(mensaje)*"*")
    print(mensaje.upper())
    print(len(mensaje)*"*")

def CargaCandidatos():
    traduccion=["Primer", "Segundo", "Tercer"]
    candidatos=[]
    for x in range(3):
        Decorar("%s candidato" % (traduccion[x]))
        nombre_candi=input("Nombre: ")
        num=0
        while num<=0 or num>5:
            num=int(input("--> Numero de provincias (Maximo 5): "))
        provincias=[]
        for y in range(num):
            Decorar("Provincia numero [%s]" % (y+1))
            provincia_nom=input("Nombre de provincia: ")
            delimitador=False
            while delimitador==False:
                votos=int(input("Cantidad de votos: "))
                if votos<=0:
                    print("--> El valor minimo debe ser superior o igual a 1.")
                else:
                    delimitador=True
            provincias.append((provincia_nom,votos))
        candidatos.append((nombre_candi,provincias))
    return candidatos

def Imprimir(candidatos):
    Decorar("Lista de candidatos")
    for x in range(len(candidatos)):
        print("Nombre: %s" % (candidatos[x][0]).upper())
        print(19*"-")
        for y in range(len(candidatos[x][1])): #Para entrar en la lista que posee la tupla provincias y votos
            print("Provincia: %s" % (candidatos[x][1][y][0]))
            print("Votos: %s" % (candidatos[x][1][y][1]))
            print(10*"-")

#FUNCION EXTRA
def Elegido(candidatos):
    totales=[]
    for x in range(len(candidatos)):
        suma=0
        for y in range(len(candidatos[x][1])):
            suma=suma+candidatos[x][1][y][1]
        totales.append(suma)
    mayor=totales[0]
    posicion=0
    for x in range(1,len(totales)):
        if mayor<totales[x]:
            mayor=totales[x]
            posicion=x
    return (posicion,mayor)

candidatos=CargaCandidatos()
Imprimir(candidatos)
posicion,votos=Elegido(candidatos)
Decorar("el candidato elegido ha sido %s\nCon un total de %s votos." % (candidatos[posicion][0], votos))
