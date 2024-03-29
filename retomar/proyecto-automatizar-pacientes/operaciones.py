#Importamos modulos necesarios
import mysql.connector as mysql
from datetime import datetime, date, timedelta
import random
#Importamos el modulo que posee las credenciales de acceso a la BD
import credenciales

#Creamos la clase
class Operaciones:

    #Metodo para establecer conexion con la BD
    def AbrirConexion(self):
        #Obtenemos las credenciales del modulo anterior y establecemos conexion
        try:
            host, usuario, clave, database=credenciales.Credenciales()
            conexion=mysql.connect(host=host, user=usuario, passwd=clave, database=database)
        #Procesamos la excepcion en caso de no encontrar el servidor
        #No especifiqué una en concreta ya que en windows(cuando se compila a .exe) la excepcion no es del modulo mysql.connector.errors sino de OSError
        except:
            conexion=False
        #Retornamos conexion
        return conexion

    #Metodo para restar a la fecha actual dos meses
    def RangosFecha(self):
        hoy=date.today()
        fecha_limite=hoy+timedelta(days=-45) #Para restar entre fechas (el maximo rango es weeks, no hay months ni years)
        #Retornamos fecha
        return fecha_limite

    #Metodo para darle un unico formato a las fechas y poder operar con ellas
    def DatetimeFormatoStandard(self, fecha):
        fecha=fecha.strftime("%Y-%m-%d")
        fecha=datetime.strptime(fecha, "%Y-%m-%d")
        #Retornamos fecha
        return fecha

    #Metodo para listar los pacientes que han asistido en los dos ultimos meses
    def ListarRecientes(self):
        #Abrimos conexion con la BD
        conexion=self.AbrirConexion()
        #Importamos la fecha limite
        fecha_limite=self.RangosFecha()
        #Creamos la consulta para extraer las asistencias
        consultas_recientes="SELECT idpaciente, dni, nombres, apellidos, cat_seguro, cod_seguro, obs_seguro, aviso, telefono, movil, MAX(timestamp) FROM consulta NATURAL JOIN paciente WHERE timestamp>=%s AND motivosconsulta!='mejora' AND (cat_seguro='Adeslas' OR cat_seguro='Dkv') GROUP BY idpaciente ORDER BY MAX(timestamp) ASC"
        cursor=conexion.cursor()
        #Ejecutamos la consulta con la fecha establecida
        cursor.execute(consultas_recientes, (fecha_limite, ))
        #Guardamos en una variable los campos de la consulta anterior
        consultas_recientes_listado=cursor.fetchall()
        #Cerramos conexion con la BD
        conexion.close()
        #Creamos una lista vacia en la que se insertaran posteriormente los datos anteriores mejor filtrados
        consultas_recientes_listado_formateado=[]
        #Recorremos los resultados
        for idpaciente, dni, nombre, apellido, seguro, delegacion, obs, aviso, fijo, movil, fecha in consultas_recientes_listado:
            telefono=""
            if movil!="":
                telefono=movil
            else:
                if fijo!="":
                    telefono=fijo
            if seguro=="Adeslas":
                if delegacion=="Muface" or delegacion=="Isfas":
                    #Insertamos campos en la lista formateada
                    consultas_recientes_listado_formateado.append([idpaciente, dni, nombre, apellido, seguro, delegacion, obs, aviso, telefono, fecha])
            else:
                #Insertamos campos en la lista formateada
                consultas_recientes_listado_formateado.append([idpaciente, dni, nombre, apellido, seguro, delegacion, obs, aviso, telefono, fecha])
        #Retornamos la lista anterior, pero incluyendo solamente los que no se encuentran en la tabla cita
        listado_recientes_final=self.FiltrarNoCitados(consultas_recientes_listado_formateado)
        #Retornamos la lista anterior
        return listado_recientes_final

    #Metodo para eliminar los que se encuentran ya citados
    def FiltrarNoCitados(self, listado_recientes):
        #Abrimos la conexion con la BD
        conexion=self.AbrirConexion()
        cursor=conexion.cursor()
        #Buscamos los pacientes en la tabla cita
        cursor.execute("SELECT idpaciente FROM cita")
        #Guardamos en una variable los campos de la consulta anterior
        listado_citas=cursor.fetchall()
        #Cerramos conexion con la BD
        conexion.close()
        pos=0
        #Recorremos lista de el total de recientes
        while pos<len(listado_recientes):
            similitud=""
            #Recorremos los que estan en cita
            for x in range(len(listado_citas)):
                if listado_citas[x][0]==listado_recientes[pos][0]:
                    similitud=True
            #Si hay coincidencia elimina al paciente de la lista de recientes
            if similitud==True:
                del listado_recientes[pos] #Usamos 'del'(no retorna valor eliminado) en contra de 'pop'(retorna valor eliminado), por alguna razon estaba alterando el indice de la lista
            else:
                pos+=1
        #Retornamos lista final de recientes
        return listado_recientes

    #Metodo para calcular los periodos individuales de asistencia
    def CalcularPeriodos(self, listado_recientes):
        #Abrimos conexion
        conexion=self.AbrirConexion()
        #Guardamos en una variable la lista reciente final
        consultas_recientes_listado=listado_recientes
        cursor=conexion.cursor()
        #Buscamos todas las consultas de pacientes Adeslas y DKV
        cursor.execute("SELECT idpaciente, timestamp FROM consulta NATURAL JOIN paciente WHERE cat_seguro='Adeslas' OR cat_seguro='Dkv' ORDER BY timestamp ASC")
        #Guardamos en una variable los campos de la consulta anterior
        consultas_total_listado=cursor.fetchall()
        #Cerramos la conexion con la BD
        conexion.close()
        pos=0
        #Recorremos el listado de pacientes recientes
        while pos<len(consultas_recientes_listado):
            contador=0
            fecha_inicio=""
            fecha_fin=""
            hoy=datetime.now()
            #Formateamos la fecha actual para operar correctamente con ella
            hoy=self.DatetimeFormatoStandard(hoy)
            #Guardamos la ultima consulta del paciente actual
            ultima=consultas_recientes_listado[pos][9]
            #Formateamos esta fecha para operar
            ultima=self.DatetimeFormatoStandard(ultima)
            #Recorremos los ultimos 30000 registros de consultas de todos los pacientes (3 años aproximadamente)
            #Esta operacion tarda 4 segundos aproximadamente, la base de datos completa tarda el doble
            for x in range(len(consultas_total_listado)-30000, len(consultas_total_listado)):
                #Filtramos la consulta del mismo paciente
                if consultas_recientes_listado[pos][0]==consultas_total_listado[x][0]:
                    #Calculamos los rangos de asistencia
                    if contador==0:
                        fecha_inicio=consultas_total_listado[x][1]
                        fecha_fin=fecha_inicio+timedelta(days=30)
                    else:
                        if fecha_fin<consultas_total_listado[x][1]:
                            fecha_inicio=consultas_total_listado[x][1]
                            fecha_fin=fecha_inicio+timedelta(days=30)
                            contador=0
                    contador+=1
            #Una vez terminados los calculos, formateamos la fecha para operar
            #Recordar que llegados a este punto el contador resultante sera el de la ultima coincidencia que se encontro en el bucle anterior
            #Por ello hay que ejecutar los ultimos filtros para que tenga en cuenta la fecha actual
            fecha_fin=self.DatetimeFormatoStandard(fecha_fin)
            if fecha_fin<hoy:
                contador=0
            #Filtramos los que a dia de hoy han venido mas de 2 veces o han asistido en la fecha actual 
            if contador>2 or hoy==ultima:
                #Eliminamos del listado de recientes final los que no cumplan el filtro
                del consultas_recientes_listado[pos] #Usamos 'del'(no retorna valor eliminado) en contra de 'pop'(retorna valor eliminado), por alguna razon estaba alterando el indice de la lista
            else:
                #Incluimos un campo en la lista del paciente con sus asistencias a dia de hoy (se usara luego)
                consultas_recientes_listado[pos].append(contador)
                pos+=1
        #Retornamos el listado de recientes final y que tengan menos de 3 asistencias hasta la fecha actual
        return consultas_recientes_listado

    #Metodo para filtrar pacientes por seguro
    def FiltrarSeguro(self, listado_recientes):
        #Importamos la lista retornada por la funcion anterior
        consultas_recientes_listado=listado_recientes
        #Creamos dos listas para ir separando los pacientes por seguro
        total_adeslas=[]
        total_dkv=[]
        #Recorremos la lista
        for x in range(len(consultas_recientes_listado)):
            #Agregamos a una lista los de adeslas
            if consultas_recientes_listado[x][4]=="Adeslas":
                total_adeslas.append(consultas_recientes_listado[x])
            #Agregamos a una lista los de dkv
            else:
                total_dkv.append(consultas_recientes_listado[x])
        #Retornamos ambas listas
        return (total_adeslas, total_dkv)
    
    #Metodo para elegir aleatoriamente la cantidad de pacientes solicitada de cada seguro
    def ElegirPacientes(self, lista_adeslas, lista_dkv, cantidad_adeslas, cantidad_dkv):
        #Creamos dos listas para ir separando los pacientes elegidos por seguro
        elegidos_adeslas=[]
        elegidos_dkv=[]
        #Recorremos la lista de pacientes de adeslas
        for x in range(cantidad_adeslas):
            #Elegimos un numero al azar (representando la posición de la lista)
            eleccion=random.randint(0, len(lista_adeslas)-1)
            #Agregamos a la lista dicha elección
            elegidos_adeslas.append(lista_adeslas[eleccion])
            #Eliminamos de la lista principal esta eleccion para que no se repita
            lista_adeslas.pop(eleccion)
        #Hacemos lo mismo con los pacientes de dkv
        for x in range(cantidad_dkv):
            eleccion=random.randint(0, len(lista_dkv)-1)
            elegidos_dkv.append(lista_dkv[eleccion])
            lista_dkv.pop(eleccion)
        #Retornamos ambas listas con los elegidos aleatoriamente
        return (elegidos_adeslas, elegidos_dkv)

    #Metodo para insertar en la tabla cita los pacientes
    def Insertar(self, elegidos_adeslas, elegidos_dkv, fecha):
        #Conectamos con la BD
        conexion=self.AbrirConexion()
        cursor=conexion.cursor()
        #Recorremos las listas para insertar los campos en la BD
        for idpaciente, dni, nombre, apellido, seguro, delegacion, obs, aviso, telefono, ultimaconsulta, contador in elegidos_adeslas:
            #Creamos la consulta de insercion de datos
            sql="INSERT INTO cita (idpaciente, fecha_hora, centro, obs_seguro, lopd, motivo, seguro, telefono, dni, aviso, nombres, apellidos, profesional) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            #Establecemos los valores que se insertaran (el campo 'fecha' lo recibimos desde la interfaz visual ya formateado)
            datos=(idpaciente, fecha, "Tegueste", obs, "1", "+", seguro, telefono, dni, aviso, nombre, apellido, "Dr. Rogelio")
            #Ejecutamos la consulta
            cursor.execute(sql, datos)
        for idpaciente, dni, nombre, apellido, seguro, delegacion, obs, aviso, telefono, ultimaconsulta, contador in elegidos_dkv:
            sql="INSERT INTO cita (idpaciente, fecha_hora, centro, obs_seguro, lopd, motivo, seguro, telefono, dni, aviso, nombres, apellidos, profesional) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            datos=(idpaciente, fecha, "Tegueste", obs, "1", "+", seguro, telefono, dni, aviso, nombre, apellido, "Dr. Rogelio")
            cursor.execute(sql, datos)
        #Fijamos campos en la BD
        conexion.commit()
        #Cerramos conexion con la BD
        conexion.close()
