"""
Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: inicializar los atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. El nombre de la clase llamarla Triangulo.
"""

class Triangulo:

    def CargaLado(self):
        condicion=False
        while condicion==False:
            print(60*"*")
            print("Introducir medidas de los lados del triangulo".upper())
            print(60*"*")
            self.lado1=float(input("Medida del lado 1 (cm): "))
            self.lado2=float(input("Medida del lado 2 (cm): "))
            self.lado3=float(input("Medida del lado 3 (cm): "))
            self.lado1=round(self.lado1, 2)
            self.lado2=round(self.lado2, 2)
            self.lado3=round(self.lado3, 2)
            if self.lado1<=0 or self.lado2<=0 or self.lado3<=0:
                print("ERROR: Todas las medidas deben de ser superior a 0.")
            else:
                condicion=True
        print(60*"*")
        print("\nMedidas del triangulo ingresado".upper())
        print("%s x %s x %s (en cm)." % (self.lado1, self.lado2, self.lado3))

    def LadoMayor(self):
        self.lados=[self.lado1,self.lado2,self.lado3]
        mayor=self.lados[0]
        for x in range(1, len(self.lados)):
            if mayor<self.lados[x]:
                mayor=self.lados[x]
        print("\nEl lado con mas longitud mide: %s cm" % (mayor))

    #LO HICE CON EL DOBLE BUCLE PARA ECONOMIZAR CONDICIONES Y LINEAS DE CODIGO
    #EN EL ENUNCIADO SOLO PIDE CALCULAR EQUILATERO, ESTE CALCULA TODOS LOS TIPOS
    def Tipo(self):
        similitud=0
        for x in range(len(self.lados)):
            contador=0
            for k in range(len(self.lados)):
               if self.lados[x]==self.lados[k]:
                   contador+=1
            if similitud<contador:
                similitud=contador
        if similitud==1:
            print("\nEl triangulo es de tipo escaleno.")
        if similitud==2:
            print("\nEl triangulo es de tipo isosceles.")
        if similitud==3:
            print("\nEl triangulo es de tipo equilatero.")


triangulo1=Triangulo()
triangulo1.CargaLado()
triangulo1.LadoMayor()
triangulo1.Tipo()

