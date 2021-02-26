import mysql.connector

#FUNCION QUITA COMILLAS
def QuitarDecoracion(cadena):
    frase=cadena.replace('"','')
    return frase

#FUNCION EXTRAER IDPACIENTE
def ExtraerIdpaciente(cadena):
    frase=QuitarDecoracion(cadena)
    idpaciente=""
    posicion=0
    condicion=True
    while condicion!=False:
        unicode=ord(frase[posicion])
        if unicode>=48 and unicode<=57:
            idpaciente+=frase[posicion]
        if frase[posicion]==",":
            condicion=False
        else:
            posicion+=1
    return int(idpaciente)

#FUNCION EXTRAER IDCONSULTA
def ExtraerIdconsulta(cadena):
    frase=QuitarDecoracion(cadena)
    idconsulta=""
    posicion=-1
    condicion=True
    while condicion!=False:
        unicode=ord(frase[posicion])
        if unicode>=48 and unicode<=57:
            idconsulta+=frase[posicion]
        if frase[posicion]==",":
            condicion=False
        else:
            posicion-=1
    idconsulta=idconsulta[::-1] #Invertir la cadena
    return int(idconsulta)

#FUNCION EXTRAER CONTENIDO DE LA CELDA
def ExtraerCampo(cadena):
    frase=QuitarDecoracion(cadena)
    inicio="Piel:"
    claveinicio=frase.find(inicio)+len(inicio)
    extraccion=frase[claveinicio:]
    clavefin=extraccion.find("//")
    extraccion=extraccion[:clavefin]
    return extraccion



for x in range(6891):
    #OBTENER ARCHIVO
    archivo=open("e:/Documentos/programacion/github/python/retomar/proyecto-exportar/explofisicas.txt","r") # se debe de abrir el archivo en cada bucle
    contenido=archivo.readlines()[x]    #Leer linea del archivo de datos
    
    idpaciente=ExtraerIdpaciente(contenido)
    idconsulta=ExtraerIdconsulta(contenido)
    campo=ExtraerCampo(contenido)
    contenido=archivo.close()   #cerrarlo para que se pueda volver a abrir en el siguiente bucle
    
    #CONEXION A BASE DE DATOS
    conexion=mysql.connector.connect(host="192.168.1.15", user="prueba", passwd="consultoriodb", database="clinica") #Se debe reiniciar la conexion en cada bucle
    cursor1=conexion.cursor()

    #INSERTAR EN LA BASE DE DATOS
    sql="UPDATE consulta set piel=%s WHERE idconsulta=%s"
    datos=(campo, idconsulta)
    cursor1.execute(sql, datos)
    conexion.commit()
    conexion.close()

    #MOSTRAR SALIDA DE LA OPERACION
    print("--> Se modificado la consulta con ID %s" % (idconsulta))
    print("--> ITERACION NUMERO %s <--" % (x))
