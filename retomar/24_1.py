"""Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. Llamarla desde el bloque principal del programa 3 veces con string distintos."""

def vocales(mensaje):
    casos=["a","e","i","o","u"]
    mensaje=mensaje.lower()
    contador=0
    for x in range(len(mensaje)):
        for y in range(len(casos)):
            if mensaje[x]==casos[y]:
                contador+=1
    
    print("***************************************")
    print("El texto '%s' tiene %s vocales" % (mensaje.capitalize(), contador))

vocales("HOla que tal esto es una frASE")
vocales("DEJA A VER SI reconoce todas las vocales y tallllll....   ")
vocales("42343qwrthnm")


