"""Realizar un programa que pida cargar una fecha cualquiera, 
luego verificar si dicha fecha corresponde a Navidad."""

dia=-1
mes=-1
anio=-1

print("introducir fecha (dia-mes-anio)")

while dia<0 or dia>31:
    dia=int(input("introducir dia: "))
while mes<0 or mes>12:
    mes=int(input("introducir mes: "))
    if dia>29 and mes==2:
        dia=28
        print("el dia ha sido reemplazado por",dia)
while anio<0:
    anio=int(input("introducir anio: "))

print("fecha introducida:",dia,"-",mes,"-",anio,end="")

if dia==24 and mes==12:
    print(" hoy es navidad :)")