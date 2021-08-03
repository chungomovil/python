#Importamos modulos necesarios
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
import sys, os

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
    imagenes=str(ruta)+"\\images"

#Creamos la clase
class Calculadora():
    #Creamos el metodo constructor
    def __init__(self):
        #Creamos la ventana
        self.ventana=tk.Tk()
        self.ventana.title("Calculadora de Estimaciones")
        #Creamos una lista para los botones de los digitos
        self.listabotones=[]
        #Creamos la variable que almacenara lo que vayamos pulsando
        self.texto=""
        #Almacenamos las imagenes en variables
        self.imagen_ventana=tk.PhotoImage(file=os.path.join(imagenes, "calculator.png"))
        self.imagen_retroceder=tk.PhotoImage(file=os.path.join(imagenes, "back-arrow.png"))
        self.imagen_borrar=tk.PhotoImage(file=os.path.join(imagenes, "trash.png"))
        self.imagen_igual=tk.PhotoImage(file=os.path.join(imagenes, "equal.png"))
        self.imagen_suma=tk.PhotoImage(file=os.path.join(imagenes, "add.png"))
        #Creamos los distintos frames para las secciones de la aplicacion
        self.framesuperior=ttk.Frame(self.ventana, borderwidth="2", relief="groove") #El atributo "groove" es el estilo del borde
        self.framesuperior.grid(column=0, row=0, columnspan=4, padx=40, pady=(20, 0), sticky="we")
        self.framesuperior.columnconfigure(0, weight=1) #Usamos metodo "columnconfigure" y "rowconfigure" para ajustar el ancho y alto relativo de sus celdas interiores
        self.framebotonesdigitos=ttk.Frame(self.ventana, borderwidth="2", relief="groove")
        self.framebotonesdigitos.grid(column=0, row=1, padx=(40,0))
        self.framebotonesfechas=ttk.Frame(self.ventana, borderwidth="2", relief="groove")
        self.framebotonesfechas.grid(column=1, row=1, sticky="ns")
        self.framebotonsumar=ttk.Frame(self.ventana, borderwidth="2", relief="groove")
        self.framebotonsumar.grid(column=2,row=1, sticky="ns")
        self.framebotonsumar.rowconfigure(0, weight=1)
        self.framebotonesacciones=ttk.Frame(self.ventana, borderwidth="2", relief="groove")
        self.framebotonesacciones.grid(column=3, row=1, padx=(0, 40), sticky="ns")
        self.framebotonesacciones.rowconfigure(0, weight=1)
        self.framebotonesacciones.rowconfigure(1, weight=1)
        self.framebotonesacciones.rowconfigure(2, weight=2) 
        self.frameporcentaje=ttk.Frame(self.ventana, borderwidth="2", relief="groove")
        self.frameporcentaje.grid(column=0, row=2, columnspan=4, padx=40, pady=10, sticky="w")
        self.frameresultado=ttk.Frame(self.ventana, borderwidth="2", relief="groove")
        self.frameresultado.grid(column=0, row=3, columnspan=4, padx=40, sticky="we") 
        #Llamamos a los distintos metodos que necesitamos de su ejecucion inicial
        self.CrearBotonesDigitos()
        self.CrearBotonesFechas()
        self.CrearBotonesAcciones()
        self.CrearBotonesPorcentaje()
        self.CrearVisorSuperior()
        self.CrearVisorResultado()
        #Creamos una etiqueta con un estilo para el visor del resultado
        self.visorresultado.tag_config("encabezado", foreground="blue")
        #Creamos el encabezado del visor del resultado
        self.encabezadoresultado=f"{'SOLO DÍAS':<20}{'SOLO HORAS':<20}{'SOLO MINUTOS'}\n"
        #Limpiamos el visor del resultado
        self.visorresultado.delete("1.0", tk.END)
        #Insertamos el encabezado del visor del resultado y le aplicamos el estilo
        self.visorresultado.insert(tk.END, self.encabezadoresultado, "encabezado")
        #Capturamos eventos del teclado y enviamos su valor al metodo encargado
        self.ventana.bind("<Key>", self.TeclaPulsada)
        #Tamaño de la ventana
        self.ventana.geometry("600x700")
        self.ventana.resizable(False, False)
        #Icono de la ventana (y barra de tareas al ejecutarse en ".exe")
        self.ventana.iconphoto(False, self.imagen_ventana)
        #Bucle de la ventana
        self.ventana.mainloop()

    #Metodo para crear los botones del 0 a 9
    def CrearBotonesDigitos(self):
        #Variable que almacena el numero del boton
        pos=9
        #Creamos dos bucles, el segundo cuenta hacia atras para que la posicion de los botones se parezca a una calculadora
        for x in range(3):
            for y in range (2, -1,-1):
                #Creamos el boton y enviamos su valor por lambda al metodo encargado
                boton=ttk.Button(self.framebotonesdigitos, width=13, text=str(pos), command=lambda numero=pos: self.NumerosPulsados(numero)) #!OJO! Recordar almacenar el valor en una variable de la funcion lambda "numero=pos"
                boton.grid(column=y, row=x, ipady=20)
                #Lo agregamos al listado de botones
                self.listabotones.append(boton)
                #Pasamos al siguiente numero
                pos-=1
        #Creamos el boton "0"
        boton=ttk.Button(self.framebotonesdigitos, text="0", command=lambda numero=pos: self.NumerosPulsados(numero))
        boton.grid(column=0, row=4, columnspan=3, ipady=20, sticky="we")
        #Lo agregamos a la lista de botones
        self.listabotones.append(boton)

    #Metodo para crear los botones del formato de la fecha
    def CrearBotonesFechas(self):
        #Creamos la etiqueta
        encabezadofecha=ttk.Label(self.framebotonesfechas, text="FORMATO")
        encabezadofecha.grid(column=0, row=0, padx=10, pady=15)
        #Creamos los botones y enviamos el valor por lambda al metodo encargado
        self.botondia=ttk.Button(self.framebotonesfechas, text="DÍAS", command=lambda: self.FormatoPulsado("D"))
        self.botondia.grid(column=0, row=1, padx=10, pady=15, ipady=5)
        self.botonhora=ttk.Button(self.framebotonesfechas, text="HORAS", command=lambda: self.FormatoPulsado("H"))
        self.botonhora.grid(column=0, row=2, padx=10, pady=15, ipady=5)
        self.botonminuto=ttk.Button(self.framebotonesfechas, text="MINUTOS", command=lambda: self.FormatoPulsado("M"))
        self.botonminuto.grid(column=0, row=3, padx=10, pady=15, ipady=5)
    
    #Metodo para crear los botones, suma, retroceder, borrar e igual
    def CrearBotonesAcciones(self):
        #Creamos los botones
        self.botonsumar=ttk.Button(self.framebotonsumar, image=self.imagen_suma, compound="center", command=self.SumarPulsado) #Los botones tendran imagen, con "compound" ponemos la imagen en posicion relativa con respecto al boton
        self.botonsumar.grid(column=0, row=0, sticky="ns")
        self.botonreset=ttk.Button(self.framebotonesacciones, image=self.imagen_borrar, compound="center", command=self.Borrar)
        self.botonreset.grid(column=0, row=0, sticky="ns")
        self.botoncorregir=ttk.Button(self.framebotonesacciones, image=self.imagen_retroceder, compound="center", command=self.Retroceder)
        self.botoncorregir.grid(column=0, row=1, sticky="ns")
        self.botonresultado=ttk.Button(self.framebotonesacciones, image=self.imagen_igual, compound="center", command=self.MostrarResultado)
        self.botonresultado.grid(column=0, row=2, sticky="ns")

    #Metodo para crear el apartado del porcentaje
    def CrearBotonesPorcentaje(self):
        #Creamos la etiqueta
        encabezado=ttk.Label(self.frameporcentaje, text="Gestión de Proyecto (%)", anchor="w")
        encabezado.grid(column=0, row=0, padx=10, pady=(5, 0), sticky="we")
        #Creamos el spinbox
        self.porcentaje=ttk.Spinbox(self.frameporcentaje, from_=0, to=20, state="readonly")
        #Lo ponemos en 10 por defecto
        self.porcentaje.set("10")
        self.porcentaje.grid(column=0, row=1, padx=10, pady=(0, 5))

    #Metodo para crear el visor que muestra lo que vayamos escribiendo
    def CrearVisorSuperior(self):
        #Creamos el visor
        self.visorsuperior=ttk.Label(self.framesuperior, text="", background="white", anchor="e", font=("Arial", 12), wraplength=520) #El atributo "wraplength" controla el overflow por pixeles haciendo retornos de carro
        self.visorsuperior.grid(column=0, row=0, ipady=10, sticky="we")
    
    #Metodo para crear el visor que muestra el resultado de la operacion
    def CrearVisorResultado(self):
        #Creamos la etiqueta del titulo
        titulo=ttk.Label(self.frameresultado, text="RESULTADO", anchor="center", font=("Arial", 18))
        titulo.grid(column=0, row=0, padx=20, pady=10, sticky="we")
        #Creamos el scrolledtext que mostrara el resultado
        self.visorresultado=st.ScrolledText(self.frameresultado, width=58, height=10)
        self.visorresultado.grid(column=0, row=1, padx=20, pady=10)
    
    #Metodo que recibe el numero pulsado
    def NumerosPulsados(self, numero):
        #Escribir en el visor superior
        self.visorsuperior.configure(text=self.RetornarTexto(numero))
    
    #Metodo que recibe el formato pulsado
    def FormatoPulsado(self, formato):
        self.visorsuperior.configure(text=self.RetornarTexto(formato))
    
    #Metodo que se activa si se pulsa el boton de sumar
    def SumarPulsado(self):
        self.visorsuperior.configure(text=self.RetornarTexto("+"))
    
    #Metodo que se activa si se pulsa el boton de retroceder
    def Retroceder(self):
        #Creamos una nueva cadena cortando su ultimo valor
        self.texto=self.texto[:-1]
        self.visorsuperior.configure(text=self.RetornarTexto())

    #Metodo que se activa al pulsar el boton de borrar
    def Borrar(self):
        #Vaciamos la cadena
        self.texto=""
        #Reestablecemos el texto del visor superior
        self.visorsuperior.configure(text=self.texto, foreground="black")
        #Desbloqueamos el visor del resultado
        self.visorresultado.configure(state="normal")
        #Vaciamos el visor del resultado
        self.visorresultado.delete("1.0", tk.END)
        #Insertamos el encabezado del visor del resultado
        self.visorresultado.insert(tk.END, self.encabezadoresultado, "encabezado")
        #Llamamos al metodo que habilita y deshabilita las teclas, las habilitamos
        self.BloquearTeclas("enabled")

    #Metodo que recibe la tecla pulsada
    def TeclaPulsada(self, tecla):
        #Obtenemos el codigo de la tecla
        tecla_codigo=tecla.keycode
        #Obtenemos el caracter
        tecla_caracter=tecla.char
        #Algoritmo para saber cual metodo llamar segun la tecla pulsada
        if self.texto!="ERROR":
            if tecla_codigo>=48 and tecla_codigo<=57 or tecla_codigo>=96 and tecla_codigo<=105:
                self.NumerosPulsados(tecla_caracter)
            elif tecla_codigo==68 or tecla_codigo==72 or tecla_codigo==77:
                tecla_caracter=tecla_caracter.upper()
                self.FormatoPulsado(tecla_caracter)
            elif tecla_codigo==107:
                self.SumarPulsado()
            elif tecla_codigo==8:
                self.Retroceder()
            elif tecla_codigo==13:
                self.MostrarResultado()

    #Metodo pasar todo a dias
    def SumarEnDias(self):
        #Creamos una variable que almacenara la suma total
        suma_total=0
        #Creamos otra variable que almacenara los numeros
        suma=""
        #Analizamos la cadena de botones pulsados
        for x in range(len(self.texto)):
            #Agregamos a la variable "suma" si un valor es entero. ¡OJO! Lo agregamos en formato string para que no se sumen aun
            try:
                numero=int(self.texto[x])
                suma=suma+str(numero)
            #Si se crea una excepcion, es decir, no es entero
            except ValueError:
                #Controlamos que no este vacia la cadena, es decir, que no hayan numeros que sumar
                if len(suma)>0:
                    #Pasamos ahora a entero la cadena de numeros
                    suma=int(suma)
                    #Segun el valor que provoco la excepcion, pasamos la suma a dicho valor temporal
                    if self.texto[x]=="H":
                        suma=suma/8
                    elif self.texto[x]=="M":
                        suma=suma/480
                    #Agregamos a la suma total esta suma
                    suma_total=suma_total+suma
                    #Vaciamos y pasamos a string nuevamente la variable "suma"
                    suma=""
        #Retornamos la suma total con un decimal como maximo
        return round(suma_total, 1)
    
    #Metodo para pasar todo a horas (similar al metodo anterior)
    def SumarEnHoras(self):
        suma_total=0
        suma=""
        for x in range(len(self.texto)):
            try:
                numero=int(self.texto[x])
                suma=suma+str(numero)
            except ValueError:
                if len(suma)>0:
                    suma=int(suma)
                    if self.texto[x]=="D":
                        suma=suma*8
                    elif self.texto[x]=="M":
                        suma=suma/60
                    suma_total=suma_total+suma
                    suma=""
        return round(suma_total, 1)

    #Metodo para pasar todo a minutos (similar al metodo anterior)
    def SumarEnMinutos(self):
        suma_total=0
        suma=""
        for x in range(len(self.texto)):
            try:
                numero=int(self.texto[x])
                suma=suma+str(numero)
            except ValueError:
                if len(suma)>0:
                    suma=int(suma)
                    if self.texto[x]=="D":
                        suma=suma*480
                    elif self.texto[x]=="H":
                        suma=suma*60
                    suma_total=suma_total+suma
                    suma=""
        return suma_total

    #Metodo para pasar todo al maximo que se pueda en cada rango
    def SumaInteligente(self, minutos):
        #Establecemos una variable con el total de minutos
        suma_total=minutos
        #Pasamos los minutos a dias en una division sin resto
        dias=suma_total//480
        #Calculamos el resto de la operacion anterior
        suma_total=suma_total-(dias*480)
        #El resto lo pasamos a horas en una division sin resto
        horas=suma_total//60
        #Calculamos el resto de la operacion anterior
        suma_total=suma_total-(horas*60)
        #El resto resultante seran minutos
        minutos=suma_total
        #Retornamos todos los tiempos
        return (dias, horas, minutos)

    #Metodo para mostrar el resultado
    def MostrarResultado(self):
        #Controlamos que el texto no este vacio
        if len(self.texto)>0:
            #Creamos una variable que almacena el ultimo caracter ingresado
            ultimo=len(self.texto)-1
            #Para que la operacion se realice correctamente, verificamos que el ultimo caracter no sea ni numeros ni el simbolo "+"
            if ord(str(self.texto[ultimo]))==68 or ord(str(self.texto[ultimo]))==72 or ord(str(self.texto[ultimo]))==77:
                #Obtenemos el porcentaje seleccionado
                porcentaje=int(self.porcentaje.get())
                #Almacenamos en variables los dias, horas y minutos
                solodias=self.SumarEnDias()
                solohoras=self.SumarEnHoras()
                solominutos=self.SumarEnMinutos()
                #Calculamos el porcentaje en minutos
                porcentaje_final=(solominutos//100)*porcentaje
                #Calculamos el resto del porcentaje
                porcentaje_programacion=solominutos-porcentaje_final
                #Pasamos los minutos en el maximo tiempo de cada rango llamando al metodo encargado
                dias, horas, minutos=self.SumaInteligente(solominutos)
                porcentaje_dias, porcentaje_horas, porcentaje_minutos=self.SumaInteligente(porcentaje_final)
                programacion_dias, programacion_horas, programacion_minutos=self.SumaInteligente(porcentaje_programacion)
                #Confeccionamos los textos que se escribiran en el cuerpo del scrolledtext
                texto=f"{str(solodias)+' Días':<20}{str(solohoras)+' Horas':<20}{str(solominutos)+' Minutos'}\n"
                encabezado_suma_inteligente=f"\n\n\nSUMA SIMPLIFICADA: "
                encabezado_porcentaje_inteligente=f"\nGESTIÓN DE PROYECTO ({porcentaje}%): "
                encabezado_programacion_inteligente=f"\nPROGRAMACIÓN: "
                texto_suma_inteligente=f"{dias} Días, {horas} Horas y {minutos} Minutos"
                texto_porcentaje_inteligente=f"{porcentaje_dias} Días, {porcentaje_horas} Horas y {porcentaje_minutos} Minutos"
                texto_programacion_inteligente=f"{programacion_dias} Días, {programacion_horas} Horas y {programacion_minutos} Minutos"
                #Habilitamos la escritura en el scrolledtext
                self.visorresultado.configure(state="normal")
                #Vaciamos el scrolledtext
                self.visorresultado.delete("1.0", tk.END)
                #Insertamos el encabezado de la tabla y los resultados de las operaciones
                self.visorresultado.insert(tk.END, self.encabezadoresultado, "encabezado")
                self.visorresultado.insert(tk.END, texto)
                self.visorresultado.insert(tk.END, encabezado_suma_inteligente, "encabezado")
                self.visorresultado.insert(tk.END, texto_suma_inteligente)
                self.visorresultado.insert(tk.END, encabezado_porcentaje_inteligente, "encabezado")
                self.visorresultado.insert(tk.END, texto_porcentaje_inteligente)
                self.visorresultado.insert(tk.END, encabezado_programacion_inteligente, "encabezado")
                self.visorresultado.insert(tk.END, texto_programacion_inteligente)
                #Deshabilitamos la escritura en el scrolledtext
                self.visorresultado.configure(state="disabled")
            #Si el ultimo caracter es un numero o el simbolo "+"
            else:
                #Cambia el texto a error
                self.texto="ERROR"
                #Escribe en el visor superior "ERROR" en rojo
                self.visorsuperior.configure(text=self.texto, foreground="red")
                #Llamamos al metodo que desactiva las teclas
                self.BloquearTeclas("disabled")

    #Metodo para verificar el texto
    def ControlTexto(self, caracter):
        #Pasamos el parametro del metodo a string
        caracter=str(caracter)
        #Controlamos que el texto no este vacio
        if len(self.texto)>0:
            #Capturamos el caracter anterior
            anterior=len(self.texto)-1
            #Analizamos si insertar o no el caracter actual dependiendo de cual sea el anterior
            if ord(str(self.texto[anterior]))>=48 and ord(str(self.texto[anterior]))<=57: #El metodo "ord" devuelve el caracter en formato ASCII
                if ord(caracter)>=48 and ord(caracter)<=57:
                    return True
                elif ord(caracter)==68 or ord(caracter)==72 or ord(caracter)==77:
                    return True
                else:
                    return False
            elif ord(str(self.texto[anterior]))==68 or ord(str(self.texto[anterior]))==72 or ord(str(self.texto[anterior]))==77:
                if ord(caracter)>=48 and ord(caracter)<=57:
                    return False
                elif ord(caracter)==43:
                    return True
                else:
                    self.texto=self.texto[:anterior]
                    return True
            else:
                if ord(caracter)>=48 and ord(caracter)<=57:
                    return True
                else:
                    return False                  
        else:
            if ord(caracter)>=48 and ord(caracter)<=57:
                return True
            else:
                return False

    #Metodo para retornar el texto actualizado
    def RetornarTexto(self, caracter=""):
        texto_convertido=""
        #Controlamos que la cadena no esta vacia
        if caracter!="":
            #Llamamos al metodo que verifica el texto
            if self.ControlTexto(caracter):
                self.texto+=str(caracter)
        #Formateamos la cadena que se mostrara
        for x in range(len(self.texto)):
            if self.texto[x]=="D":
                texto_convertido=texto_convertido+" Días"
            elif self.texto[x]=="H":
                texto_convertido=texto_convertido+" Horas"
            elif self.texto[x]=="M":
                texto_convertido=texto_convertido+" Minutos"
            elif self.texto[x]=="+":
                texto_convertido=texto_convertido+" + "
            else:
                texto_convertido=texto_convertido+str(self.texto[x])
        #La retornamos
        return texto_convertido
    
    #Metodo para bloquear las teclas
    def BloquearTeclas(self, estado):
        #Bloqueamos los botones del 0 al 9
        for x in range(len(self.listabotones)):
            self.listabotones[x].configure(state=estado)
        #Bloqueamos el resto de botones (menos el de borrar todo)
        self.botondia.configure(state=estado)
        self.botonhora.configure(state=estado)
        self.botonminuto.configure(state=estado)
        self.botonsumar.configure(state=estado)
        self.botoncorregir.configure(state=estado)
        self.botonresultado.configure(state=estado)

#Ejecutamos el programa
if __name__=="__main__":
    iniciar=Calculadora()
