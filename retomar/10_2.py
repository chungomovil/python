"""Desarrollar un programa que solicite la carga de 10 números 
e imprima la suma de los últimos 5 valores ingresados."""

suma=0

for x in range (10):
    num=int(input("introducir valor: "))
     
    if x>=5:
        suma=suma+num

print("la suma de los ultimos 5 valores ingresados es:",suma)