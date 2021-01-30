"""
Confeccionar una clase que permita carga el nombre y la edad de una persona. Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)
"""

class Persona:

    def CargaDatos(self, nom, edad):
        self.nombre=nom
        self.edad=edad

    def Imprimir(self):
        print(30*"*")
        print("datos introducidos".upper())
        print(30*"*")
        print("nombre:".capitalize(),self.nombre)
        print("edad:".capitalize(),self.edad)

    def CalcularEdad(self):
        if self.edad>=18:
            print("-->","es mayor de edad.".capitalize())
        else:
            print("-->","es menor de edad.".capitalize())

persona1=Persona()
persona1.CargaDatos("Carla", 22)
persona1.Imprimir()
persona1.CalcularEdad()
persona2=Persona()
persona2.CargaDatos("Eustaquio", 15)
persona2.Imprimir()
persona2.CalcularEdad()
