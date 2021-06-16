import mysql.connector as mysql
from datetime import datetime, date, timedelta
import random

from mysql.connector.errors import OperationalError

class Operaciones:

    def AbrirConexion(self, usuario, clave):
        try:
            conexion=mysql.connect(host="192.168.1.15", user=usuario, passwd=clave, database="clinica")
        except mysql.errors.ProgrammingError:
            conexion=False
        finally:
            return conexion

    def RangosFecha(self):
        hoy=date.today()
        fecha_limite=hoy+timedelta(days=-60) #Para restar entre fechas (el maximo rango es weeks, no hay months ni years)
        return fecha_limite

    def DatetimeFormatoStandard(self, fecha):
        fecha=fecha.strftime("%Y-%m-%d %H:%M:%S")
        fecha=datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
        return fecha

    def ListarRecientes(self, usuario, clave):
        conexion=self.AbrirConexion(usuario, clave)
        fecha_limite=self.RangosFecha()
        consultas="SELECT idpaciente, dni, nombres, apellidos, cat_seguro, cod_seguro, obs_seguro, aviso, telefono, movil, MAX(timestamp) FROM consulta NATURAL JOIN paciente WHERE timestamp>=%s AND (cat_seguro='Adeslas' OR cat_seguro='Dkv') GROUP BY idpaciente ORDER BY MAX(timestamp) ASC"
        cursor=conexion.cursor()
        cursor.execute(consultas, (fecha_limite, ))
        consultas_listado=cursor.fetchall()
        conexion.close()
        consultas_listado_formateado=[]
        for idpaciente, dni, nombre, apellido, seguro, delegacion, obs, aviso, fijo, movil, fecha in consultas_listado:
            #fecha=fecha.strftime("%Y-%m-%d")
            telefono=""
            if movil!="":
                telefono=movil
            else:
                if fijo!="":
                    telefono=fijo
            if seguro=="Adeslas":
                if delegacion=="Muface" or delegacion=="Isfas":
                    consultas_listado_formateado.append([idpaciente, dni, nombre, apellido, seguro, delegacion, obs, aviso, telefono, fecha])
            else:
                consultas_listado_formateado.append([idpaciente, dni, nombre, apellido, seguro, delegacion, obs, aviso, telefono, fecha])
        return consultas_listado_formateado


    def CalcularPeriodos(self, usuario, clave):
        conexion=self.AbrirConexion(usuario, clave)
        consultas_listado=self.ListarRecientes(usuario, clave)
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
            hoy=self.DatetimeFormatoStandard(hoy)
            for x in range(len(listado_formateado)-20000,len(listado_formateado)):
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
            fecha_fin=self.DatetimeFormatoStandard(fecha_fin)
            if fecha_fin<hoy:
                contador=0
            if contador>2:
                del consultas_listado[pos] #Usamos 'del'(no retorna valor eliminado) en contra de 'pop'(retorna valor eliminado), por alguna razon estaba alterando el indice de la lista
            else:
                consultas_listado[pos].append(contador)
                pos+=1
        return consultas_listado

    def FiltrarSeguro(self, adeslas, dkv, usuario, clave):
        consultas_listado=self.CalcularPeriodos(usuario, clave)
        total_adeslas=[]
        elegidos_adeslas=[]
        total_dkv=[]
        elegidos_dkv=[]
        for x in range(len(consultas_listado)):
            if consultas_listado[x][4]=="Adeslas":
                total_adeslas.append(consultas_listado[x])
            else:
                total_dkv.append(consultas_listado[x])
        if adeslas>len(total_adeslas) or dkv>len(total_dkv):
            return False
        else:
            for x in range(adeslas):
                eleccion=random.randint(0, len(total_adeslas)-1)
                elegidos_adeslas.append(total_adeslas[eleccion])
                total_adeslas.pop(eleccion)
            for x in range(dkv):
                eleccion=random.randint(0, len(total_dkv)-1)
                elegidos_dkv.append(total_dkv[eleccion])
                total_dkv.pop(eleccion)
        return (elegidos_adeslas, elegidos_dkv)

    def Insertar(self, lista_completa, usuario, clave):
        lista_adeslas, lista_dkv= lista_completa[0], lista_completa[1]
        conexion=self.AbrirConexion(usuario, clave)
        cursor=conexion.cursor()
        hoy=datetime.now()
        hoy=self.DatetimeFormatoStandard(hoy)
        for idpaciente, dni, nombre, apellido, seguro, delegacion, obs, aviso, telefono, fecha, contador in lista_adeslas:
            sql="INSERT INTO cita (idpaciente, fecha_hora, centro, obs_seguro, lopd, motivo, seguro, telefono, dni, aviso, nombres, apellidos, profesional) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            datos=(idpaciente, hoy, "Tegueste", obs, "1", "+", seguro, telefono, dni, aviso, nombre, apellido, "Dr. Rogelio")
            cursor.execute(sql, datos)
        for idpaciente, dni, nombre, apellido, seguro, delegacion, obs, aviso, telefono, fecha, contador in lista_dkv:
            sql="INSERT INTO cita (idpaciente, fecha_hora, centro, obs_seguro, lopd, motivo, seguro, telefono, dni, aviso, nombres, apellidos, profesional) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            datos=(idpaciente, hoy, "Tegueste", obs, "1", "+", seguro, telefono, dni, aviso, nombre, apellido, "Dr. Rogelio")
            cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()



            
fecha1=datetime.now()
iniciar=Operaciones()

#lista=iniciar.Filtrar_Seguro(1, 2)
#consulta=iniciar.Insertar(lista)
fecha2=datetime.now()
resultado=fecha2-fecha1
print(f"EL PROGRAMA HA TARDADO EN EJECUTARSE {resultado} SEGUNDOS")

