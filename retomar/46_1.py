"""
Plantear una clase Club y otra clase Socio.
La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el club (en años).
En el método __init__ de la clase Socio pedir la carga por teclado del nombre y su antigüedad.
La clase Club debe tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre del socio con mayor antigüedad en el club.
"""

class Socio:

    def __init__(self):
        condicion=False
        #Controlar que no se introduzcan numeros negativos ni campos en blanco
        while condicion==False:
            print("datos del socio".upper())
            print(30*"-")
            self.nombre=input("Nombre: ")
            self.estancia=int(input("Antiguedad (en anios): "))
            print("\n")
            if self.nombre!="" and self.estancia>0:
                condicion=True
            else:
                print("--> Alguno de los datos es incorrecto.")
    
    def MostrarSocio(self):
        print("Nombre: %s" % (self.nombre.capitalize()))
        print("Antiguedad: %s anios" % (self.estancia))
        print("\n")

    def RetornarAntiguedad(self):
        return self.estancia

class Club:

    def __init__(self):
        self.socio1=Socio()
        self.socio2=Socio()
        self.socio3=Socio()
        self.socio1.MostrarSocio()
        self.socio2.MostrarSocio()
        self.socio3.MostrarSocio()

    def MasAntiguo(self):
        print("El socio con mas antiguedad es")
        print(30*"-")
        #Exportamos el metodo correspondiente de la clase socio
        if self.socio1.RetornarAntiguedad()==self.socio2.RetornarAntiguedad() or self.socio1.RetornarAntiguedad()==self.socio3.RetornarAntiguedad() or self.socio2.RetornarAntiguedad()==self.socio3.RetornarAntiguedad(): #controlamos si hay varios con la misma antiguedad
            print("Dos o mas socios poseen la misma antiguedad.")
        elif self.socio1.RetornarAntiguedad()>self.socio2.RetornarAntiguedad() and self.socio1.RetornarAntiguedad()>self.socio3.RetornarAntiguedad():
            self.socio1.MostrarSocio()
        elif self.socio2.RetornarAntiguedad()>self.socio3.RetornarAntiguedad():
            self.socio2.MostrarSocio()
        else:
            self.socio3.MostrarSocio()

#iniciamos el programa
Iniciar=Club()
Iniciar.MasAntiguo()
        


