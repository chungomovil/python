"""Definir una función que cargue una lista con palabras y la retorne.
Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres."""

def Decorar(mensaje):
    print(len(mensaje)*"*")
    print(mensaje.upper())
    print(len(mensaje)*"*")

def CargaPalabra():
    palabras=[]
    palabra=""
    while palabra!="Q" or len(palabras)==0:
        palabra=input("Introducir palabra (Presionar 'Q' para terminar): ")
        palabra=palabra.upper()
        if palabra!="Q":
            palabras.append(palabra)
        if len(palabras)==0:
            print("--> Introducir al menos una palabra.")
    return palabras

def MasCaracteres(palabras):
    Decorar("Palabras con mas de 5 caracteres")
    for palabra in palabras: # USANDO LA FORMA ALTERNATIVA DE RECORRER LISTAS Y TUPLAS
        if len(palabra)>=5:
            print(palabra)

listado=CargaPalabra()
Decorar("Palabras introducidas: %s" % (listado))
MasCaracteres(listado)
