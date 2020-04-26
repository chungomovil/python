"""Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje
 "Promocionado"."""

nota1=int(input("nota primer trimestre: "))
nota2=int(input("nota segundo trimestre: "))
nota3=int(input("nota tercer trimestre: "))

suma=nota1+nota2+nota3
promedio=suma/3
promedio=round(promedio,2)

if promedio>=7:
    print("el alumno ha promocionado con una nota promedio de",promedio)

else:
    print("el alumno ha suspendido con una nota promedio de",promedio,"siendo inferior a 7")