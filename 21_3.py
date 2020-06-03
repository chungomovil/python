"""
Desarrollar un programa que cree una lista de 50 elementos. El primer elemento es una lista con un elemento entero, el segundo elemento es una lista de dos elementos etc.
La lista debería tener esta estructura y asignarle esos valores a medida que se crean los elementos:
[[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], etc....]
"""

lista=[]

for x in range(50):
    num=0
    lista.append([])
    while num<=x:
        num+=1
        lista[x].append(num) """Introducirlo despues de sumar el numero asi se muestra el rango bien"""
    

print(lista)
