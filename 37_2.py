"""
Cargar una cadena por teclado luego:
1) Imprimir los dos primeros caracteres.
2) Imprimir los dos últimos
3) Imprimir todos menos el primero y el último caracter.
"""

def Decorar(texto):
    print(len(texto)*"*")
    print(texto.upper())
    print(len(texto)*"*")

def CargaMensaje(mensaje):
    Decorar("primeros 2 caracteres: %s" % (mensaje[:2]))
    Decorar("ultimos 2 caracteres: %s" % (mensaje[len(mensaje)-2:]))
    Decorar("del segundo caracter al penultimo: %s" % (mensaje[1:len(mensaje)-1]))

mensaje=""
while mensaje=="":
    mensaje=input("Introducir una frase: ")
    if mensaje=="":
        print("ERROR: El texto no puede estar vacio.")
    else:
        CargaMensaje(mensaje)
