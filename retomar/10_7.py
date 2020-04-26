"""Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares."""

negativos=0
positivos=0
multiplos=0
suma=0

for x in range(1,11):
    num=int(input("ingresar valor: "))
    if num<0:
        negativos+=1
    else:
        positivos+=1
        suma=suma+num
        if num%15==0 and num>0:
            multiplos+=1

print("\n----------------------\nTOTALES\n----------------------\n")
print("negativos:",negativos)
print("positivos:",positivos)
print("multiplos:",multiplos)
print("suma:",suma)