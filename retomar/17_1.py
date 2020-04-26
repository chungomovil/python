"""Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado."""

productos=[]
precios=[]
total=0

for x in range(5):
    producto=input("Nombre del producto: ")
    precio=float(input("Precio: "))
    productos.append(producto)
    precios.append(precio)

print("\n--------------------\nLOS PRODUCTOS CON PRECIO SUPERIOR A",productos[0].upper(),"SON\n--------------------\n")
for x in range(len(productos)):
    if precios[x]>precios[0]:
        print(productos[x],": ",sep="", end="")
        print(precios[x])
        total+=1

if total==0:
    print(productos[0].capitalize(),"es el articulo mas caro.")