import mysql.connector as mysql
from datetime import datetime
import credenciales

def Conexion():
    ip, usuario, password, db=credenciales.BaseDatos()
    conexion=mysql.connect(host=ip, user=usuario, passwd=password, database=db)
    return conexion

def FechaHoy():
    hoy=datetime.now()
    hoy=hoy.strftime("%m-%d")
    return hoy

def CumplenHoy():
    conexion=Conexion()
    cursor=conexion.cursor()
    hoy=(FechaHoy(), )
    consulta="SELECT nombres, apellidos, movil FROM (SELECT nombres, apellidos, movil, DATE_FORMAT(fecha_nacimiento, '%m-%d') as fecha_nac FROM paciente WHERE YEAR(fecha_nacimiento)>'1001') as nacimiento WHERE fecha_nac=%s AND movil NOT LIKE ''"
    cursor.execute(consulta, hoy)
    listado_pacientes=cursor.fetchall()
    return listado_pacientes
