"""Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
3) Imprimir las dos listas generadas."""

def CargaValor():
    valores=[]
    for x in range(1, 11):
        valor=int(input("Introducir valor entero [%s]: " % (x)))
        valores.append(valor)
    return valores

def Diferenciar(numeros):
    pos=[]
    neg=[]
    for x in range(len(numeros)):
        if numeros[x]>=0:
            pos.append(numeros[x])
        else:
            neg.append(numeros[x])
    return [pos, neg]

def Decorar(titulo, mensaje):
    print("*******************************")
    print(titulo.upper())
    print(mensaje)
    print("*******************************")

numeros=CargaValor()
positivos, negativos=Diferenciar(numeros)
Decorar("valores introducidos", numeros)
Decorar("valores positivos", positivos)
Decorar("valores negativos", negativos)
