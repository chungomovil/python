"""
Confeccionar una función de orden superior que reciba un String y una función con un parámetro de tipo String que retorna un Boolean.
La función debe analizar cada elemento del String llamando a la función que recibe como parámetro, si retorna un True se agrega dicho caracter al String que se retornará.

En el bloque principal definir un String con una cadena cualquiera.

Llamar a la función de orden superior y pasar expresiones lambdas para filtrar y generar otro String con las siguientes restricciones:

Un String solo con las vocales
Un String solo con los caracteres en minúsculas
Un String con todos los caracteres no alfabéticos
"""

#Creamos la funcion de orden mayor
def Analizar(oracion, fn):
    #Creamos una variable nueva para la cadena que se resultante
    nuevaoracion=""
    #Recorremos la cadena principal
    for caracter in oracion:
        #Retornamos booleano
        if fn(caracter):
            #Agregamos el caracter a la nueva cadena en caso de ser True
            nuevaoracion=nuevaoracion+caracter
    #Retornamos nueva cadena
    return nuevaoracion


#Creamos la cadena a analizar
frase="Esta 3ra una Vez una CASA QUE est4ba abandonada y la OKUPAR0N. F1n."

#Creamos las lambdas con los filtros pertinentes
vocales=Analizar(frase, lambda caracter: caracter=="A" or caracter=="E" or caracter=="I" or caracter=="O" or caracter=="U"
                                or caracter=="a" or caracter=="e" or caracter=="i" or caracter=="o" or caracter=="u")
print(f"La frase con solo vocales quedaria de tal modo: {vocales}")
minusculas=Analizar(frase, lambda caracter: caracter>="a" and caracter<="z")
print(f"La frase unicamente con los caracteres en minusculas quedaria: {minusculas}")
simbolos=Analizar(frase, lambda caracter: caracter<"A" and caracter!=" ")
#simbolos=Analizar(frase, lambda caracter: not(caracter>="a" and caracter<="z") and not(caracter>="A" and caracter<="Z") and caracter!=" ") //OTRA FORMA DE REALIZARLO
print(f"La frase con los caracteres no alfabeticos se mostraria de modo: {simbolos}")



