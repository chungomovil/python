import os
import json
import mysql.connector

def Archivo():
    ruta=os.path.dirname(__file__)
    ruta=ruta+"\\datos\\datos.json"
    archivo=open(ruta, "r", encoding="utf-8")
    archivo_json=json.load(archivo)
    datos=archivo_json[2]["data"]
    return datos

def ConexionDB():
    conexion=mysql.connector.connect(host="******", user="******", passwd="******", database="******")
    conexion.connect()
    return conexion

def InsertarFacturaDB(idpaciente, idconsulta, costo, timestamp):
    cursor=conexion.cursor()
    campos=(idpaciente, idconsulta, costo, timestamp)
    sql="INSERT INTO factura (idpaciente, idconsulta, total, fecha_factura) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, campos)
    return cursor._last_insert_id

def InsertarLineasFacturaDB(idfactura, idservicio, costo, cantidad, neto):
    cursor=conexion.cursor()
    campos=(idfactura, idservicio, costo, cantidad, neto)
    sql="INSERT INTO lineasfactura (idfactura, idservicio, precio, cantidad, neto) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, campos)

def ModificarLineasFacturaDB(idpaciente, idconsulta, idservicio):
    cursor1=conexion.cursor()
    cursor2=conexion.cursor()
    campos1=(idpaciente, idconsulta)
    campos2=[idservicio]
    sql1="SELECT idfactura FROM factura WHERE idpaciente=%s AND idconsulta=%s"
    sql2="UPDATE lineasfactura SET idservicio=%s WHERE idfactura=%s"
    cursor1.execute(sql1, campos1)
    campos2.append(cursor1.fetchone()[0])
    campos2=tuple(campos2)
    cursor2.execute(sql2, campos2)



datos=Archivo()
#HABILITAR SOLO PARA MODIFICAR FACTURAS
entrada_motivo=input("Valor a buscar: ").lower()
entrada_idservicio=int(input("Id del servicio: "))
conexion=ConexionDB()
for x in range(len(datos)):
    idpaciente=datos[x]['idpaciente']
    idconsulta=datos[x]['idconsulta']
    costo=datos[x]['costo']
    timestamp=datos[x]['timestamp']
    motivosconsulta=datos[x]['motivosconsulta'].lower()
    #HABILITAR SOLO PARA MODIFICAR FACTURAS
    resultado_motivo=motivosconsulta.find(entrada_motivo)
    if resultado_motivo!=-1:
        idservicio=entrada_idservicio
        ModificarLineasFacturaDB(idpaciente, idconsulta, entrada_idservicio)
    #--------------------------------------
    #HABILITAR SOLO PARA CREAR FACTURAS
    #idfactura=InsertarFacturaDB(idpaciente, idconsulta, costo, timestamp)
    #InsertarLineasFacturaDB(idfactura, 1, costo, 1, costo)
    #--------------------------------------
    print("Linea JSON:", x, "idconsulta:", idconsulta)
conexion.commit()
conexion.close()