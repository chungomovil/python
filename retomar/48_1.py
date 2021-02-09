"""
Plantear una clase llamada Jugador.
Definir en la clase Jugador los atributos nombre y puntaje, y los métodos __init__, imprimir y pasar_tiempo (que debe reducir en uno la variable de clase).
Declarar dentro de la clase Jugador una variable de clase que indique cuantos minutos falta para el fin de juego (iniciarla con el valor 30)
Definir en el bloque principal dos objetos de la clase Jugador.
Reducir dicha variable hasta llegar a cero.
"""

import random

class Jugador:
    #Minutos del partido (al ser variable de clase cambia en todas las instancias simultaneamente aunque se modifique solo en una de ellas)
    minutos=30

    def __init__(self, num):
        self.nombre=""
        self.puntuacion=0
        self.numjugador=num

    def CargaDatos(self):
        condicion=False
        while condicion==False:
            print("nombre del jugador".upper(),"%s" % (self.numjugador))
            self.nombre=input("Nombre: ")
            if self.nombre=="":
                print("ERROR: Nombre incorrecto.")
            else:
                condicion=True
    
    #Genera un numero aleatorio del puntuaje del jugador
    def SumaPuntos(self):
        self.aleatorio=random.randint(0,10)
        self.puntuacion=self.puntuacion+self.aleatorio
        return self.puntuacion
    
    #Resta a la variable de clase (afecta a todas las instancias)
    def PasarTiempo(self):
        Jugador.minutos-=1


    def Imprimir(self):
        print("\n***jugador %s***" % (self.numjugador))
        print("Nombre: %s" % (self.nombre))
        print("--Ha sumado %s puntos.--" % (self.aleatorio))
        print("Puntuacion actual: %s" % (self.puntuacion))


jugador1=Jugador(1)
jugador2=Jugador(2)
jugador1.CargaDatos()
jugador2.CargaDatos()
while jugador1.minutos>0:
    print(30*"_")
    print("\ntiempo restante".upper(),"%s" % (jugador1.minutos-1))
    conteo1=jugador1.SumaPuntos()
    conteo2=jugador2.SumaPuntos()
    jugador1.PasarTiempo() # Con declararla una vez se modifican para el resto de instancias
    jugador1.Imprimir()
    jugador2.Imprimir()
    if jugador1.minutos==0:
        if conteo1>conteo2:
            print("\n***ganador jugador 1***".upper())
        elif conteo2>conteo1:
            print("\n***ganador jugador 2***".upper())
        else:
            print("***se ha producido un empate***".upper())
