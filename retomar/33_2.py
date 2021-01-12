"""Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15."""

def Decorar(mensaje):
    print(len(mensaje)*"*")
    print(mensaje.upper())
    print(len(mensaje)*"*")

def CargaProductos():
    traduccion=["Primer","Segundo","Tercer","Cuarto","Quinto"]
    productos=[]
    for x in range(5):
        Decorar("%s producto" % (traduccion[x]))
        nombre=input("Nombre: ")
        condicion=False
        while condicion==False:
            precio=float(input("Precio: "))
            precio=round(precio, 2)
            if precio<=0:
                print("--> El precio debe ser superior a 0.")
            else:
                condicion=True
        productos.append((nombre, precio))
    return productos

def Imprimir(productos):
    Decorar("lista de productos")
    for producto in productos:
        print("%s --> %s €" % (producto[0], producto[1]))

def Rango(productos):
    Decorar("productos con un precio comprendido entre 10€ y 15€")
    for producto in productos:
        if producto[1]>=10 and producto[1]<=15:
            print("%s --> %s €" % (producto[0], producto[1]))

itinerario=CargaProductos()
Imprimir(itinerario)
Rango(itinerario)
