"""En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
realizar un programa que lea los sueldos que cobra cada empleado e informe 
cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. 
Además el programa deberá informar el importe que gasta la empresa en sueldos al personal."""

x=1
sueldominimo=0
sueldomaximo=0
suma=0

while x<=5:
    sueldo=float(input("introducir salario: "))
    if sueldo<100 or sueldo>500:
        print("solo sueldos comprendidos entre 100 y 500")
    else:
        if sueldo<=300:
            sueldominimo+=1
        else:
            sueldomaximo+=1
        suma=suma+sueldo
        x+=1

print("salarios entre 100 y 300 (euros):",sueldominimo)
print("salarios superiores a 300 (euros):",sueldomaximo)
print("-----------------------------------")
print("suma total salarios: ",round(suma,2),"euros",sep="")