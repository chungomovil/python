"""Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. 
Contar la cantidad de vocales. 
Crear un segundo string con toda la oración en minúsculas 
para que sea más fácil disponer la condición que verifica que es una vocal."""

oracion=input("introducir frase: ")
oracion=oracion.lower()
vocal=0
for x in range(len(oracion)):
    if oracion[x]=="a" or oracion[x]=="e" or oracion[x]=="i" or oracion[x]=="o" or oracion[x]=="u":
        vocal+=1

if vocal==0:
    print("la oracion no contiene vocales")
else:
    if vocal==1:
        print("la oracion contiene una vocal")
    else:
        print("la oracion contiene",vocal,"vocales")