"""
Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el nombre de persona menor en orden alfabético.
"""

personas=[]

for x in range(5):
    nombre=input("Introducir nombre: ")
    personas.append(nombre)

menor=personas[0]
posicion=1

for x in range(len(personas)):
    if personas[x]<menor:
        menor=personas[x]
        posicion=x+1

print("\n---------------------\nLISTA INTRODUCIDA")
print(personas)
print("---------------------\nNOMBRE MENOR ALFABETICAMENTE")
print("'",menor.upper(), "' en la posicion ", posicion, " de la lista", sep="")