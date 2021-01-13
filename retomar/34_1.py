"""
Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento."""

def CargaPersonas():
    datospersonales={}
    for x in range(4):
        print(10*"*")
        print("PERSONA NUMERO [%s]" % (x+1))
        print(10*"*")
        condicion=False
        while condicion==False:
            dni=input("Introducir DNI: ").upper()
            nombre=input("Introducir nombre: ").capitalize()
            if dni=="" or nombre=="":
                print("--> Se deben rellenar ambos campos.")
            else:
                datospersonales[dni]=nombre
                print("--> Usuario creado.")
                condicion=True
    return datospersonales

def Imprimir(personas):
    print(10*"*")
    print("LISTADO DE PERSONAS")
    print(10*"*")
    for persona in personas:
        print("%s ---> %s" % (personas[persona], persona))
    
def Consultar(personas):
    valor=""
    while valor!="Q":
        valor=input("Buscar persona por DNI ('Q' Omitir): ").upper()
        if valor!="Q":
            if valor in personas:
                print("Nombre: %s" % (personas[valor]))
            else:
                print("--> No existe dicho DNI.")
            
datospersonales=CargaPersonas()
Imprimir(datospersonales)
Consultar(datospersonales)
