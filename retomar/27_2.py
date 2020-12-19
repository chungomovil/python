"""Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de articulos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado."""

def CargaArticulo():
    nombres=[]
    precios=[]
    x=1
    while x<=5:
        nombre=input("Ingresar nombre articulo [%s]: " % (x))
        precio=float(input("Precio: "))
        if nombre=="" or precio<=0:
            print("Nombre o precio erroneo. Reintentar.")
        else:
            nombres.append(nombre)
            precios.append(round(precio, 2))
            x+=1
    return [nombres, precios]

def MasCaro(valor):
    posicion=0
    mayor=valor[0]
    for x in range(1, len(productos)):
        if mayor<valor[x]:
            mayor=valor[x]
            posicion=x
    return posicion

#CALCULAR VALORES INFERIORES PARA POSTERIORMENTE IMPRIMIRLOS EN EL BLOQUE PRINCIPAL
def CalcularMenores(articulo, valor):
    menornom=[]
    menorprecio=[]
    teclado=float(input("Valor inicial a filtrar: "))
    teclado=round(teclado, 2)
    for x in range(len(articulo)):
        if teclado>=valor[x]:
            menornom.append(articulo[x])
            menorprecio.append(valor[x])
    return [menornom, menorprecio, teclado] # devuelve tambien el teclado para que quede mejor mostrado


def decorar(mensaje):
    print("**************************")
    print(mensaje)
    print("**************************")


productos, precios=CargaArticulo()
masvalor=MasCaro(precios)
menorproc, menorprec, teclado=CalcularMenores(productos, precios)
decorar("Lista de productos ingresados")

for x in range(len(productos)):
    print("%s: %s€" % (productos[x], precios[x]))

decorar("Producto mas ostentoso: %s --> %s€" %(productos[masvalor], precios[masvalor]))
decorar("Productos de menor valor a %s" % (teclado))

for x in range(len(menorproc)):
    print("%s: %s€" % (menorproc[x], menorprec[x]))
