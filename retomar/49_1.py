"""
Desarrollar un programa que implemente una clase llamada Jugador.
Definir como atributos su nombre y puntaje.
Codificar el método especial __str__ que retorne el nombre y si es principiante (menos de 1000 puntos) o experto (1000 o más puntos)
"""

import random

class Jugador:

    #Inicializar variables esenciales
    def __init__(self):
        self.nombre=""
        self.puntuacion=0

    #Retornar en forma de string
    def __str__(self):
        self.puntuacionfinal=self.RetornarPuntuacion() #Usar puntuacion actualizada, tambien se puede hacer sin esta funcion ya que depende del orden que se nombre en el bloque principal
        if self.puntuacionfinal<1000:
            return "Puntuacion: "+str(self.puntuacionfinal)+"\nNivel: Principiante"
        elif self.puntuacionfinal<7000:
            return "Puntuacion: "+str(self.puntuacionfinal)+"\nNivel: Intermedio"
        else:
            return "Puntuacion: "+str(self.puntuacionfinal)+"\nNivel: Experto"

    #Cargar datos del jugador
    def CargarDatos(self):
        condicion=False
        while condicion==False:
            print(30*"*")
            print("NOMBRE DEL JUGADOR")
            print(30*"*")
            self.nombre=input("Nombre: ")
            if self.nombre=="":
                print("ERROR: Nombre vacio.")
            else:
                condicion=True
        self.puntuacion=random.randint(1,9999)
    
    #Retornar puntuacion actualizada
    def RetornarPuntuacion(self):
        return self.puntuacion
    

#BLOQUE PRINCIPAL

jugador1=Jugador()
condicion="S"
while condicion=="S":
    jugador1.CargarDatos()
    print(jugador1)
    condicion=input("Probar nuevamente 'S'(si) 'N'(no): ")
    condicion=condicion.upper()
