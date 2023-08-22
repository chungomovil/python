#Importamos los modulos necesarios
import openai
import credenciales
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
import threading as Hilo
import sys
import win32print
import win32api
import tempfile


class Aplicacion:
    #TOKEN DE OPENAI
    openai.api_key=credenciales.API_KEY()

    #Metodo constructor
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Rocky")
        #CONTINUAR DESARROLLANDO EL SCROLL
        """
        self.contenedor=ttk.Frame(self.ventana)
        self.contenedor.pack(fill=tk.BOTH, expand=1)
        self.canvas=tk.Canvas(self.contenedor)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.scrollventana=tk.Scrollbar(self.contenedor, orient="vertical", command=self.canvas.yview)
        self.scrollventana.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollventana.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.subframe=tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.subframe, anchor="nw")
        """
        #Creamos el menu
        barra_menu=tk.Menu()
        opciones=tk.Menu(barra_menu, tearoff=0)
        opciones.add_command(label="Imprimir", command=self.Imprimir)
        opciones.add_command(label="Salir", command=self.Salir)
        barra_menu.add_cascade(menu=opciones, label="Opciones")
        self.ventana.config(menu=barra_menu)
        #Creamos los estilos para las diferentes etiquetas
        self.estilos=ttk.Style()
        self.estilos.configure("titulo.TLabel", font=("Arial 16 bold"), foreground="green")
        self.estilos.configure("encabezado.TLabel", font=("Arial 10 bold"), borderwidth=2, relief="groove")
        self.estilos.configure("comandos.TLabel", borderwidth=2, relief="groove")
        self.estilos.configure("barracarga.TLabel", font=("Arial, 12 bold"), foreground="red")
        self.titulo=ttk.Label(self.ventana, text="ROCKY", style="titulo.TLabel")
        self.titulo.grid(column=0, row=0, columnspan=2, pady=20)
        self.chat=st.ScrolledText(self.ventana, height=25, font=("Arial 11 bold"))
        self.chat.grid(column=0, row=1, padx=20, columnspan=2, sticky="we")
        self.chat.config(wrap=tk.WORD) #De este modo garantizamo que no se corten las palabras en los saltos de linea del scrolledtext
        #Estilos del scrolledtext (pensé que seria mejor ponerlo por separado y no por Style)
        self.chat.tag_config("rocky", foreground="green", font=("Arial 12 bold"))
        self.chat.tag_config("usuario", foreground="blue", font=("Arial 12 bold"))
        self.chat.tag_config("emoji", font=("Arial 14 bold"))
        self.entrada=ttk.Entry(self.ventana, font=("Arial 11 bold"))
        self.entrada.grid(column=0, row=2, padx=(20, 10), pady=20, ipady=5, sticky="we")
        self.entrada.focus_set() #Para hacer focus automatico en el campo de escribir
        #Llamadas a las funciones que desencadenan las demas operaciones, hay dos ya que se puede llamar pulsando un boton o pulsando ENTER
        self.entrada.bind("<Return>", self.HiloEjecucion)
        self.enviar=ttk.Button(self.ventana, width=10, text="ENVIAR", command=self.HiloEjecucion)
        self.enviar.grid(column=1, row=2, padx=(10, 20), ipady=5)
        self.frameinferior=ttk.Frame(self.ventana)
        self.frameinferior.grid(column=0, row=5, padx=20, pady=10, sticky="we")
        #Reseteamos el chat al cargar el programa
        self.ResetChat()
        #Creamos el frame de los comandos
        self.FrameInferior()
        #Configuracion de las columnas, la columna 0 ocupará todo el espacio que desee
        self.ventana.columnconfigure(0, weight=1)
        #Algoritmo para centrar la ventana
        ventana_ancho=800
        ventana_alto=800
        pantalla_ancho=self.ventana.winfo_screenwidth() #Obtenemos el ancho en píxeles del monitor
        pantalla_alto=self.ventana.winfo_screenheight() #Obtenemos el alto en píxeles del monitor
        pos_x=int((pantalla_ancho/2)-(ventana_ancho/2))
        pos_y=int((pantalla_alto/2)-(ventana_alto/2))
        self.ventana.geometry(f"{ventana_ancho}x{ventana_alto}+{pos_x}+{pos_y}") #Centramos la ventana
        self.ventana.mainloop()
    
    #Metodo para los elementos del frame de los comandos
    def FrameInferior(self):
        self.etiqueta1=ttk.Label(self.frameinferior, text="Lista de comandos", style="encabezado.TLabel")
        self.etiqueta1.grid(column=0, row=0, columnspan=2, pady=10)
        self.etiqueta2=ttk.Label(self.frameinferior, text="COMANDO", style="encabezado.TLabel")
        self.etiqueta2.grid(column=0, row=1, ipadx="5", ipady="5", sticky="we")
        self.etiqueta3=ttk.Label(self.frameinferior, text="DESCRIPCIÓN", style="encabezado.TLabel")
        self.etiqueta3.grid(column=1, row=1, ipadx="5", ipady="5", sticky="we")
        self.etiqueta4=ttk.Label(self.frameinferior, text="!redactor", style="comandos.TLabel")
        self.etiqueta4.grid(column=0, row=2, ipadx="5", ipady="5", sticky="we")
        self.etiqueta5=ttk.Label(self.frameinferior, text="Cambiar a modo 'Experto en redacciones'.", style="comandos.TLabel")
        self.etiqueta5.grid(column=1, row=2, ipadx="5", ipady="5", sticky="we")
        self.etiqueta6=ttk.Label(self.frameinferior, text="!informatico", style="comandos.TLabel")
        self.etiqueta6.grid(column=0, row=3, ipadx="5", ipady="5", sticky="we")
        self.etiqueta7=ttk.Label(self.frameinferior, text="Cambiar a modo 'Experto en informática'.", style="comandos.TLabel")
        self.etiqueta7.grid(column=1, row=3, ipadx="5", ipady="5", sticky="we")
        self.etiqueta8=ttk.Label(self.frameinferior, text="!new", style="comandos.TLabel")
        self.etiqueta8.grid(column=0, row=4, ipadx="5", ipady="5", sticky="we")
        self.etiqueta9=ttk.Label(self.frameinferior, text="Comenzar una nueva conversación.", style="comandos.TLabel")
        self.etiqueta9.grid(column=1, row=4, ipadx="5", ipady="5", sticky="we")
    
    #Metodo que realiza diversas operaciones
    def operaciones(self):
        texto_filtrado=self.Filtrado(self.entrada.get())
        if texto_filtrado!=False:
            #Controles mientras carga la respuesta el robot
            self.ControlChat("USUARIO", self.entrada.get())
            self.BarraCarga(1)
            #Vaciamos el campo de escritura y desactivamos las acciones del chat
            self.entrada.delete(0, tk.END)
            self.entrada.unbind("<Return>")
            self.entrada.configure(state="disabled")
            self.enviar.configure(state="disabled")
            #Obtenemos la respuesta del robot
            respuesta=self.ControlChatGPT()
            #Controlamos si la API retorna una respuesta
            if respuesta!=False:
                #Insertamos la respuesta en el scrolledtext
                self.ControlChat("ROCKY", respuesta)
            else:
                self.ControlChat("ROCKY", "Lo siento no pude encontrar la respuesta, puedes volver a preguntarmelo.")
            #Volvemos a activar las acciones del chat
            self.entrada.bind("<Return>", self.HiloEjecucion)
            self.entrada.configure(state="normal")
            self.enviar.configure(state="normal")
            self.BarraCarga(0)
    
    #Metodo para llamar a la API de ChatGPT
    def ControlChatGPT(self):
        try:
            respuesta=openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.mensajes, max_tokens=500, request_timeout=60) #Llamada a la API de OPENAI, con request_timeout limitamos el tiempo de espera por repuesta
            respuesta=respuesta['choices'][0]['message']['content'] #Como nos devuelve un archivo con estructura JSON extraemos su contenido de esta forma
            self.mensajes.append({"role": "assistant", "content": respuesta}) #Agregamos la respuesta a una lista para que el robot sepa que nos ha respondido y asi tenga contexto en respuestas futuras
        except:
            mb.showerror("ERROR", "ROCKY ha tardado demasiado en responder, volver a intentarlo.")
            respuesta=False
        finally:
            return respuesta
    
    #Metodo para filtrar el texto introducido
    def Filtrado(self, texto):
        comandos=["!redactor", "!informatico", "!new"]
        comando=""
        if texto!="":
            for x in range(len(comandos)):
                if texto==comandos[x]:
                    comando=texto
            if comando!="":
                if comando=="!redactor":
                    self.mensajes.append({"role":"system", "content": "Actúa como si fueras un experto en redacción."})
                if comando=="!informatico":
                    self.mensajes.append({"role":"system", "content":"Actúa como si fueras un experto en informática."})
                if comando=="!new":
                    repuesta=self.Alerta("¿Desea limpiar esta conversación y comenzar una nueva?")
                    if repuesta==True:
                        self.ResetChat()
                    return False
            else:
                self.mensajes.append({"role":"user", "content": texto}) #Agregamos los mensajes del usuario en una lista para que el robot tenga contexto en preguntas futuras
        else:
            return False
    
    #Metodo para escribir en el scrolledtext
    def ControlChat(self, rol, texto):
        self.chat.configure(state="normal")
        self.chat.insert(tk.END, f"\n{rol} dice:\n", rol.lower())
        self.chat.insert(tk.END, "💬", "emoji")
        self.chat.insert(tk.END, f" {texto}\n")
        self.chat.see(tk.END) #De esta forma hacemos que se scrollee automáticamente hacia el final
        self.chat.configure(state="disabled") #Desactivamos la edicion del chat por parte del usuario

    #Metodo para resetear el chat
    def ResetChat(self):
        self.mensajes=[] #Vaciamos la lista, así el robot pierde la información que hayamos introducido anteriormente
        self.chat.config(state="normal")
        self.chat.delete(1.0, tk.END)
        self.ControlChat("ROCKY", "¡Hola, mi nombre es Rocky! ¿En qué te puedo ayudar?")
        self.entrada.delete(0, tk.END)

    #Metodo para mostrar alertas
    def Alerta(self, mensaje):
        pregunta=mb.askyesno(message=mensaje, title="¡Cuidado!")
        return pregunta

    #Metodo para ejecutar la barra de carga
    def BarraCarga(self, estado):
        if estado==1:
            #Creamos la barra de carga y su etiqueta
            self.barracarga_comentario=ttk.Label(self.ventana, text="Cargando respuesta...", style="barracarga.TLabel")
            self.barracarga_comentario.grid(column=0, row=3, padx=20, sticky="w")
            self.barracarga=ttk.Progressbar(self.ventana, length=200, mode="indeterminate" )
            self.barracarga.grid(column=0, row=4, padx=20, sticky="w")
            self.barracarga.start(10)
        else:
            self.barracarga_comentario.destroy()
            self.barracarga.stop()
            self.barracarga.destroy()

    #Metodo para trabajar con hilos, de esta forma no se congela la barra de carga al esperar la respuesta de la API
    def HiloEjecucion(self, event=""):
        self.t1=Hilo.Thread(target=self.operaciones)#Creamos el hilo en dicho metodo
        self.t1.start() #Inicializamos el hilo
    
    #Metodo para preparar el texto a imprimir
    def PrepararImpresion(self):
        cadena=""
        #Recorremos el diccionario y los escribimos en una cadena de texto
        for x in range(len(self.mensajes)):
            for clave, valor in self.mensajes[x].items():
                if valor=="user" or valor=="assistant":
                    if valor=="user":
                        cadena+="\n"+"USUARIO dice:"+"\n"
                    else:
                        cadena+="\nRobot(ROCKY) dice:\n"
                else:
                    cadena+="\n"+valor+"\n"
        return cadena

    #Metodo para imprimir
    def Imprimir(self):
        #Mostramos alerta de impresion
        respuesta=self.Alerta("¿Desea imprimir la conversación?")
        if respuesta==True:
            #Obtenemos la cadena formateada
            cadena=self.PrepararImpresion()
            #Obtenemos la impresora predeterminada del sistema
            self.impresora=win32print.GetDefaultPrinter()
            #Creamos un archivo temporal
            archivo=tempfile.NamedTemporaryFile(suffix=".txt", prefix="print", delete=False) #Poner el parametro "delete" para que no de errores de permisos de edicion
            #Abrimos el archivo y escribimos el contenido
            #La clausula "with" significa que tras ejecutarse se cerrara el archivo en cuestion
            with open(archivo.name, "w") as archivo_nombre:
                archivo_nombre.write(cadena)
            #Lanzamos el comando para imprimir
            win32api.ShellExecute(0, "print", archivo.name, None, ".", 0)
            mb.showinfo("Información","IMPRIMIENDO...")

    #Metodo para salir del programa
    def Salir(self):
        sys.exit(0)


#Bucle principal y llamada al programa
if __name__=="__main__":
    Aplicacion()
