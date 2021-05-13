"""
Realizar la carga de dos números enteros por teclado e imprimir su suma, luego preguntar si quiere seguir sumando valores.
Capturar la excepcion de entrada de datos no numericos.
"""

#Creamos el bucle
while True:
    #Creamos el algoritmo que se intentara realizar
    try:
        num1=int(input("Primer valor: "))
        num2=int(input("Segundo valor: "))
        suma=num1+num2
        print("%s + %s = %s" % (num1, num2, suma))
    #Si el resultado de lo anterior es la excepcion 'ValueError' muestra el mensaje (de este modo no se detiene el programa)
    except ValueError:
        print("Solo se admiten valores enteros.")
    #Opcion para continuar el bucle
    continuar=input("Ingresar nuevos valores [si (S) || no (N)]: ").upper()
    #Si pulsa 'n' el bucle se rompe y por consiguiente se termina el programa
    if continuar=="N":
        break




