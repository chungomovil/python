"""
Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es """

oracion=""
espacios=0

while len(oracion)==0:
    oracion=str(input("Escribir una frase: "))
    if len(oracion)==0:
        print("no se ha escrito nada, la longitud de la oracion es:",len(oracion))
    else:
        for x in range(len(oracion)-1):
            if oracion[x]==" ":
                espacios+=1
                if oracion[x+1]==" ":
                    espacios-=1
        print("En la oracion: '",oracion.upper(),"'")
        if espacios==1:
            print("Hay",espacios,"espacio")
        else:
            print("Hay",espacios,"espacios")

