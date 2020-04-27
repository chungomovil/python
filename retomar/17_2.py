"""
En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.
"""

nombres=[]
notas=[]
mejores=0

for x in range(4):
    nota=-1
    validacion=False
    while validacion==False:
        nombre=input("introducir nombre: ")
        validacion=nombre.isalpha() # isalpha devuelve un True si todos los caracteres son alfabeticos, de lo contrario devuelve False
    while nota<0 or nota>10:
        nota=float(input("introducir nota: "))
        if nota<0 or nota>10:
            print("Solo notas del 0 al 10")
    nombres.append(nombre)
    notas.append(nota)

print("\n----------------------\nLISTADO DE ALUMNOS\n----------------------")
for x in range(len(nombres)):
    print(nombres[x], end=": ")
    print(notas[x])
    if notas[x]>=8:
        print("Muy Bueno\n")
        mejores+=1
    else:
        if notas[x]>=4:
            print("Bueno\n")
        else:
            print("Insuficiente\n")

print("----------------------\nHay un total de",mejores,"alumnos con notas 'Muy Buenas'.")
