"""Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos como parámetro. Definir un segundo parámetro llamado termino que por defecto almacene el valor 10. Se deben mostrar tantos términos de la tabla de multiplicar como lo indica el segundo parámetro.
Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados."""

def multiplicar(multiplicando, multiplicador=10):
    print("\nTABLA DEL %s\n" % (multiplicando))
    for x in range(1, multiplicador+1):
        resultado=round(multiplicando*x, 2)
        print("%s x %s = %s" % (multiplicando, x, resultado))

multiplicar(5)
multiplicar(multiplicador=20, multiplicando=12)
multiplicar(7, 14)
