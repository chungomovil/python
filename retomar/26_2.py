"""Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))"""

def CalcularCadena(lista):
    mayor=lista[0]
    for x in range(len(lista)):
        if len(mayor)<len(lista[x]):
            mayor=lista[x]
        if x==len(lista)-1: #PARA RETORNAR EL QUE TENGA MENOR VALOR DE COMPONENTE
            for y in range(len(lista)):
                if len(mayor)==len(lista[y]):
                    if mayor<lista[y]:
                        mayor=lista[y]                    
    return mayor


marcas=["pepsi","apple","toyota","ford","lambo","bugatti","xiaomi","samsung","ubisoft"]
print("La palabra con más caracteres es:", CalcularCadena(marcas))
