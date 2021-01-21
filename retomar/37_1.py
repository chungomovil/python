"""
Realizar un programa que contenga las siguientes funciones:
1) Carga de una lista de 10 enteros.
2) Recibir una lista y retornar otra con la primer mitad (se sabe que siempre llega una lista con una cantidad par de elementos)
3) Imprimir una lista.
"""

def CargaNumeros():
    numeros=[]
    for x in range(10):
        numero=int(input("Cargar valor [%s]: " % (x+1)))
        numeros.append(numero)
    return numeros

def DivideLista(numeros):
    limite=int(len(numeros)/2) #PONER INT YA QUE AL DIVIDIR EL RESULTADO SE TRADUCE A FLOAT Y SELECTOR DE POSICIONES DE LA LISTA SOLO ACEPTA ENTEROS
    numeros_segunda=[]
    numeros_segunda.append(numeros[:limite])
    del(numeros[:limite])
    return (numeros, numeros_segunda)

def ImprimirListas(numerosprimera, numerossegunda):
    print(20*"*")
    print("primera parte de la lista".upper())
    print(20*"*")
    print(numerosprimera)
    print(20*"*")
    print("segunda parte de la lista".upper())
    print(20*"*")
    print(numerossegunda)


listanumeros=CargaNumeros()
parte1, parte2=DivideLista(listanumeros)
ImprimirListas(parte1, parte2)
