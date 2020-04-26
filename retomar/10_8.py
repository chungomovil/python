"""Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor."""

sumam=0
promm=0
sumat=0
promt=0
suman=0
promn=0
count=0

print("------------------\nTURNO DE MANIANA\n------------------")

for x in range(1,6):
    edad=int(input("introducir edad: "))
    sumam=sumam+edad
    count+=1

promm=sumam/count
count=0

print("------------------\nTURNO DE TARDE\n------------------")

for x in range(1,7):
    edad=int(input("introducir edad: "))
    sumat=sumat+edad
    count+=1

promt=sumat/count
count=0

print("------------------\nTURNO DE NOCHE\n------------------")

for x in range(1,12):
    edad=int(input("introducir edad: "))
    suman=suman+edad
    count+=1

promn=suman/count

print("\n-------------------------\nPROMEDIO\n-------------------------\n")
print("MANIANA:",round(promm,2))
print("TARDE:",round(promt,2))
print("NOCHE:",round(promn,2))
print("\n-----------------------------------------------------------\n")
if promm>promt and promm>promn:
    print("el turno con mayor promedio de edad es el turno de maniana")
else:
    if promt>promn:
        print("el turno con mayor promedio de edad es el turno de tarde")
    else:
        print("el turno con mayor promedio de edad es el turno de noche")