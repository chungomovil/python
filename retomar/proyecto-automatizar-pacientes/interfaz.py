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
        #Llamamos a los metodos necesarios
        self.FormularioEntrada()
        self.FormularioFecha()
        #El metodo 'RecibirFecha' lo ejecutamos desde el metodo constructor para que al iniciar el programa ya se copie la fecha actual en los Spinbox
        self.RecibirFecha()
        #Parametros de la ventana
        self.ventana.minsize(400, 600)
        self.ventana.mainloop()

    #Metodo para crear el formulario de entrada de datos
    def FormularioEntrada(self):
        self.Encabezado=ttk.Label(self.ventana, text="AUTOMATIZAR CITAS", anchor="center", foreground="blue", font=("Arial", 20)) #El atributo anchor viene siendo como un align
        self.Encabezado.grid(column=0, row=0, columnspan=2, padx=200, pady=50, sticky="nswe")
        self.titulo3=ttk.Label(self.ventana, text="Total Adeslas", anchor="center", font=("Arial", 12))
        self.titulo3.grid(column=0, row=2, padx=10, pady=10)
        self.dato3=ttk.Spinbox(self.ventana, from_=0, to=10, width=10, state="readonly", font=("Arial", 12))
        self.dato3.set(0)
        self.dato3.grid(column=0, row=3, padx=10, pady=10)
        self.titulo4=ttk.Label(self.ventana, text="Total DKV", anchor="center", font=("Arial", 12))
        self.titulo4.grid(column=1, row=2, padx=10, pady=10)
        self.dato4=ttk.Spinbox(self.ventana, from_=0, to=10, width=10, state="readonly", font=("Arial", 12))
        self.dato4.set(0)
        self.dato4.grid(column=1, row=3, padx=10, pady=10)
        self.confirmar2=ttk.Button(self.ventana, width=20, text="Confirmar", command=self.EnviarDatos)
        self.confirmar2.grid(column=0, row=4, columnspan=2, padx=10, pady=20)
        self.titulo5=ttk.Label(self.ventana, text="Pacientes citados", anchor="center", font=("Arial", 14))
        self.titulo5.grid(column=0, row=5, columnspan=2, padx=5, pady=5, sticky="we")
        self.scrolledtext=st.ScrolledText(self.ventana, width=80, height=20)
        self.scrolledtext.grid(column=0, row=6, columnspan=2, padx=10, pady=5)
        #Agregamos el encabezado al scrolledtext (Recordar que debemos de partir desde el final para una mejor organizacion)
        self.encabezado=f"{'NUMERO':<10}{'NOMBRE':<50}{'SEGURO':<10}{'CONSULTAS':<10}"
        self.scrolledtext.insert(tk.END, self.encabezado)
        self.Estado=ttk.Label(self.ventana, text="", foreground="green", font=("Arial", 14))
        self.Estado.grid(column=0, row=7, columnspan=2, padx=10, pady=10, sticky="w")
   
    #Metodo que crea el formulario para entrada de fechas
    def FormularioFecha(self):
        self.fecha=ttk.Frame(self.ventana)
        self.fecha.grid(column=0, row=1, columnspan=2, padx=10, pady=10)
        self.titulo_dia=ttk.Label(self.fecha, text="Dia", anchor="center", font=("Arial", 12))
        self.titulo_dia.grid(column=0, row=0, padx=5, pady=10)
        self.dia=ttk.Spinbox(self.fecha, from_=1, to=31, width=10, state="readonly", font=("Arial", 12))
        self.dia.grid(column=0, row=1, padx=5, pady=10)
        self.titulo_mes=ttk.Label(self.fecha, text="Mes", anchor="center", font=("Arial", 12))
        self.titulo_mes.grid(column=1, row=0, padx=5, pady=10)
        self.mes=ttk.Spinbox(self.fecha, from_=1, to=12, width=10, state="readonly", font=("Arial", 12))
        self.mes.grid(column=1, row=1, padx=5, pady=10)
        self.titulo_anio=ttk.Label(self.fecha, text="Año", anchor="center", font=("Arial", 12))
        self.titulo_anio.grid(column=2, row=0, padx=5, pady=10)
        self.anio=ttk.Spinbox(self.fecha, from_=2021, to=2030, width=10, state="readonly", font=("Arial", 12))
        self.anio.grid(column=2, row=1, padx=5, pady=10)
        self.titulo_hora=ttk.Label(self.fecha, text="Hora", anchor="center", font=("Arial", 12))
        self.titulo_hora.grid(column=3, row=0, padx=5, pady=10)
        self.hora=ttk.Spinbox(self.fecha, from_=00, to=23, width=10, state="readonly", font=("Arial", 12))
        self.hora.grid(column=3, row=1, padx=5, pady=10)
        self.titulo_minuto=ttk.Label(self.fecha, text="Minutos", anchor="center", font=("Arial", 12))
        self.titulo_minuto.grid(column=4, row=0, padx=5, pady=10)
        self.minuto=ttk.Spinbox(self.fecha, from_=0, to=59, width=10, state="readonly", font=("Arial", 12))
        self.minuto.grid(column=4, row=1, padx=5, pady=10)

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
        self.minuto.set(minuto)

    #Metodo para devolver la fecha introducida por el usuario
    def EnviarFecha(self):
        #Obtenemos los datos de los diferentes Spinbox
        dia=self.dia.get()
        mes=self.mes.get()
        anio=self.anio.get()
        hora=self.hora.get()
        minuto=self.minuto.get()
        #Transformamos en una unica cadena (string) estos datos dandole el formato de una fecha
        fecha_nueva=anio+"-"+mes+"-"+dia+" "+hora+":"+minuto+":00"
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
        elif operacion==2:
            texto="Obteniendo pacientes recientes..."
        elif operacion==3:
            texto="Calculando asistencias en el mes..."
        elif operacion==4:
            texto="Verificando peticion del usuario..."
        elif operacion==5:
            texto="Citando pacientes..."
        elif operacion==6:
            texto="Operacion realizada correctamente."
        else:
            texto=operacion
        self.Estado.configure(text=texto)
        #Este metodo de la ventana permite refrescar la interfaz visual y no esperar a que termine el hilo de ejecucion de otra funcion
        self.ventana.update()

    #Metodo para enviar datos a la BD
    def EnviarDatos(self):
        #Obtenemos el resultado de dicho metodo
        fecha=self.EnviarFecha()
        #Controlar si la fecha es correcta, es decir, que no sea una fecha no existente.
        if fecha!=False:
            #Obtenemos datos de los campos de adeslas y dkv
            peticion_adeslas=int(self.dato3.get())
            peticion_dkv=int(self.dato4.get())
            #Si uno de los dos es mayor que 0 procedemos a conectar con la BD (evitamos hacer trabajar a la BD de forma innecesaria)
            if peticion_adeslas>0 or peticion_dkv>0:
                #Mostramos mensaje de estado del programa
                self.mensaje(1)
                #Este metodo de la ventana hace que la interfaz visual se pause un numero de milisegundos especificados (basicamente para leer el mensaje)
                self.ventana.after(1000)
                self.mensaje(2)
                self.ventana.after(1000)
                #Retornamos la lista final de pacientes recientes
                recientes=self.conectar.ListarRecientes()
                self.mensaje(3)
                #Retornamos la lista final de recientes que tengan menos de 3 asistencias o no hayan acudido hoy
                #No hace falta pausar la interfaz ya que esta operacion tarda un par de segundos
                recientes_con_rangos=self.conectar.CalcularPeriodos(recientes)
                self.mensaje(4)
                self.ventana.after(1000)
                #Obtenemos la lista de los pacientes filtrados por seguro
                listado_final=self.conectar.FiltrarSeguro(peticion_adeslas, peticion_dkv, recientes_con_rangos)
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
            #Informamos de que ambos campos de seguros estan a 0
            else:
                mb.showerror("ERROR", "Los campos de Adeslas y DKV estan en 0.")
        #Informamos de una fecha incorrecta
        else:
            mb.showerror("ERROR", "Fecha incorrecta.")

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

    #Metodo para salir del programa
    def Salir(self):
        sys.exit(0)

#Bloque principal y creacion de objeto
iniciar=Aplicacion()
