"""Definir una lista con 5 valores flotantes con distintas cantidades de decimales. Mostrar los números solo con dos decimales.(EXTRA)Imprimir su suma. MOSTRAR SALIDA CON f-strings."""

numeros=[10.2, 56.123435, -1, 800.23239, 12]

#Recorremos la lista
for valor in numeros:
    #Imprimimos cada valor de la lista, especificando el espacio que ocupará y los decimales que tendrá
    print(f"{valor:10.2f}")
print(10*"-")
#(EXTRA)Imprimimos la suma, especificando el espacio que ocupará y los decimales que tendrá
print(f"{sum(numeros):10.2f}")

