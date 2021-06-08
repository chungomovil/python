"""Crear una estructura tipo conjunto vacia.
Agregar lenguajes de programacion por teclado a dicho conjunto.
Permitir al usuario eliminar elemento del conjunto.
Informar al usuario si intenta insertar un lenguaje existente.
Informar al usuario si intenta eliminar un lenguaje no existente.
Mostrar todos los elementos del conjunto."""

#Funcion para formatear encabezado
def Decorar(mensaje):
    print(20*"*")
    espacio=18-len(mensaje)
    espacio=espacio//2
    print("*"+espacio*" "+mensaje.upper()+" "*espacio+"*")
    print(20*"*")

#Funcion para insertar nuevo elemento en el conjunto
def Insertar(lenguajes):
    Decorar("insertar")
    entrada=input("Introducir lenguaje: ")
    if entrada in lenguajes:
        print("ERROR: El lenguaje ya existe en la lista.")
    else:
        lenguajes.add(entrada)
        print("--> Insercion realizada con exito.")
    continuar=input("Continuar... [ENTER]")

#Funcion para eliminar elemento del conjunto
def Eliminar(lenguajes):
    Decorar("eliminar")
    entrada=input("Introducir lenguaje: ")
    if entrada in lenguajes:
        lenguajes.remove(entrada)
        print("--> Eliminacion realizada con exito.")
    else:
        print("ERROR: Lenguaje no encontrado.")
    continuar=input("Continuar... [ENTER]")

#Funcion para mostrar todos los elementos del conjunto
def Mostrar(lenguajes):
    Decorar("Listado")
    pos=1
    if len(lenguajes)==0:
        print("Lista vacia.")
    else:
        for lenguaje in lenguajes:
            print(f"{pos}.- {lenguaje}")
            pos+=1
    continuar=input("Continuar... [ENTER]")
#------------------------------------------------
#Creamos el conjunto
lenguajes=set()
#------------------------------------------------
#Creamos el bucle para las opciones
while True:
    print("")
    Decorar("menu")
    print("PULSAR:")
    print("1 - Insertar lenguaje.")
    print("2 - Borrar lenguaje.")
    print("3 - Mostrar todos los lenguajes.")
    print("4 - Salir.")
    entrada=int(input("Eleccion seleccionada: "))
    if entrada==1:
        Insertar(lenguajes)
    elif entrada==2:
        Eliminar(lenguajes)
    elif entrada==3:
        Mostrar(lenguajes)
    elif entrada==4:
        break
    else:
        print("ERROR: Opcion no encontrada.")
    


