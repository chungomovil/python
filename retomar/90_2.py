"""Imprimir los números de 1 a 5 en pantalla utilizando recursividad."""

#Crear funcion
def Entero(numero):
    #Crear caso base
    if numero>1:
        #Crear recursividad
        Entero(numero-1)
    #Imprimir secuencia SEGUN EL ORDEN DE LIBERACION en la memoria
    print(numero)
    
#Llamar a la funcion
Entero(5)
