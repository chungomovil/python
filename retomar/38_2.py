"""
Confeccionar un programa con las siguientes funciones:
1) Cargar una lista con 5 palabras.
2) Intercambiar la primer palabra con la última.
3) Imprimir la lista
"""

def CargaLista():
    palabras=[]
    for x in range(5):
        palabra=""
        while len(palabra)<=1:
            print("palabra numero".upper(),"[%s]" % (x+1))
            palabra=input("Introducir palabra: ")
            if len(palabra)<=1:
                print("ERROR: La longitud de la palabra debe de ser superior a 1 caracter.")
        palabras.append(palabra)
    print(20*"*")
    print("palabras introducidas".upper())
    print(20*"*")
    for sentencia in palabras:
        print(sentencia)
    return palabras

def OperacionPalabras(palabras):
    aux=palabras[0]
    palabras[0]=palabras[-1]
    palabras[-1]=aux
    return (palabras)

def Imprimir(palabras):
    print(20*"*")
    print("nueva lista de palabras".upper())
    print(20*"*")
    for palabra in palabras:
        print(palabra)

listado=CargaLista()
OperacionPalabras(listado)
Imprimir(listado)
