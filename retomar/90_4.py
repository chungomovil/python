"""Implementar un método recursivo para ordenar los elementos de una lista."""

#Creamos la funcion
def Ordenar(lista, longitud):
    #Caso base
    if longitud>0:
        #Bucle para organizar
        for x in range(longitud-1):
            if lista[x]>lista[x+1]:
                aux=lista[x]
                lista[x]=lista[x+1]
                lista[x+1]=aux
        #Creamos la recursividad
        Ordenar(lista, longitud-1)
    #Retornamos la lista ordenada de menor a mayor
    return lista

#Creamos la lista
lista=[99, 15, 23, -18, 0]
#Obtenemos longitud de la lista para la recursividad
longitud=len(lista)
#Imprimimos lista sin ordenar
print(f"LISTA SIN ORDENAR\n{lista}\n")
#Llamamos e imprimimos el resultado de la funcion
Ordenar(lista, longitud)
print(f"LISTA ORDENADA\n{lista}")
