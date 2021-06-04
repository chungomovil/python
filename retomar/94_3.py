"""Generar una lista con todos los valores múltiplos de 8 comprendidos entre 1 y 500."""

#Creamos la lista con comprension y le pasamos el algoritmo
numeros=[numero for numero in range(1, 501) if numero%8==0]

#Imprimimos la lista
print(f"Multiplos de 8:\n{numeros}")


