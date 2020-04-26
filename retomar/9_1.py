"""Escribir un programa que solicite ingresar 10 notas de alumnos y 
nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores."""

x=1
menor=0
mayor=0

while x<=10:
    nota=float(input("introducir nota: "))
    if nota<7:
        menor+=1
    else:
        mayor+=1
    x+=1

if menor==0:
    print("todas las notas son superiores a 7")
else:
    if mayor==0:
        print("todas las notas son inferiores a 7")
    else:
        print("hay un total de",menor,"notas inferiores a 7")
        print("hay un total de",mayor,"notas superiores a 7")