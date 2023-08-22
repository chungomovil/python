#IMPORTAMOS LAS LIBRERIAS NECESARIAS
import os
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog as fd

class Aplicacion:

    #METODO CONSTRUCTOR
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("EXTRAER")
        self.estilos=ttk.Style()
        self.estilos.configure("mensaje.TLabel", font=("Arial 12 bold"), foreground="green")
        self.estilos.configure("aviso.TLabel", font=("Arial 12 bold"), foreground="orange")
        self.estilos.configure("error.TLabel", font=("Arial 12 bold"), foreground="red")
        self.frame=tk.LabelFrame(self.ventana, text="BACKUP")
        self.frame.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=20)
        self.opciones=tk.IntVar()
        self.opciones.set(1)
        self.radiobutton1=ttk.Radiobutton(self.frame, text="OFF", variable=self.opciones, value=0, cursor="hand2", command=self.EstadoCopia)
        self.radiobutton1.grid(column=1, row=0, pady=5, sticky="w")
        self.radiobutton2=ttk.Radiobutton(self.frame, text="ON", variable=self.opciones, value=1, cursor="hand2", command=self.EstadoCopia)
        self.radiobutton2.grid(column=1, row=0, padx=(80,0), pady=5, sticky="w")
        self.etiqueta1=ttk.Label(self.frame, text="Ruta")
        self.etiqueta1.grid(column=0, row=1, padx=5, pady=(5,20))
        self.campo1=ttk.Entry(self.frame, font=("Arial", 11))
        self.campo1.grid(column=1, row=1, padx=5, pady=(5,20), sticky="we")
        self.campo1.insert(0, "D:\\documentos\\diario")
        self.boton1=ttk.Button(self.frame, text="...", cursor="hand2", command=self.Buscador, width=3)
        self.boton1.grid(column=2, row=1, padx=(0,5), pady=(5,20))
        self.boton2=ttk.Button(self.ventana, text="EXTRAER", cursor="hand2", command=self.Iniciador)
        self.boton2.pack(side=tk.TOP, ipadx=5, ipady=5)
        self.lista_etiquetas=[] #CREAMOS UNA LISTA EN LA QUE SE IRAN AGREGANDO LAS ETIQUETAS DE MENSAJES
        self.frame.columnconfigure(1, weight=1)
        self.ventana.minsize(600,200)
        self.ventana.mainloop()
    
    def Iniciador(self):
        self.VaciarEstado()
        datos=self.ExtraerDatos()
        if datos!=1:
            total, fragmento=datos
            if len(total)>0: #DE ESTE MODO IMPEDIMOS QUE EL PROGRAMA SIGA SI EL DOCUMENTO PRINCIPAL ESTA VACIO
                self.CopiarDatos(fragmento)
                self.QuitarDatos(total, fragmento)
                if self.opciones.get()==1:
                    self.ExportarDocumento()
            else:
                mb.showinfo("Aviso","El documento principal no contiene datos.")
    
    #METODO PARA CONTROLAR ESTADO DE LA BARRA DE BUSQUEDA
    def EstadoCopia(self):
        if self.opciones.get()==0:
            self.campo1.config(state="disabled")
        else:
            if self.opciones.get()==1:
                self.campo1.config(state="normal")
    
    #METODO PARA ABRIR EL BUSCADOR DE ARCHIVOS
    def Buscador(self):
        carpeta=fd.askdirectory(initialdir="C:\\")#INICIAMOS EL BUSCADOR EN LA RAIZ DEL SISTEMA
        if carpeta!="":
            self.campo1.delete(0, tk.END)
            self.campo1.insert(0, carpeta)

    #METODO PARA ELIMINAR LOS MENSAJES DE ESTADO DE LA EJECUCION ANTERIOR
    def VaciarEstado(self):
        if len(self.lista_etiquetas)>0:
            for x in range(len(self.lista_etiquetas)):
                self.lista_etiquetas[x].destroy()

    #METODO PARA EXTRAER LOS DATOS DEL DOCUMENTO PRINCIPAL
    def ExtraerDatos(self):
        ruta=str(os.path.dirname(__file__))+"\\almacen.txt"
        excepcion=0
        try:
            archivo=open(ruta,"r+")
        except: 
            excepcion=1
            self.mensaje=ttk.Label(self.ventana, text="Lectura del documento principal: ERROR", style="error.TLabel")
            self.mensaje.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
            self.lista_etiquetas.append(self.mensaje)
        finally:
            if excepcion==0:
                lineas=archivo.readlines()
                extraer=[]
                contador=0
                pos=0
                while contador<10:
                    if pos>=len(lineas):
                        break
                    else:
                        linea_actual=lineas[pos]
                        extraer.append(lineas[pos])
                        if linea_actual.find("?")>0:
                            contador+=1
                    pos+=1
                archivo.close()
                self.mensaje=ttk.Label(self.ventana, text="Lectura del documento principal: OK", style="mensaje.TLabel")
                self.mensaje.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
                self.lista_etiquetas.append(self.mensaje)
                return (lineas, extraer)
            return(excepcion)

    #METODO PARA COPIAR LOS DATOS AL DOCUMENTO TEMPORAL
    def CopiarDatos(self, fragmento):
        ruta=str(os.path.dirname(__file__))+"\\extracto.txt"
        archivo=open(ruta,"w")
        archivo.writelines(fragmento)
        archivo.close()
        self.mensaje=ttk.Label(self.ventana, text="Copiado al documento de extracto: OK", style="mensaje.TLabel")
        self.mensaje.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.lista_etiquetas.append(self.mensaje)

    #METODO PARA QUITAR LOS DATOS DEL DOCUMENTO PRINCIPAL
    def QuitarDatos(self, total, fragmento):
        fecha=self.UltimaFecha(fragmento)
        fragmento_fin=len(fragmento)
        ruta=str(os.path.dirname(__file__))+"\\almacen.txt"
        archivo=open(ruta,"w")
        if (len(total)>fragmento_fin): #ASI EVITAMOS QUE INTENTE BUSCAR FUERA DEL INDICE (SOLO CUANDO QUEDAN MUY POCOS DATOS EN EL DOCUMENTO PRINCIPAL)
            if total[fragmento_fin].find("?")>0:
                archivo.write(fecha)
        archivo.writelines(total[fragmento_fin:])
        archivo.close()
        self.mensaje=ttk.Label(self.ventana, text="Modificar documento principal: OK", style="mensaje.TLabel")
        self.mensaje.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.lista_etiquetas.append(self.mensaje)

    #METODO PARA RESCATAR LA ULTIMA FECHA
    def UltimaFecha(self, fragmento):
        fecha=""
        for linea in fragmento:
            if linea.find("?")<0:
                fecha=linea
        return fecha

    #METODO PARA EXPORTAR LOCALMENTE EL DOCUMENTO PRINCIPAL
    def ExportarDocumento(self):
        ruta_origen=str(os.path.dirname(__file__))+"\\almacen.txt"
        carpeta_destino=str(self.campo1.get())
        ruta_destino=carpeta_destino+"\\almacen.txt"
        try:
            os.mkdir(carpeta_destino)
            self.mensaje=ttk.Label(self.ventana, text=f"Carpeta de backup creada en: {carpeta_destino}", style="aviso.TLabel")
            self.mensaje.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
            self.lista_etiquetas.append(self.mensaje)
        except OSError as error:
            if error.errno!=17:
                self.mensaje=ttk.Label(self.ventana, text=error, style="error.TLabel")
                self.mensaje.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
                self.lista_etiquetas.append(self.mensaje)
        shutil.copy(ruta_origen, ruta_destino)
        self.mensaje=ttk.Label(self.ventana, text=f"Backup realizado en: {ruta_destino}", style="aviso.TLabel")
        self.mensaje.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.lista_etiquetas.append(self.mensaje)


#BUCLE PRINCIPAL Y LLAMADA DEL PROGRAMA
if __name__=="__main__":
    iniciar=Aplicacion()
