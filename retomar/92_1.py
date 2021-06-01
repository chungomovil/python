"""
Declarar una clase que almacene el nombre y la edad de una persona. Definir un método que retorne True o False según si la persona es mayor de edad o no. Este método debe recibir como parámetro una función que al llamarla pasando la edad de la persona retornará si es mayor o no de edad.
Tener en cuenta que una persona es mayor de edad en Estados Unidos si tiene 21 o más años y en Argentina si tiene 18 o más años.
"""

#Creamos la clase
class Persona:

    #Creamos el metodo constructor y almacenamos los valores esenciales
    def __init__(self, valor1, valor2):
        self.nombre=valor1
        self.edad=valor2

    #Creamos la funcion de orden superior
    def MayorEdad(self, fn):
        #Retornamos el resultado de la operacion de la funcion que se le pase como referencia (SIEMPRE SE LE DEBE DE PASAR EL VALOR A CALCULAR)
        return fn(self.edad)

#Funcion para calcular mayor de edad en Argentina
def Mayor_Argentina(edad):
    if edad>=18:
        return True
    else:
        return False

#Funcion para calcular mayor de edad en EEUU
def Mayor_EEUU(edad):
    if edad>=21:
        return True
    else:
        return False

#Bucle
continuar=True
while continuar!=False:
    #Introducimos datos y los guardamos en un objeto
    nombre=input("Nombre: ").capitalize()
    edad=int(input("Edad: "))
    pais=input("Pulsar (A) Argentina || (E) Estados Unidos: ").upper()
    persona1=Persona(nombre, edad)
    #Elecciones del usuario
    if pais=="A":
        #Calculamos mayor de edad en una de las regiones e segun retorne True o False informamos al usuario
        if persona1.MayorEdad(Mayor_Argentina):
            print(f"{nombre} es mayor de edad en Argentina.")
        else:
            print(f"{nombre} es menor de edad en Argentina.")
    if pais=="E":
        if persona1.MayorEdad(Mayor_EEUU):
            print(f"{nombre} es mayor de edad en Estados Unidos.")
        else:
            print(f"{nombre} es menor de edad en Estados Unidos.")
    print(20*"-")
    #Eleccion del usuario por si desea continuar consultando edades
    continuar=input("Desea continuar (S) si || (N) no: ").upper()
    if continuar=="N":
        continuar=False



