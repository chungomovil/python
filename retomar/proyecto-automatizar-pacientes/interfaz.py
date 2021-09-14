#Importamos modulos necesarios
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import sys
import os
from datetime import date, datetime, timedelta
#Importamos el modulo con la sintaxis de la BD
import operaciones

#Buscar la ruta del archivo actual
try:
    #Si se esta ejecutando desde desde el interprete python
    ruta=os.path.dirname(__file__)
#Generara una excepcion si el archivo esta en ".exe"
except NameError:
    #Si esta en formato ".exe"
    ruta=os.path.dirname(sys.argv[0])
#Nos situamos en la carpeta imagenes
finally:
    tema_ruta=str(ruta)+"\\tema\\arc.tcl"

#Creamos la clase
class Aplicacion:

    #Creamos el metodo constructor
    def __init__(self):
        #Importamos la clase del modulo con las operacion de la DB
        self.conectar=operaciones.Operaciones()
        #Creamos dos elementos tipo lista que se usaran mas adelante
        self.listado_adeslas=[]
        self.listado_dkv=[]
        #Establecemos el tema que usará la ventana
        self.ventana=tk.Tk()
        self.ventana.title("AUTOMATIZAR CITAS")
        #Fijamos este color en específico porque es el color de fondo de los widgets de este tema (para evitar el cambio de tono en elementos que no se expandan)
        self.ventana.configure(background="#f5f6f8")
        tema=ttk.Style(self.ventana)
        self.ventana.call("source", tema_ruta)
        tema.theme_use("arc")
        #Creamos el menu
        menubar=tk.Menu(self.ventana)
        self.ventana.configure(menu=menubar)
        opciones=tk.Menu(menubar, tearoff=0)
        opciones.add_command(label="SALIR", command=self.Salir)
        menubar.add_cascade(label="Opciones", menu=opciones)
        #Seccion de los estilos de algunos widgets
        self.estilo_etiquetas_global=ttk.Style(self.ventana)
        self.estilo_etiquetas_global.configure("TLabel", font=("Arial", 12))
        self.estilo_etiqueta_seguros=ttk.Style(self.ventana)
        self.estilo_etiqueta_seguros.configure("Seguro.TLabel", font=("Arial", 14, "bold"))
        self.estilo_etiqueta_fecha=ttk.Style(self.ventana)
        self.estilo_etiqueta_fecha.configure("Fecha.TLabel", font=("Arial", 12, "bold"), foreground="#004AAD")
        self.estilo_spinbox_global=ttk.Style(self.ventana)
        self.estilo_spinbox_global.configure("TSpinbox", arrowsize=15)
        #Creamos los distintos Frames
        self.frame1=tk.Frame(self.ventana)
        self.frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        #grid_columconfigure se emplea para que las celdas tengan el mismo ancho
        self.frame1.grid_columnconfigure(0, weight=1)
        self.frame1.grid_rowconfigure(0, weight=1)
        self.frame2=ttk.Frame(self.ventana)
        self.frame2.pack(side=tk.TOP, expand=True)
        self.frame2.grid_columnconfigure(0, weight=1, uniform="grupo") #El atributo 'uniform' es para asignar el conjunto al que va dirigida esta configuracion
        self.frame2.grid_columnconfigure(1, weight=1, uniform="grupo")
        self.frame3=ttk.Frame(self.ventana)
        self.frame3.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.frame3.grid_columnconfigure(0, weight=1, uniform="grupo")
        self.frame3.grid_columnconfigure(1, weight=1, uniform="grupo")
        self.frame4=ttk.Frame(self.ventana)
        self.frame4.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        #Llamamos a los metodos necesarios
        self.Header()
        self.FormularioSeguros()
        self.FormularioFecha()
        #El metodo 'RecibirFecha' lo ejecutamos desde el metodo constructor para que al iniciar el programa ya se copie la fecha actual en los Spinbox
        self.RecibirFecha()
        #Despues que la ventana termine de iniciar su mainloop procedera a ejecutar esta funcion ¡OJO! No poner '()' en la funcion ya que si no se ejecutará inmediatamente
        self.ventana.after(1000, self.BusquedaDB)
        #Algoritmo para centrar la ventana
        ventana_ancho=670
        ventana_alto=750
        pantalla_ancho=self.ventana.winfo_screenwidth() #Obtenemos el ancho en píxeles del monitor
        pantalla_alto=self.ventana.winfo_screenheight() #Obtenemos el alto en píxeles del monitor
        pos_x=int((pantalla_ancho/2)-(ventana_ancho/2))
        pos_y=int((pantalla_alto/2)-(ventana_alto/2))
        self.ventana.geometry(f"{ventana_ancho}x{ventana_alto}+{pos_x}+{pos_y}") #Centramos la ventana
        self.ventana.resizable(False, False)
        self.ventana.mainloop()

    #Metodo para crear el formulario de entrada de datos
    def Header(self):
        self.Encabezado=ttk.Label(self.frame1, text="Automatizar Citas", anchor="center", foreground="#E74C3C", font=("Comic Sans MS", 20, "italic")) #El atributo anchor viene siendo como un align
        self.Encabezado.grid(column=0, row=0, sticky="nswe", ipady=20)
        self.titulo_disponibles=ttk.Label(self.frame2, text="Disponibles", font=("Arial", 14, "bold"))
        self.titulo_disponibles.grid(column=0, row=0, columnspan=2, pady=(0, 20))
        self.titulo_disponibles_adeslas=ttk.Label(self.frame2, text="Adeslas", anchor="center", borderwidth=1, relief="groove")
        self.titulo_disponibles_adeslas.grid(column=0, row=1, ipadx=5, sticky="we")
        self.disponibles_adeslas=ttk.Label(self.frame2, text="---", anchor="center", foreground="#5DADE2", font=("Arial", 18, "bold"), borderwidth=1, relief="groove")
        self.disponibles_adeslas.grid(column=0, row=2, sticky="we")
        self.titulo_disponibles_dkv=ttk.Label(self.frame2, text="DKV", anchor="center", borderwidth=1, relief="groove")
        self.titulo_disponibles_dkv.grid(column=1, row=1, ipadx=5, sticky="we")
        self.disponibles_dkv=ttk.Label(self.frame2, text="---", anchor="center", foreground="#2ECC71", font=("Arial", 18, "bold"), borderwidth=1, relief="groove")
        self.disponibles_dkv.grid(column=1, row=2, sticky="we")
        self.titulo5=ttk.Label(self.frame4, text="Pacientes citados", anchor="center", font=("Arial", 14, "bold"))
        self.titulo5.grid(column=0, row=5, ipady=20, sticky="nswe")
        self.scrolledtext=st.ScrolledText(self.frame4, width=80, height=20)
        self.scrolledtext.grid(column=0, row=6)
        #Agregamos el encabezado al scrolledtext (Recordar que debemos de partir desde el final para una mejor organizacion)
        self.encabezado=f"{'NUMERO':<10}{'NOMBRE':<50}{'SEGURO':<10}{'CONSULTAS':<10}"
        self.scrolledtext.insert(tk.END, self.encabezado)

    #Metodo para crear el formulario de seguros
    def FormularioSeguros(self):
        self.frame_seguros=ttk.Frame(self.frame3)
        self.frame_seguros.grid(column=1, row=0, padx=50, sticky="nswe")
        self.frame_seguros.columnconfigure(0, weight=1)
        self.frame_seguros.columnconfigure(1, weight=1)
        self.titulo3=ttk.Label(self.frame_seguros, text="Adeslas", style="Seguro.TLabel") #De esta forma aplicamos un estilo personalizado a un widget
        self.titulo3.grid(column=0, row=2, pady=10)
        self.entrada_adeslas=ttk.Spinbox(self.frame_seguros, from_=0, to=10, width=10, state="readonly", font=("Arial", 12))
        self.entrada_adeslas.set(0)
        self.entrada_adeslas.grid(column=0, row=3, pady=10)
        self.titulo4=ttk.Label(self.frame_seguros, text="DKV", style="Seguro.TLabel")
        self.titulo4.grid(column=1, row=2, pady=10)
        self.entrada_dkv=ttk.Spinbox(self.frame_seguros, from_=0, to=5, width=10, state="readonly", font=("Arial", 12))
        self.entrada_dkv.set(0)
        self.entrada_dkv.grid(column=1, row=3, pady=10)
        self.confirmar2=ttk.Button(self.frame_seguros, width=20, text="CITAR", command=self.InsertarDB)
        self.confirmar2.grid(column=0, row=4, columnspan=2, pady=20)

    #Metodo que crea el formulario para entrada de fechas
    def FormularioFecha(self):
        self.frame_fecha=ttk.Frame(self.frame3)
        self.frame_fecha.grid(column=0, row=0, padx=50, sticky="nswe")
        #Indicamos al frame padre que las columnas usarán todo su espacio disponible
        self.frame_fecha.columnconfigure(0, weight=1)
        self.frame_fecha.columnconfigure(1, weight=1)
        #Indicamos al frame padre que las filas usarán todo su espacio disponible
        for x in range(4):
            self.frame_fecha.rowconfigure(x , weight=1)
        self.titulo_fecha=ttk.Label(self.frame_fecha, text="Fecha Cita", anchor="n", font=("Arial", 14, "bold"))
        self.titulo_fecha.grid(column=0, row=0, columnspan=2, pady=10, sticky="nswe")
        self.titulo_dia=ttk.Label(self.frame_fecha, text="Día", style="Fecha.TLabel")
        self.titulo_dia.grid(column=0, row=1, sticky="nswe")
        self.dia=ttk.Spinbox(self.frame_fecha, from_=1, to=31, width=5, state="readonly", font=("Arial", 12))
        self.dia.grid(column=1, row=1, sticky="nswe")
        self.titulo_mes=ttk.Label(self.frame_fecha, text="Mes", style="Fecha.TLabel")
        self.titulo_mes.grid(column=0, row=2, sticky="nswe")
        self.mes=ttk.Spinbox(self.frame_fecha, from_=1, to=12, width=5, state="readonly", font=("Arial", 12))
        self.mes.grid(column=1, row=2, sticky="nswe")
        self.titulo_anio=ttk.Label(self.frame_fecha, text="Año", style="Fecha.TLabel")
        self.titulo_anio.grid(column=0, row=3, sticky="nswe")
        self.anio=ttk.Spinbox(self.frame_fecha, from_=2021, to=2030, width=5, state="readonly", font=("Arial", 12))
        self.anio.grid(column=1, row=3, sticky="nswe")
        self.titulo_hora=ttk.Label(self.frame_fecha, text="Hora", style="Fecha.TLabel")
        self.titulo_hora.grid(column=0, row=4, sticky="nswe")
        self.hora=ttk.Spinbox(self.frame_fecha, from_=00, to=23, width=5, state="readonly", font=("Arial", 12))
        self.hora.grid(column=1, row=4, sticky="nswe")
    
    #Metodo para crear la ventana de carga
    def AbrirVentanaCarga(self):
        #Llamamos a la funcion que cambia los parametros de la ventana principal
        self.EstadoVentana(1)
        #La abrimos en modo "Toplevel" para que sea independiente de la principal ¡RECORDATORIO! Esta ventana no necesita mainloop() para ejecutarse
        self.ventanacarga=tk.Toplevel()
        self.ventanacarga.title("Cargando datos...")
        self.ventanacarga.attributes("-topmost", "true") #De este modo indicamos que la ventana se mostrará encima de las demás
        self.ventanacarga.configure(background="#f5f6f8")
        self.titulocarga=ttk.Label(self.ventanacarga, text="", anchor="center", font=("Arial", 13, "bold"))
        self.titulocarga.grid(column=0, row=0, sticky="we", padx=10, pady=(25, 5))
        #Creamos una barra de progreso
        self.barracarga=ttk.Progressbar(self.ventanacarga, length=300, mode="determinate")
        self.barracarga.grid(column=0, row=1, sticky="we", padx=10)
        #Algoritmo para centrar el Toplevel a su ventana padre
        ventana_ancho=320
        ventana_alto=100
        ubicacion_padre_ancho=self.ventana.winfo_x() #Obtenemos la posición actual en píxeles de la ventana padre (ancho)
        ubicacion_padre_alto=self.ventana.winfo_y() #Obtenemos la posición actual en píxeles de la ventana padre (alto)
        pos_x=int(ubicacion_padre_ancho+((670/2)-(ventana_ancho/2)))
        pos_y=int(ubicacion_padre_alto+((750/2)-(ventana_alto/2)))
        self.ventanacarga.geometry(f"{ventana_ancho}x{ventana_alto}+{pos_x}+{pos_y}") #La centramos en la ubicación actual de la ventana padre
        self.ventanacarga.resizable(False, False)       
    
    #Metodo para cerrar la ventana de carga
    def CerrarVentanaCarga(self):
        #Destruimos la ventana
        self.ventanacarga.destroy()
        #Devolvemos la ventana principal a su estado inicial
        self.EstadoVentana(0)

    #Metodo para obtener fecha actual e insertarla en el formulario
    def RecibirFecha(self):
        actual=datetime.now()
        #Desglosamos la fecha actual
        dia=actual.strftime("%d")
        mes=actual.strftime("%m")
        anio=actual.strftime("%Y")
        hora=actual.strftime("%H")
        #Insertamos cada campo de la fecha en su Spinbox
        self.dia.set(dia)
        self.mes.set(mes)
        self.anio.set(anio)
        self.hora.set(hora)

    #Metodo para devolver la fecha introducida por el usuario
    def EnviarFecha(self):
        #Obtenemos los datos de los diferentes Spinbox
        dia=self.dia.get()
        mes=self.mes.get()
        anio=self.anio.get()
        hora=self.hora.get()
        #Transformamos en una unica cadena (string) estos datos dandole el formato de una fecha
        fecha_nueva=anio+"-"+mes+"-"+dia+" "+hora+":"+"00:00"
        #Algoritmo que testearemos
        try:
            #Transformamos la string a formato datetime
            fecha_nueva=datetime.strptime(fecha_nueva, "%Y-%m-%d %H:%M:%S")
        #Si devuelve error, es decir, si la fecha no existe (31-02-2021) devuelve ValueError
        except ValueError:
            fecha_nueva=False
        #Retornamos la fecha resultante
        finally:
            return fecha_nueva

    #Metodo para mostrar mensajes en la ventana de carga según la operación que se esté realizando
    def mensaje(self, operacion):
        if operacion==1:
            texto="Conectando a la base de datos..."
            #Rellenamos en '%' la barra de progreso
            self.barracarga["value"]=30
        elif operacion==2:
            texto="Obteniendo pacientes recientes..."
            self.barracarga["value"]=50
        elif operacion==3:
            texto="Calculando asistencias en el mes..."
            self.barracarga["value"]=80
        elif operacion==4:
            texto="Finalizando..."
            self.barracarga["value"]=100
        self.titulocarga.configure(text=texto)
        #Este metodo de la ventana permite refrescar la interfaz visual y no esperar a que termine el hilo de ejecución de otra función
        self.ventana.update()

    #Metodo para buscar datos en la BD
    def BusquedaDB(self):
        #Abrimos la ventana de carga
        self.AbrirVentanaCarga()
        #Mostramos mensaje de estado del programa
        self.mensaje(1)
        #Este metodo de la ventana hace que la interfaz visual se pause un número de milisegundos especificados (básicamente para leer el mensaje)
        self.ventana.after(1000)
        #Establecemos conexión a la base de datos y retornamos resultado
        conexion=self.conectar.AbrirConexion()
        #Si se establece la conexion
        if conexion!=False:
            self.mensaje(2)
            self.ventana.after(1000)
            #Retornamos la lista final de pacientes recientes
            recientes=self.conectar.ListarRecientes()
            self.mensaje(3)
            #Retornamos la lista final de recientes que tengan menos de 3 asistencias y no hayan acudido hoy
            #No hace falta pausar la interfaz ya que esta operación tarda un par de segundos
            recientes_con_rangos=self.conectar.CalcularPeriodos(recientes)
            self.mensaje(4)
            self.ventana.after(500)
            #Obtenemos la lista de los pacientes filtrados por seguro y los almacenamos en las variables globales que hablamos antes
            self.listado_adeslas, self.listado_dkv=self.conectar.FiltrarSeguro(recientes_con_rangos)
            #Mostramos el total de disponibles en la interfaz
            self.disponibles_adeslas.configure(text=len(self.listado_adeslas))
            self.disponibles_dkv.configure(text=len(self.listado_dkv))
        #Cerramos la ventana de carga
        self.CerrarVentanaCarga()
        #Reiniciamos los rangos de los Spinbox de los seguros
        self.RangosSpinbox()
        #Si no se establece conexión con la DB (Lo puse al final para que se cierre antes la ventana de carga)
        if conexion==False:
            #Informamos de que no se pudo establecer la conexion con el servidor
            mb.showerror("ERROR", "No se pudo conectar a la base de datos.")

    #Metodo para establecer los rangos a los Spinbox de los seguros
    def RangosSpinbox(self):
        #Fijamos como 0 en ambos Spinbox para resetearlos
        self.entrada_adeslas.set(0)
        self.entrada_dkv.set(0)
        #Establecemos las condiciones
        if len(self.listado_adeslas)>=10:
            self.entrada_adeslas.configure(to=10)
        else:
            self.entrada_adeslas.configure(to=len(self.listado_adeslas))
        if len(self.listado_dkv)>=5:
            self.entrada_dkv.configure(to=5)
        else:
            self.entrada_dkv.configure(to=len(self.listado_dkv))

    #Metodo para citar los pacientes elegidos
    def InsertarDB(self):
        #Obtenemos la fecha formateada
        fecha=self.EnviarFecha()
        #Controlar si la fecha es correcta, es decir, que no sea una fecha no existente.
        if fecha!=False:
            #Obtenemos datos de los campos de adeslas y dkv
            peticion_adeslas=int(self.entrada_adeslas.get())
            peticion_dkv=int(self.entrada_dkv.get())
            #Si uno de los dos es mayor que 0 procedemos a conectar con la BD (evitamos hacer trabajar a la BD de forma innecesaria)
            if peticion_adeslas>0 or peticion_dkv>0:
                #Preguntamos al usuario si realmente desea insertarlos en la BD
                respuesta=mb.askyesno("Información",f"Se va a proceder a insertar {peticion_adeslas+peticion_dkv} citas.")
                #Si afirma llamamos al método encargado y los insertamos
                if respuesta==True:
                    #Randomizamos los pacientes a elegir
                    elegidos_adeslas, elegidos_dkv=self.conectar.ElegirPacientes(self.listado_adeslas, self.listado_dkv, peticion_adeslas, peticion_dkv)
                    #Citamos los pacientes elegidos
                    self.conectar.Insertar(elegidos_adeslas, elegidos_dkv, fecha)
                    #Llamamos al metodo encargado de escribir en el scrolledtext las inserciones que acabamos de realizar (los metemos en una tupla a ambos para ser procesados correctamente)
                    self.MostrarInserciones((elegidos_adeslas,elegidos_dkv))
                    #Actualizamos los listados de los pacientes
                    self.ventana.after(1000, self.BusquedaDB)
                else:
                    mb.showerror("Información", "Operación cancelada.")
            else:
                mb.showerror("ERROR", "Los campos de Adeslas y DKV están en 0.")
            #Informamos de una fecha incorrecta
        else:
            mb.showerror("ERROR", "Fecha incorrecta.")
        #Reiniciamos los rangos de los Spinbox de los seguros
        self.RangosSpinbox()

    #Metodo escribir en el scrolledtext
    def MostrarInserciones(self, listado):
        #Vaciamos el scrolledtext
        self.scrolledtext.delete(1.0, tk.END)
        #Insertamos el encabezado
        self.scrolledtext.insert(tk.END, self.encabezado) #Lo debemos volver a insertar ya que no encontre forma de eliminar a partir de una linea especifica, siempre se borraba todo o nada
        operacion=0
        #Recorremos la lista de valores
        for x in range(len(listado)):
            #Recorremos la sublista de valores, es decir, Adeslas y DKV
            for y in range(len(listado[x])):
                operacion+=1
                #Extraemos los datos del paciente en cuestion
                nombre=listado[x][y][2]
                apellido=str(listado[x][y][3])
                nombre_completo=str(nombre)+" "+str(apellido)
                seguro=str(listado[x][y][4])
                consultas=str(listado[x][y][10])
                #Lo fusionamos en una unica cadena (string) y le agregamos los espacios
                fila=f"{operacion:<10}{nombre_completo:<50}{seguro:<10}{consultas:<10}"
                #La insertamos en el scrolledtext siempre desde el final para mejor organizacion
                self.scrolledtext.insert(tk.END, fila)

    #Metodo para cambiar el estado de la ventana principal
    def EstadoVentana(self, estado):
        self.ventana.attributes("-disabled", estado) #De esta forma prohibimos cualquier interacción con la ventana: valor 1 desactivado; valor 0 activado
        if estado==0:
            self.ventana.attributes("-topmost", "true") #Volvemos a mostrar la ventana principal al frente

    #Metodo para salir del programa
    def Salir(self):
        sys.exit(0)

#Bloque principal y creacion de objeto
iniciar=Aplicacion()
