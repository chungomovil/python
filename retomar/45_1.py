"""
Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail.
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.
"""

class Agenda:

    def __init__(self):
        self.contactos={}
        self.Menu()
    
    def Menu(self):
        opcion=0
        while opcion!=5:
            print(40*"*")
            print("1.- Crear contacto.")
            print("2.- Listado de contactos.")
            print("3.- Buscar contacto.")
            print("4.- Modificar contacto.")
            print("5.- Salir.")
            print(40*"*")
            opcion=int(input("Seleccionar opcion: "))
            if opcion==1:
                self.Crear()
            if opcion==2:
                self.Listar()
            if opcion==3:
                self.Busqueda()
            if opcion==4:
                self.Modificar()
            if opcion==5:
                print("Se ha cerrado la agenda.")

    def Crear(self):
        print(40*"_")
        print("datos del contacto".upper())
        print(40*"_")
        nombre=input("Nombre: ").capitalize()
        telefono=int(input("Telefono: "))
        email=input("Email: ")
        datos=[]
        if nombre!="" and telefono!="" and email!="":
            datos.append([telefono,email])  #SE DEBE EMPAQUETAR EN UNA LISTA PARA USARLO EN EL BUCLE FOR DESEMPAQUETADO
            self.contactos[nombre]=(datos)
            print("Contacto creado correctamente.")
        else:
            print("ERROR: Se deben rellenar todos los campos.")

    def Listar(self):
        print(40*"_")
        print("lista de contactos".upper())
        print(40*"_")
        for persona in self.contactos:
            print("Nombre: %s" % (persona))
            for telefono, correo in self.contactos[persona]: #DESEMPAQUETADO DE LA LISTA
                print("Telefono: %s" % (telefono))
                print("Correo: %s" % (correo))
                print("\n")
    
    def Busqueda(self):
        print(40*"_")
        print("buscar contacto".upper())
        print(40*"_")
        busqueda=input("Nombre del contacto: ").capitalize()
        if busqueda in self.contactos:
            print("--> Datos del contacto")
            print("Nombre: %s" % (busqueda))
            for telefono, correo in self.contactos[busqueda]:
                print("Telefono: %s" % (telefono))
                print("Correo: %s" % (correo))
        else:
            print("No se ha encontrado contacto con ese nombre.")
    
    def Modificar(self):
        print(40*"_")
        print("modificar datos".upper())
        print(40*"_")
        busqueda=input("Nombre del contacto: ").capitalize()
        if busqueda in self.contactos:
            opcion=0
            while opcion!=4:
                print("1.- Modificar nombre.")
                print("2.- Modificar numero.")
                print("3.- Modificar correo.")
                print("4.- Salir.")
                opcion=int(input("Seleccionar opcion: "))
                if opcion==1:
                    nombre=input("Nuevo nombre: ").capitalize()
                    if nombre=="":
                        print("ERROR: Campo vacio.")
                    else:
                        self.contactos[nombre]=self.contactos.pop(busqueda) #ESTA ES LA FORMA MAS SENCILLA DE CAMBIAR LA CLAVE DE UN DICCIONARIO
                        busqueda=nombre #SE DEBE DE CAMBIAR LA CLAVE DE LA BUSQUEDA PARA QUE NO SIGA BUSCANDO LA ANTIGUA
                elif opcion==2:
                    telefono=int(input("Nuevo telefono: "))
                    if telefono=="":
                        print("ERROR: Campo vacio.")
                    else:
                        self.contactos[busqueda][0][0]=telefono #FORMA YA APRENDIDA DE CAMBIAR VALORES DE DICCIONARIOS
                elif opcion==3:
                    email=input("Nuevo correo: ")
                    if email=="":
                        print("ERROR: Campo vacio.")
                    else:
                        self.contactos[busqueda][0][1]=email
        else:
            print("No se ha encontrado contacto con ese nombre.")


contactos=Agenda()