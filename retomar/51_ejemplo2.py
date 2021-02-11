"""
Plantear una clase Rectangulo. Definir dos atributos (ladomenor y ladomayor).
Redefinir el operador == de tal forma que tengan en cuenta la superficie del rectángulo. Lo mismo hacer con todos los otros operadores relacionales.
"""

class Rectangulo:
    #Cargar atributos esenciales
    def __init__(self, ladomayor, ladomenor):
        self.ladomayor=ladomayor
        self.ladomenor=ladomenor
    #Retornar superficie
    def Superficie(self):
        return self.ladomenor*self.ladomayor
    #Metodo para retornar cadena de valores
    def __str__(self):
        return str(self.Superficie())
    #Metodo de igualdad
    def __eq__(self, objeto2):
        if self.Superficie()==objeto2.Superficie():
            return True
        else:
            return False
    #Metodo de diferencia
    def __ne__(self, objeto2):
        if self.Superficie()!=objeto2.Superficie():
            return True
        else:
            return False
    #Metodo de superioridad
    def __gt__(self, objeto2):
        if self.Superficie()>objeto2.Superficie():
            return True
        else:
            return False
    #Metodo de igualdad o superioridad
    def __ge__(self, objeto2):
        if self.Superficie()>=objeto2.Superficie():
            return True
        else:
            return False
    #Metodo de inferioridad
    def __lt__(self, objeto2):
        if self.Superficie()<objeto2.Superficie():
            return True
        else:
            return False
    #Metodo de igualdad o inferioridad
    def __le__(self, objeto2):
        if self.Superficie()<=objeto2.Superficie():
            return True
        else:
            return False

#BLOQUE PRINCIPAL
rectangulo1=Rectangulo(25, 90)
rectangulo2=Rectangulo(19, 110)
print(30*"*")
print("Superficie del rectangulo 1: %s cm" % (rectangulo1))
print("Superficie del rectangulo 2: %s cm" % (rectangulo2))
#Debido a los metodos nombrados anteriormente, en este apartado solo nos limitamos a llamarlos
if rectangulo1==rectangulo2:
    print("Ambos rectangulos poseen la misma superficie.")
elif rectangulo1>rectangulo2:
    print("La superficie del primer rectangulo es mayor.")
else:
    print("La superficie del segundo rectangulo es mayor.")


