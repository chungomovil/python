"""Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. 
Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar."""

puntos=0
coordenadax=0
coordenaday=0
cuadrante1=0
cuadrante2=0
cuadrante3=0
cuadrante4=0
centro=0

while puntos<=0:
    puntos=int(input("cuantos puntos desea ingresar: "))

for x in range(1,puntos+1):
    print("\n--------------\ncoordenadas del punto",x)
    coordenadax=int(input("posicion de X: "))
    coordenaday=int(input("posicion de Y: "))
    if coordenadax>0 and coordenaday>0:
        cuadrante1+=1
    else:
        if coordenadax>0 and coordenaday<0:
            cuadrante2+=1
        else:
            if coordenadax<0 and coordenaday<0:
                cuadrante3+=1
            else:
                if coordenadax<0 and coordenaday>0:
                    cuadrante4+=1
                else:
                    centro+=1

print("\n-----------------------------\nTOTALES\n-----------------------------\n")
print("cuadrante 1:",cuadrante1,"puntos")
print("cuadrante 2:",cuadrante2,"puntos")
print("cuadrante 3:",cuadrante3,"puntos")
print("cuadrante 4:",cuadrante4,"puntos")
print("centro:",centro,"puntos")
    
    