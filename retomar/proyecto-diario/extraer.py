#IMPORTAMOS LAS LIBRERIAS NECESARIAS
import os
import shutil

#FUNCION PARA EXTRAER LOS DATOS DEL DOCUMENTO PRINCIPAL
def ExtraerDatos():
    ruta=str(os.path.dirname(__file__))+"\\almacen.txt"
    archivo=open(ruta,"r+")
    lineas=archivo.readlines()
    extraer=[]
    contador=0
    pos=0
    while contador<10:
        if pos>=len(lineas):
            break
        else:
            linea_actual=lineas[pos]
            extraer.append(lineas[pos])
            if linea_actual.find("?")>0:
                contador+=1
        pos+=1
    archivo.close()
    AdornarMensaje("Texto extraido correctamente.")
    return (lineas, extraer)

#FUNCION PARA COPIAR LOS DATOS AL DOCUMENTO TEMPORAL
def CopiarDatos(fragmento):
    ruta=os.path.dirname(__file__)+"\\extracto.txt"
    archivo=open(ruta,"w")
    archivo.writelines(fragmento)
    archivo.close()
    AdornarMensaje("Se ha renovado el documento temporal de claves.")

#FUNCION PARA QUITAR LOS DATOS DEL DOCUMENTO PRINCIPAL
def QuitarDatos(total, fragmento):
    fecha=UltimaFecha(fragmento)
    fragmento_fin=len(fragmento)
    ruta=os.path.dirname(__file__)+"\\almacen.txt"
    archivo=open(ruta,"w")
    if (len(total)>fragmento_fin): #ASI EVITAMOS QUE INTENTE BUSCAR FUERA DEL INDICE (SOLO CUANDO QUEDAN MUY POCOS DATOS EN EL DOCUMENTO PRINCIPAL)
        if total[fragmento_fin].find("?")>0:
            archivo.write(fecha)
    archivo.writelines(total[fragmento_fin:])
    archivo.close()
    AdornarMensaje("Se ha modificado el documento principal de claves.")

#FUNCION PARA RESCATAR LA ULTIMA FECHA
def UltimaFecha(fragmento):
    fecha=""
    for linea in fragmento:
        if linea.find("?")<0:
            fecha=linea
    return fecha

#FUNCION PARA EXPORTAR LOCALMENTE EL DOCUMENTO PRINCIPAL
def ExportarDocumento():
    ruta_origen=os.path.dirname(__file__)+"\\almacen.txt"
    carpeta_destino="D:\\documentos\\diario"
    ruta_destino="D:\\documentos\\diario\\almacen.txt"
    try:
        os.mkdir(carpeta_destino)
        AdornarMensaje(f"Se ha creado el directorio: {carpeta_destino}")
    except OSError:
        pass
    shutil.copy(ruta_origen, ruta_destino)
    AdornarMensaje(f"Se ha copiado el documento a la ruta: {ruta_destino}")

#FUNCION PARA EMBELLECER LOS MENSAJES
def AdornarMensaje(mensaje):
    print("\n"+(len(mensaje)+8)*"*")
    print("|   "+mensaje+"   |")
    print((len(mensaje)+8)*"*"+"\n")


verificacion=input("Confirmar el extracto de claves [S/N]: ")
verificacion=verificacion.upper()
if verificacion=="S":
    total, fragmento=ExtraerDatos()
    if len(total)>0: #DE ESTE MODO IMPEDIMOS QUE EL PROGRAMA SIGA SI EL DOCUMENTO PRINCIPAL ESTA VACIO
        CopiarDatos(fragmento)
        QuitarDatos(total, fragmento)
        ExportarDocumento()
    else:
        AdornarMensaje("AVISO: El documento 'almacen.txt' esta vacio.")
else:
    AdornarMensaje("Cancelado.")

input("Presionar calquier tecla para salir") #ASI IMPEDIMOS QUE SE CIERRE LA TERMINAL AL FINALIZAR EL PROGRAMA
