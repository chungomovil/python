import mayormenor

def Decorar(mensaje):
    print(len(mensaje)*"*")
    print(mensaje.upper())
    print(len(mensaje)*"*")

eleccion=""
while eleccion!="Q":
    Decorar("calcular numeros dos numeros")
    eleccion=input("Introducir 'S' para mayor 'I' para menor o 'Q' para cerrar: ")
    eleccion=eleccion.upper()
    if eleccion=='S':
        Decorar("calcular mayor")
        num1=float(input("Introducir primer valor: "))
        num2=float(input("Introducir segundo valor: "))
        print("El mayor es: %s" % (mayormenor.mayor(num1,num2)))
    if eleccion=='I':
        Decorar("calcular menor")
        num1=float(input("Introducir primer valor: "))
        num2=float(input("Introducir segundo valor: "))
        print("El menor es: %s" % (mayormenor.menor(num1,num2)))

