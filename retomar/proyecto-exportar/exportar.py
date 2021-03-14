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
def ExtraerCampo(cadena, valor):
    frase=QuitarDecoracion(cadena)
    inicio=valor
    claveinicio=frase.find(inicio)
    #Controlar que no ingrese al no encontrar el valor
    if claveinicio<=0:
        return ""
    else:
        claveinicio=claveinicio+len(inicio)
        extraccion=frase[claveinicio:]
        clavefin=extraccion.find("//")
        extraccion=extraccion[:clavefin]
        return extraccion


columna=input("Nombre de la columna de la base de datos: ").lower()
filtro=input("Valor a filtrar en el documento: ")
for x in range(9427):
    #OBTENER ARCHIVO
    archivo=open("e:/Documentos/programacion/github/python/retomar/proyecto-exportar/explofisicas.txt","r") # se debe de abrir el archivo en cada bucle
    contenido=archivo.readlines()[x]    #Leer linea del archivo de datos
    
    idpaciente=ExtraerIdpaciente(contenido)
    idconsulta=ExtraerIdconsulta(contenido)
    campo=ExtraerCampo(contenido, filtro)
    contenido=archivo.close()   #cerrarlo para que se pueda volver a abrir en el siguiente bucle
    if campo!="":
        #CONEXION A BASE DE DATOS
        conexion=mysql.connector.connect(host="*******", user="*****", passwd="*****", database="******") #Se debe reiniciar la conexion en cada bucle
        cursor1=conexion.cursor()

        #INSERTAR EN LA BASE DE DATOS
        sql="UPDATE consulta set columna=%s WHERE idconsulta=%s"
        datos=(campo, idconsulta)
        sql=sql.replace("columna", columna)
        cursor1.execute(sql, datos)
        conexion.commit()
        conexion.close()

        #MOSTRAR SALIDA DE LA OPERACION
        print("--> Se modificado la consulta con ID %s" % (idconsulta))
    else:
        print("--> Se ha omitido. Motivo vacio.")
    print("--> ITERACION NUMERO %s <--" % (x))
