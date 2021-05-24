"""Definir una lista con 5 valores enteros. Mostrar los 5 valores formateados a derecha junto a su suma. MOSTRAR SALIDA CON f-strings."""

numeros=[5, 15, 88, -10, 111]

#Recorremos la lista
for valor in numeros:
    #Imprimimos cada valor con f-string y establecemos la cantidad de espacios que ocupará el texto
    print(f"{valor:10}")
print(10*"-")
#Sumamos los valores de la lista, imprimimos con f-string y establecemos los espacios que ocupará
print(f"{sum(numeros):10}")
