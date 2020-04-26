"""Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más caracteres."""

nombres=["pepe","amanda milagros","elizabeth","yuli","poreciiiita"]
x=0
contar=0
coma=0
print("Nombres con mas de 5 caracteres\n------------------------------------")

while x<len(nombres):
    if len(nombres[x])>5:
        if coma>0:              #para asignar bien las comas
            print(", ", end="")
        contar+=1
        print(nombres[x], end="")
        coma+=1
    x+=1

print("\n------------------------------------\nHay un total de", contar, "nombres con mas de 5 caracteres")
