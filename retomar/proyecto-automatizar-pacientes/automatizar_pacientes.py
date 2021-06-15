import mysql.connector as mysql
from datetime import datetime, date, timedelta
import random

def AbrirConexion():
    conexion=mysql.connect(host="192.168.1.15", user="", passwd="", database="clinica")
    return conexion

def RangosFecha():
    hoy=date.today()
    fecha_limite=hoy+timedelta(days=-60) #Para restar entre fechas (el maximo rango es weeks, no hay months ni years)
    return fecha_limite

def DatetimeFormatoStandard(fecha):
    fecha=fecha.strftime("%Y-%m-%d %H:%M:%S")
    fecha=datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
    return fecha

def ListarRecientes():
    conexion=AbrirConexion()
    fecha_limite=RangosFecha()
    consultas="SELECT idpaciente, concat(nombres,' ', apellidos) as nombre, cat_seguro, cod_seguro, telefono, movil, MAX(timestamp) FROM consulta NATURAL JOIN paciente WHERE timestamp>=%s AND (cat_seguro='Adeslas' OR cat_seguro='Dkv') GROUP BY idpaciente ORDER BY MAX(timestamp) ASC"
    cursor=conexion.cursor()
    cursor.execute(consultas, (fecha_limite, ))
    consultas_listado=cursor.fetchall()
    conexion.close()
    consultas_listado_formateado=[]
    for idpaciente, nombre, seguro, delegacion, fijo, movil, fecha in consultas_listado:
        #fecha=fecha.strftime("%Y-%m-%d")
        telefono=""
        if movil!="":
            telefono=movil
        else:
            if fijo!="":
                telefono=fijo
        if seguro=="Adeslas":
            if delegacion=="Muface" or delegacion=="Isfas":
                consultas_listado_formateado.append([idpaciente, nombre, seguro, delegacion, telefono, fecha])
        else:
            consultas_listado_formateado.append([idpaciente, nombre, seguro, delegacion, telefono, fecha])
    return consultas_listado_formateado


def CalcularPeriodos():
    conexion=AbrirConexion()
    consultas_listado=ListarRecientes()
    cursor=conexion.cursor()
    cursor.execute("SELECT idpaciente, timestamp FROM consulta NATURAL JOIN paciente WHERE cat_seguro='Adeslas' OR cat_seguro='Dkv' ORDER BY timestamp ASC")
    listado=cursor.fetchall()
    conexion.close()
    listado_formateado=[]
    for idpaciente, fecha in listado:
        #fecha=fecha.strftime("%Y-%m-%d")
        listado_formateado.append([idpaciente, fecha])
    pos=0
    while pos<len(consultas_listado):
        contador=0
        fecha_inicio=""
        fecha_fin=""
        hoy=datetime.now()
        hoy=DatetimeFormatoStandard(hoy)
        for x in range(len(listado_formateado)):
            if consultas_listado[pos][0]==listado_formateado[x][0]:
                if contador==0:
                    fecha_inicio=listado_formateado[x][1]
                    fecha_fin=fecha_inicio+timedelta(days=30)
                else:
                    if fecha_fin<listado_formateado[x][1]:
                        fecha_inicio=listado_formateado[x][1]
                        fecha_fin=fecha_inicio+timedelta(days=30)
                        contador=0
                contador+=1
        fecha_fin=DatetimeFormatoStandard(fecha_fin)
        if fecha_fin<hoy:
            contador=0
        if contador>2:
            consultas_listado.pop(pos)
        else:
            consultas_listado[pos].append([contador])
        pos+=1
    return consultas_listado

def Filtrar_Seguro(adeslas, dkv):
    consultas_listado=CalcularPeriodos()
    total_adeslas=[]
    elegidos_adeslas=[]
    total_dkv=[]
    elegidos_dkv=[]
    for x in range(len(consultas_listado)):
        if consultas_listado[x][2]=="Adeslas":
            total_adeslas.append(consultas_listado[x])
        else:
            total_dkv.append(consultas_listado[x])
    if adeslas>len(total_adeslas) or dkv>len(total_dkv):
        return False
    else:
        for x in range(adeslas):
            eleccion=random.randint(0, len(total_adeslas))
            elegidos_adeslas.append(total_adeslas[eleccion])
            total_adeslas.pop(eleccion)
        for x in range(dkv):
            eleccion=random.randint(0, len(total_dkv))
            elegidos_dkv.append(total_dkv[eleccion])
            total_dkv.pop(eleccion)
    return elegidos_adeslas

            
fecha1=datetime.now()
iniciar=Filtrar_Seguro(5,0)
print(iniciar)
fecha2=datetime.now()
resultado=fecha2-fecha1
print(f"EL PROGRAMA HA TARDADO EN EJECUTARSE {resultado} SEGUNDOS")

