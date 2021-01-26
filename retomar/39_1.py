"""
Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre.
El operador debe tratar de adivinar el número ingresado.
Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al generado o "El número aleatorio es mayor" o "El número aleatorio es menor".
Mostrar cuando gana el jugador cuantos intentos necesitó.
"""

import random

def GenerarNum():
    numero=random.randint(1, 100)
    return numero

def ComenzarJuego(numero):
    teclado=0
    intento=1
    while teclado!=numero:
        print(30*"*")
        print("rango entre 1 y 100".upper())
        print(30*"*")
        teclado=int(input("Intenta acertar el numero aleatorio: "))
        if teclado==numero:
            print("ENHORABUENA: Has acertado el numero secreto [%s]." % (numero))
            print("Has necesitado %s intentos." % (intento))
        #PARTE EXTRA: Da indicaciones de si te vas acercando al valor
        else:
            print("Has fallado.")
            transformar=numero-teclado
            #Convierte el valor siempre en positivo
            if transformar<0:
                transformar=transformar*-1
            else:
                transformar=transformar*1
            #Condiciones segun se vaya acercando
            if transformar>50:
                print("No te has acercado lo mas minimo al valor secreto.")
            else:
                if transformar>30:
                    print("Te has acercado minimamente al valor secreto.")
                else:
                    if transformar>15:
                        print("Te has acercado medianamente al valor secreto.")
                    else:
                        if transformar>5:
                            print("Has estado cerca del valor secreto.")
                        else:
                            print("Casi aciertas el valor secreto.")
            intento+=1

valor=GenerarNum()
ComenzarJuego(valor)
