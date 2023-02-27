import mysql.connector

def ExtraerCampos(texto):
    cortar=texto.find(";")
    num_tarjeta=texto[:cortar-1]
    nombre_tarjeta=texto[cortar+1:len(texto)-1]
    return (num_tarjeta, nombre_tarjeta)


for x in range(4099):
    archivo=open("d:/Documentos/programacion/github/python/retomar/proyecto-exportar/tarjetas/tarjetas.txt","r")
    contenido=archivo.readlines()[x]
    datos=ExtraerCampos(contenido)
    archivo.close()
    conexion=mysql.connector.connect(host="*******", user="********", passwd="********", database="**********")
    cursor1=conexion.cursor()
    sql="UPDATE paciente SET idbusqueda=%s WHERE obs_seguro=%s AND idbusqueda=''"
    cursor1.execute(sql, datos)
    conexion.commit()
    conexion.close()
    print("linea: %s" % (x+1))
