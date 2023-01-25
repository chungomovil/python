#Importamos los modulos necesarios
import mysql.connector as mysql
from datetime import datetime
import credenciales

#Funcion para abrir la conexion con la base de datos
def Conexion():
    #Almacenamos las credenciales del modulo encargado
    ip, usuario, password, db=credenciales.BaseDatos()
    #contectamos con la BD
    conexion=mysql.connect(host=ip, user=usuario, passwd=password, database=db)
    #Retornamos la conexion
    return conexion

#Funcion para obtener la fecha actual
def FechaHoy():
    #Guardamos la fecha actual
    hoy=datetime.now()
    #La formateamos para que muestre solo mes-dia
    hoy=hoy.strftime("%m-%d")
    #Retornamos la fecha
    return hoy

#Funcion para obtener los que cumplen en la fecha actual
def CumplenHoy():
    #Conectamos con la BD
    conexion=Conexion()
    #Creamos el cursor
    cursor=conexion.cursor()
    #Obtenemos la fecha formateada y la convertimos en tupla para la consulta sql
    hoy=(FechaHoy(), )
    #Consulta sql (con subconsulta) para obtener los pacientes que cumples en la fecha actual
    consulta="SELECT nombres, apellidos, movil FROM (SELECT nombres, apellidos, movil, DATE_FORMAT(fecha_nacimiento, '%m-%d') as fecha_nac FROM paciente WHERE YEAR(fecha_nacimiento)>'1001') as nacimiento WHERE fecha_nac=%s AND movil NOT LIKE ''"
    #Ejecutamos la consulta
    cursor.execute(consulta, hoy)
    #Extraemos todas sus filas
    listado_pacientes=cursor.fetchall()
    #Retornamos los pacientes
    return listado_pacientes
