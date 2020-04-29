print("\n-----------------------------\n| ELEGIR TIPO DE TRADUCCION |\n-----------------------------\n")
tipo=""

while tipo!="R" and tipo!="L":
    tipo=input("Escribir (R) para Revista y (L) para Libro: ").upper()
    
if tipo=="L":
    print("\n--------------\n| MODO LIBRO |\n--------------\n")
    preciopalabra=0.015
    palabraspagina=884
    tipo="libro"

else:
    print("\n----------------\n| MODO REVISTA |\n----------------\n")
    preciopalabra=0.08
    while True:
        palabraspagina=input("Palabras por pagina: ")
        try:
            palabraspagina=int(palabraspagina)
            break
        except ValueError:
            print("--> Introducir valor numerico.")
    tipo="revista"

while True:
    numeropaginas=input("Total paginas: ")
    try:
        numeropaginas=int(numeropaginas)
        break
    except ValueError:
        print("--> Introducir valor numerico.")

suma=preciopalabra*palabraspagina
presupuesto=numeropaginas*suma
print("\n---------------------\n| PRESUPUESTO TOTAL |\n---------------------\n")
print("--> Tipo:",tipo.capitalize())
print("--> Precio/palabra: ",preciopalabra,"€",sep="")
print("--> Paginas:",numeropaginas)
print("____________________________________________")
print("\n---------\n| TOTAL |\n---------")
print(round(presupuesto,2),"€",sep="")
