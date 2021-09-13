#Importamos modulos necesarios
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import sys
from datetime import date, datetime, timedelta
#Importamos el modulo con la sintaxis de la BD
import operaciones

#Creamos la clase
class Aplicacion:

    #Creamos el metodo constructor
    def __init__(self):
        #Importamos la clase del modulo con las operacion de la DB
        self.conectar=operaciones.Operaciones()
        self.ventana=tk.Tk()
        self.ventana.title("AUTOMATIZAR CITAS")
        #Creamos el menu
        menubar=tk.Menu(self.ventana)
        self.ventana.configure(menu=menubar)
        opciones=tk.Menu(menubar, tearoff=0)
        opciones.add_command(label="SALIR", command=self.Salir)
        menubar.add_cascade(label="Opciones", menu=opciones)
        self.estilo_etiquetas_global=ttk.Style(self.ventana)
        self.estilo_etiquetas_global.configure("TLabel", font=("Arial", 12))
        self.estilo_etiqueta_seguros=ttk.Style(self.ventana)
        self.estilo_etiqueta_seguros.configure("Seguro.TLabel", font=("Arial", 14, "bold"))
        self.estilo_etiqueta_fecha=ttk.Style(self.ventana)
        self.estilo_etiqueta_fecha.configure("Fecha.TLabel", font=("Arial", 12, "bold"), foreground="#004AAD", borderwidth=1, relief="solid")
        self.frame1=ttk.Frame(self.ventana)
        self.frame1.pack(side=tk.TOP, fill=tk.BOTH, pady=20)
        self.frame1.columnconfigure(0, weight=1)
        self.frame2=ttk.Frame(self.ventana)
        self.frame2.pack(side=tk.TOP, pady=20)
        self.frame2.grid_columnconfigure(0, weight=1, uniform="grupo")
        self.frame2.grid_columnconfigure(1, weight=1, uniform="grupo")
        self.frame3=ttk.Frame(self.ventana)
        self.frame3.pack(side=tk.TOP, fill=tk.BOTH)
        self.frame3.grid_columnconfigure(0, weight=1, uniform="grupo")
        self.frame3.grid_columnconfigure(1, weight=1, uniform="grupo")
        self.frame4=ttk.Frame(self.ventana)
        self.frame4.pack(side=tk.BOTTOM, fill=tk.BOTH)
        #Llamamos a los metodos necesarios
        self.Header()
        self.FormularioSeguros()
        self.FormularioFecha()
        #El metodo 'RecibirFecha' lo ejecutamos desde el metodo constructor para que al iniciar el programa ya se copie la fecha actual en los Spinbox
        self.RecibirFecha()
        self.BusquedaDB()
        self.ventana.minsize(400, 600)
        self.ventana.mainloop()

    #Metodo para crear el formulario de entrada de datos
    def Header(self):
        self.Encabezado=ttk.Label(self.frame1, text="AUTOMATIZAR CITAS", foreground="blue", font=("Arial", 20)) #El atributo anchor viene siendo como un align
        self.Encabezado.grid(column=0, row=0)
        self.titulo_disponibles=ttk.Label(self.frame2, text="Disponibles", font=("Arial", 14, "bold"))
        self.titulo_disponibles.grid(column=0, row=0, columnspan=2, pady=(0, 20))
        self.titulo_disponibles_adeslas=ttk.Label(self.frame2, text="Adeslas", anchor="center", borderwidth=1, relief="solid")
        self.titulo_disponibles_adeslas.grid(column=0, row=1, ipadx=5, sticky="we")
        self.disponibles_adeslas=ttk.Label(self.frame2, text="---", anchor="center", foreground="#5DADE2", font=("Arial", 18, "bold"), borderwidth=1, relief="solid")
        self.disponibles_adeslas.grid(column=0, row=2, sticky="we")
        self.titulo_disponibles_dkv=ttk.Label(self.frame2, text="DKV", anchor="center", borderwidth=1, relief="solid")
        self.titulo_disponibles_dkv.grid(column=1, row=1, ipadx=5, sticky="we")
        self.disponibles_dkv=ttk.Label(self.frame2, text="---", anchor="center", foreground="#2ECC71", font=("Arial", 18, "bold"), borderwidth=1, relief="solid")
        self.disponibles_dkv.grid(column=1, row=2, sticky="we")
        self.titulo5=ttk.Label(self.frame4, text="Pacientes citados", anchor="center", font=("Arial", 14))
        self.titulo5.grid(column=0, row=5, columnspan=2, padx=5, pady=5, sticky="we")
        self.scrolledtext=st.ScrolledText(self.frame4, width=80, height=20)
        self.scrolledtext.grid(column=0, row=6, columnspan=2, padx=10, pady=5)
        #Agregamos el encabezado al scrolledtext (Recordar que debemos de partir desde el final para una mejor organizacion)
        self.encabezado=f"{'NUMERO':<10}{'NOMBRE':<50}{'SEGURO':<10}{'CONSULTAS':<10}"
        self.scrolledtext.insert(tk.END, self.encabezado)

    def FormularioSeguros(self):
        self.frame_seguros=ttk.Frame(self.frame3)
        self.frame_seguros.grid(column=1, row=0, padx=50, sticky="nswe")
        self.frame_seguros.columnconfigure(0, weight=1)
        self.frame_seguros.columnconfigure(1, weight=1)
        self.titulo3=ttk.Label(self.frame_seguros, text="Adeslas", style="Seguro.TLabel")
        self.titulo3.grid(column=0, row=2, pady=10)
        self.dato3=ttk.Spinbox(self.frame_seguros, from_=0, to=10, width=10, state="readonly", font=("Arial", 12))
        self.dato3.set(0)
        self.dato3.grid(column=0, row=3, pady=10)
        self.titulo4=ttk.Label(self.frame_seguros, text="DKV", style="Seguro.TLabel")
        self.titulo4.grid(column=1, row=2, pady=10)
        self.dato4=ttk.Spinbox(self.frame_seguros, from_=0, to=10, width=10, state="readonly", font=("Arial", 12))
        self.dato4.set(0)
        self.dato4.grid(column=1, row=3, pady=10)
        self.confirmar2=ttk.Button(self.frame_seguros, width=20, text="CITAR", command=self.BusquedaDB)
        self.confirmar2.grid(column=0, row=4, columnspan=2, pady=20)

    #Metodo que crea el formulario para entrada de fechas
    def FormularioFecha(self):
        self.frame_fecha=ttk.Frame(self.frame3)
        self.frame_fecha.grid(column=0, row=0, padx=50, sticky="nswe")
        self.frame_fecha.columnconfigure(0, weight=1)
        self.frame_fecha.columnconfigure(1, weight=1)
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

    
    def AbrirVentanaCarga(self):
        self.EstadoVentana(1)
        self.ventanacarga=tk.Toplevel()
        self.ventanacarga.title("Cargando datos...")
        self.ventanacarga.attributes("-topmost", "true")
        self.ventanacarga.geometry("320x100")
        self.ventanacarga.resizable(False, False)
        self.titulocarga=ttk.Label(self.ventanacarga, text="", anchor="center", font=("Arial", 13, "bold"))
        self.titulocarga.grid(column=0, row=0, sticky="we", padx=10, pady=5)
        self.barracarga=ttk.Progressbar(self.ventanacarga, length=300, mode="determinate")
        self.barracarga.grid(column=0, row=1, sticky="we", padx=10)
    
    def CerrarVentanaCarga(self):
        self.ventanacarga.destroy()
        self.EstadoVentana(0)

    #Metodo para obtener fecha actual e insertarla en el formulario
    def RecibirFecha(self):
        actual=datetime.now()
        #Desglosamos la fecha actual
        dia=actual.strftime("%d")
        mes=actual.strftime("%m")
        anio=actual.strftime("%Y")
        hora=actual.strftime("%H")
        minuto=actual.strftime("%M")
        #Insertamos cada campo de la fecha en su Spinbox
        self.dia.set(dia)
        self.mes.set(mes)
        self.anio.set(anio)
        self.hora.set(hora)
        #self.minuto.set(minuto)

    #Metodo para devolver la fecha introducida por el usuario
    def EnviarFecha(self):
        #Obtenemos los datos de los diferentes Spinbox
        dia=self.dia.get()
        mes=self.mes.get()
        anio=self.anio.get()
        hora=self.hora.get()
        #minuto=self.minuto.get()
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

    #Metodo para mostrar mensajes en la Label 'Estado' sobre las operaciones que se van realizando
    def mensaje(self, operacion):
        if operacion==1:
            texto="Conectando a la base de datos..."
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
        #Este metodo de la ventana permite refrescar la interfaz visual y no esperar a que termine el hilo de ejecucion de otra funcion
        self.ventana.update()

    #Metodo para enviar datos a la BD
    def BusquedaDB(self):
        self.AbrirVentanaCarga()
        #Mostramos mensaje de estado del programa
        self.mensaje(1)
        #Este metodo de la ventana hace que la interfaz visual se pause un numero de milisegundos especificados (basicamente para leer el mensaje)
        self.ventana.after(1000)
        #Establecemos conexion a la base de datos y retornamos resultado
        conexion=self.conectar.AbrirConexion()
        #Si se establece la conexion
        if conexion!=False:
            self.mensaje(2)
            self.ventana.after(1000)
            #Retornamos la lista final de pacientes recientes
            recientes=self.conectar.ListarRecientes()
            self.mensaje(3)
            #Retornamos la lista final de recientes que tengan menos de 3 asistencias o no hayan acudido hoy
            #No hace falta pausar la interfaz ya que esta operacion tarda un par de segundos
            recientes_con_rangos=self.conectar.CalcularPeriodos(recientes)
            self.mensaje(4)
            self.ventana.after(500)
            #Obtenemos la lista de los pacientes filtrados por seguro
            self.listado_adeslas, self.listado_dkv=self.conectar.FiltrarSeguro(recientes_con_rangos)
            self.disponibles_adeslas.configure(text=len(self.listado_adeslas))
            self.disponibles_dkv.configure(text=len(self.listado_dkv))
        else:
            #Informamos de que no se pudo establecer la conexion con el servidor
            mb.showerror("ERROR", "No se pudo conectar a la base de datos.")
            self.mensaje("")
        self.CerrarVentanaCarga()

    """def InsertarDB(self):
        #Obtenemos el resultado de dicho metodo
        fecha=self.EnviarFecha()
        #Controlar si la fecha es correcta, es decir, que no sea una fecha no existente.
        if fecha!=False:
            #Obtenemos datos de los campos de adeslas y dkv
            peticion_adeslas=int(self.dato3.get())
            peticion_dkv=int(self.dato4.get())
            #Si uno de los dos es mayor que 0 procedemos a conectar con la BD (evitamos hacer trabajar a la BD de forma innecesaria)
            if peticion_adeslas>0 or peticion_dkv>0:
            #Si devuelve falte, es decir, que es superior lo exigido a lo existente
                if listado_final==False:
                    #Informamos al usuario del error
                    mb.showwarning("VALOR INCORRECTO","Algun valor supera la cantidad de pacientes disponibles.")
                else:
                    #Preguntamos al usuario si realmente desea insertarlos en la BD
                    respuesta=mb.askyesno("Informacion",f"Se va a proceder a insertar {len(listado_final[0])+len(listado_final[1])} citas.")
                    #Si afirma llamamos al metodo encargado y los insertamos
                    if respuesta==True:
                        self.conectar.Insertar(listado_final, fecha)
                        self.mensaje(5)
                        self.ventana.after(1000)
                        #Llamamos al metodo encargado de escribir en el scrolledtext las inserciones que acabamos de realizar
                        self.MostrarInserciones(listado_final)
                        self.mensaje(6)
                    #Si rechaza vaciamos el campo de estado del programa
                    else:
                        self.mensaje("")
                        self.CerrarVentanaCarga()
                            #Informamos de que ambos campos de seguros estan a 0
        else:
            mb.showerror("ERROR", "Los campos de Adeslas y DKV estan en 0.")
        #Informamos de una fecha incorrecta
        else:
            mb.showerror("ERROR", "Fecha incorrecta.")"""

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

    def EstadoVentana(self, estado):
        self.ventana.attributes("-disabled", estado)
        if estado==0:
            self.ventana.attributes("-topmost", "true")

    #Metodo para salir del programa
    def Salir(self):
        sys.exit(0)

#Bloque principal y creacion de objeto
iniciar=Aplicacion()
