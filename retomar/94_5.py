"""
Codificar un programa que muestre en pantalla los números del 1 al 100, sustituyendo los múltiplos de 3 por el palabra "Fizz" y, a su vez, los múltiplos de 5 por "Buzz".
Para los números que, al tiempo, son múltiplos de 3 y 5, mostrar el mensaje "FizzBuzz".
"""

print("Lista de valores:")
#Algoritmo pasado a comprension de listas
print(["Fizz"*(not numero%3) + "Buzz"*(not numero%5) or numero for numero in range(1, 101)])
#EXPLICACION DEL ALGORITMO
"""El operador 'not' retorna un True o False segun la operacion, si es una opcion o la otra imprime Fizz o Buzz, si son ambas se concatenan por el operador '+' ambas palabras.
Si el operador 'not' retorna False en estas operaciones, no se imprime la cadena de caracteres y pasa a mostrarse la variable numero"""



