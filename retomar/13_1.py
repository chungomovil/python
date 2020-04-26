"""Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. 
Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es """

oracion=input("introducir una frase: ")
espacio=0

if oracion=="":
    print("la oracion no contiene ningun caracter.")
else:
    for x in range(len(oracion)):
        if oracion[x]==" ":
            espacio+=1
            if x<len(oracion)-1:
                if oracion[x]==oracion[x+1]:
                    espacio-=1
    if espacio>0:
        print("la oracion tiene",espacio,"espacios.")
    else:
        print("la oracion no contiene espacios.")
