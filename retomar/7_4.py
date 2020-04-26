"""Un postulante a un empleo, realiza un test de capacitación, 
se obtuvo la siguiente información: cantidad total de preguntas que se le realizaron 
y la cantidad de preguntas que contestó correctamente. 
Se pide confeccionar un programa que ingrese los dos datos por teclado e informe 
el nivel del mismo según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:
	Nivel máximo:	Porcentaje>=90%.
	Nivel medio:	Porcentaje>=75% y <90%.
	Nivel regular:	Porcentaje>=50% y <75%.
	Fuera de nivel:	Porcentaje<50%."""

preguntas=int(input("total preguntas del examen: "))
aciertos=int(input("total aciertos: "))
porcentaje=(aciertos/preguntas)*100
porcentaje=round(porcentaje,2)

if porcentaje<50:
    print("el nivel minimo para aprobar es del 50% y el candidato obtuvo ",porcentaje,"%; ha suspendido.",sep="")
else:
    if porcentaje>=50 and porcentaje<75:
        print("el nivel regular esta comprendido con porcentajes de acierto entre 50% y 75%, el candidato obtuvo ",porcentaje,"%; calificacion regular.",sep="")
    else:
        if porcentaje>=75 and porcentaje<90:
            print("el nivel medio esta comprendido con porcentajes de acierto entre el 75% y el 90%, el candidato obtuvo ",porcentaje,"%; calificacion media.",sep="")
        else:
            print("el nivel maximo esta comprendido con porcentajes de acierto superiores al 90%, el candidato obtuvo ",porcentaje,"%; calificacion maxima.",sep="")    