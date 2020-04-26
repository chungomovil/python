"""Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. 
Contar la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica que es una vocal."""

oracion=input("introducir una oracion: ")
oracion=oracion.lower()
vocales=0

for x in range(len(oracion)):
    if oracion[x]=="a" or oracion[x]=="e" or oracion[x]=="i" or oracion[x]=="o" or oracion[x]=="u":
        vocales+=1

print("En la oracion '",oracion,"' hay un total de",vocales,'vocales.')