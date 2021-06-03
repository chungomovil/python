"""Definir una lista con 5 valores enteros, luego a partir de la primer lista generar una segunda lista con los valores elevados al cuadrado. USAR COMPRESION DE LISTA."""

#Creamos la lista principal
lista1=[9, 81, -19, 0, 998]
#Resolvemos el problema con comprension de lista
lista2=[elemento*elemento for elemento in lista1]
#Mostramos resultado
print(f"Lista principal: {lista1}\nLista resultante: {lista2}")
