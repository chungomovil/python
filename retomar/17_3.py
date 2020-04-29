"""
Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. Mostrar esta tercer lista.
"""

lista1=[]
lista2=[]
lista3=[]
x=0

print("----------------------\nVALORES DE LA PRIMERA LISTA\n----------------------\n")
for x in range(4):
    valor=int(input("Introducir valor: ")) #para hacer que solo acepte numeros enteros probar con Try y Except (es mas avanzado por eso lo exclui) con isdigit() solo acepta positivos enteros
    lista1.append(valor)

print("\n----------------------\nVALORES DE LA SEGUNDA LISTA\n----------------------\n")
for x in range(len(lista1)):
    valor=int(input("Introducir numero: "))
    lista2.append(valor)

print("\n----------------------\nLISTAS SUMADAS\n----------------------\n")
for x in range(len(lista1)):
    suma=lista1[x]+lista2[x]
    lista3.append(suma)
print(lista3)

