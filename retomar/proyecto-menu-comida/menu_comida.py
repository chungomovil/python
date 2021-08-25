import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import operaciones_db as database
from datetime import datetime
import random
import time

class Menu():

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("MENU SEMANAL")
        self.dias_semana=("lunes", "martes", "miércoles", "jueves", "viernes")
        self.dias_contenido=[]
        self.listado_completo=[]
        self.listado_plato_principal=[]
        self.listado_acompanamiento=[]
        self.listado_ensalada=[]
        self.nombre_antiguo=""
        self.hoy=datetime.now()
        self.hoy=datetime.strftime(self.hoy, "%d-%m-%Y")
        self.secciones=ttk.Notebook(self.ventana)
        self.secciones.grid(column=0, row=0, sticky="nswe")
        self.frame_ventana_principal=ttk.Frame(self.secciones)
        self.frame_gestion_menu=ttk.Frame(self.secciones)
        self.secciones.add(self.frame_ventana_principal, text="Principal")
        self.secciones.add(self.frame_gestion_menu, text="Agregar Menu")
        self.frame_ventana_principal.columnconfigure(0, weight=1)
        self.frame_gestion_menu.columnconfigure(1, weight=1)
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        self.ContenidoVentanaPrincipal()
        self.ContenidoVentanaGestionMenu()
        self.ActualizarListado()
        self.MostrarMenuDia()
        self.listado_menu.bind("<ButtonRelease-1>", self.SeleccionCursor)
        self.ventana.minsize(1000, 600)
        self.ventana.mainloop()
    
    def ContenidoVentanaPrincipal(self):
        frame1=ttk.Frame(self.frame_ventana_principal)
        frame1.grid(column=0, row=1, padx=20, pady=(20, 60))
        frame2=ttk.Frame(self.frame_ventana_principal)
        frame2.grid(column=0, row=2, padx=20, sticky="we")
        frame3=ttk.Frame(self.frame_ventana_principal)
        frame3.grid(column=0, row=3, padx=20, pady=(60, 20))
        titulo=ttk.Label(frame1, text="MENÚ SEMANAL", anchor="center", font=("Arial", 20), foreground="blue")
        titulo.grid(column=0, row=0, columnspan=2, pady=20, sticky="we")
        boton_anterior=ttk.Button(frame1, text="Anterior", width=20)
        boton_anterior.grid(column=0, row=1, padx=5, ipady=5)
        boton_actual=ttk.Button(frame1, text="Actual", width=20)
        boton_actual.grid(column=1, row=1, padx=5, ipady=5)
        for x in range(len(self.dias_semana)):
            dias_encabezado=ttk.Label(frame2, text=self.dias_semana[x].capitalize(), anchor="center", font=("Arial", 16), borderwidth=1, relief="solid", background="#5DADE2")
            dias_encabezado.grid(column=x, row=0, sticky="we")
            dias_contenido=ttk.Label(frame2, text="", anchor="n", font=("Arial", 12), borderwidth=1, relief="solid", background="#D6EAF8")
            dias_contenido.grid(column=x, row=3, ipadx=5, sticky="nswe")
            self.dias_contenido.append(dias_contenido)
            frame2.columnconfigure(x, weight=1)
        self.boton_generar_nuevo=ttk.Button(frame3, text="Generar Nuevo", width=20, command=self.SeleccionarMenuDia)
        self.boton_generar_nuevo.grid(column=0, row=0, padx=5, ipady=5)
        self.boton_refrescar=ttk.Button(frame3, text="Refrescar", width=20, command=self.MostrarMenuDia)
        self.boton_refrescar.grid(column=1, row=0, padx=5, ipady=5)
            
    def ContenidoVentanaGestionMenu(self):
        frame1=ttk.Frame(self.frame_gestion_menu)
        frame1.grid(column=0, row=0, padx=20, pady=30, rowspan=2)
        frame2=ttk.Frame(self.frame_gestion_menu, borderwidth=1, relief="groove")
        frame2.grid(column=1, row=0, padx=20, pady=10, sticky="swe")
        frame3=ttk.Frame(self.frame_gestion_menu, borderwidth=1, relief="groove")
        frame3.grid(column=1, row=1, padx=20, pady=10, sticky="nwe")
        for x in range(4):
            frame2.columnconfigure(x, weight=1)
            frame3.columnconfigure(x, weight=1)
        
        #<-----SECCION TABLA PRODUCTOS----->
        titulo_frame1=ttk.Label(frame1, text="Listado de Menús", font=("Arial", 16))
        titulo_frame1.grid(column=0, row=0, pady=(0, 10))
        barra_nav=ttk.Scrollbar(frame1, orient=tk.VERTICAL)
        self.listado_menu=tk.Listbox(frame1, width=35, height=30, yscrollcommand=barra_nav.set, font=("Arial", 13), selectbackground="#82E0AA", selectforeground="black")
        barra_nav.config(command=self.listado_menu.yview)
        barra_nav.grid(column=1, row=1, sticky="ns")
        self.listado_menu.grid(column=0, row=1)
        
        #<-----SECCION DE CREACION----->
        titulo_frame2=ttk.Label(frame2, text="Nuevo Menú", font=("Arial", 16), foreground="blue")
        titulo_frame2.grid(column=0, row=0, padx=20, pady=(10, 0), columnspan=4)
        subtitulo1_frame2=ttk.Label(frame2, text="Categoría:", font=("Arial", 13, "underline"))
        subtitulo1_frame2.grid(column=0, row=1, padx=5, pady=5, columnspan=2)
        subtitulo2_frame2=ttk.Label(frame2, text="Admite:", font=("Arial", 13, "underline"))
        subtitulo2_frame2.grid(column=2, row=1, padx=5, pady=5, columnspan=2)
        self.creacion_categoria_dato=tk.StringVar()
        categoria_plato_principal_entrada=ttk.Radiobutton(frame2, variable=self.creacion_categoria_dato, value="Principal", command=lambda: self.VerificacionCreacionCategoria("Principal"))
        categoria_plato_principal_entrada.grid(column=0, row=2, pady=5, sticky="e")
        categoria_plato_principal_etiqueta=ttk.Label(frame2, text="Plato principal", font=("Arial", 10))
        categoria_plato_principal_etiqueta.grid(column=1, row=2, pady=5, sticky="w")
        categoria_acompanamiento_entrada=ttk.Radiobutton(frame2, variable=self.creacion_categoria_dato, value="Acompanamiento", command=lambda: self.VerificacionCreacionCategoria("Acompanamiento"))
        categoria_acompanamiento_entrada.grid(column=0, row=3, pady=5, sticky="e")
        categoria_acompanamiento_etiqueta=ttk.Label(frame2, text="Acompañamiento", font=("Arial", 10))
        categoria_acompanamiento_etiqueta.grid(column=1, row=3, pady=5, sticky="w")
        categoria_creacion_ensalada_entrada=ttk.Radiobutton(frame2, variable=self.creacion_categoria_dato, value="Ensalada", command=lambda: self.VerificacionCreacionCategoria("Ensalada"))
        categoria_creacion_ensalada_entrada.grid(column=0, row=4, pady=5, sticky="e")
        categoria_creacion_ensalada_etiqueta=ttk.Label(frame2, text="Ensalada", font=("Arial", 10))
        categoria_creacion_ensalada_etiqueta.grid(column=1, row=4, pady=5, sticky="w")
        self.creacion_admision_acompanamiento_dato=tk.StringVar()
        self.admision_acompanamiento_entrada1=ttk.Checkbutton(frame2, variable=self.creacion_admision_acompanamiento_dato, onvalue="Si", offvalue="No")
        self.admision_acompanamiento_entrada1.grid(column=2, row=2, pady=5, sticky="e")
        admision_acompanamiento_etiqueta=ttk.Label(frame2, text="Acompañamiento", font=("Arial", 10))
        admision_acompanamiento_etiqueta.grid(column=3, row=2, pady=5, sticky="w")
        self.creacion_admision_ensalada_dato=tk.StringVar()
        self.admision_ensalada_entrada1=ttk.Checkbutton(frame2, variable=self.creacion_admision_ensalada_dato, onvalue="Si", offvalue="No")
        self.admision_ensalada_entrada1.grid(column=2, row=3, pady=2, sticky="e")
        admision_ensalada_etiqueta=ttk.Label(frame2, text="Ensalada", font=("Arial", 10))
        admision_ensalada_etiqueta.grid(column=3, row=3, pady=2, sticky="w")
        self.creacion_nombre_dato=tk.StringVar()
        creacion_nombre_entrada=ttk.Entry(frame2, width=40, font=("Arial", 12), textvariable=self.creacion_nombre_dato)
        creacion_nombre_entrada.grid(column=0, row=5, padx=20, pady=10, ipady=5, columnspan=4)
        boton_guardar=ttk.Button(frame2, text="Crear Nuevo", width=20, command=self.AgregarMenu)
        boton_guardar.grid(column=0, row=6, padx=10, pady=(10, 20), ipady=5, columnspan=4)
        self.creacion_categoria_dato.set("Principal")
        self.creacion_admision_acompanamiento_dato.set("No")
        self.creacion_admision_ensalada_dato.set("No")

        #<-----SECCION DE MODIFICACION----->
        titulo_frame3=ttk.Label(frame3, text="Gestionar Menú", font=("Arial", 16), foreground="blue")
        titulo_frame3.grid(column=0, row=0, padx=20, pady=(10, 0), columnspan=4)
        subtitulo1_frame2=ttk.Label(frame3, text="Categoría:", font=("Arial", 13, "underline"))
        subtitulo1_frame2.grid(column=0, row=1, padx=5, pady=5, columnspan=2)
        subtitulo2_frame2=ttk.Label(frame3, text="Admite:", font=("Arial", 13, "underline"))
        subtitulo2_frame2.grid(column=2, row=1, padx=5, pady=5, columnspan=2)
        self.mod_categoria_dato=tk.StringVar()
        categoria_plato_principal_entrada=ttk.Radiobutton(frame3, variable=self.mod_categoria_dato, value="Principal", command=lambda: self.VerificacionModificacionCategoria("Principal"))
        categoria_plato_principal_entrada.grid(column=0, row=2, pady=5, sticky="e")
        categoria_plato_principal_etiqueta=ttk.Label(frame3, text="Plato principal", font=("Arial", 10))
        categoria_plato_principal_etiqueta.grid(column=1, row=2, pady=5, sticky="w")
        categoria_acompanamiento_entrada=ttk.Radiobutton(frame3, variable=self.mod_categoria_dato, value="Acompanamiento", command=lambda: self.VerificacionModificacionCategoria("Acompanamiento"))
        categoria_acompanamiento_entrada.grid(column=0, row=3, pady=5, sticky="e")
        categoria_acompanamiento_etiqueta=ttk.Label(frame3, text="Acompañamiento", font=("Arial", 10))
        categoria_acompanamiento_etiqueta.grid(column=1, row=3, pady=5, sticky="w")
        categoria_ensalada_entrada=ttk.Radiobutton(frame3, variable=self.mod_categoria_dato, value="Ensalada", command=lambda: self.VerificacionModificacionCategoria("Ensalada"))
        categoria_ensalada_entrada.grid(column=0, row=4, pady=5, sticky="e")
        categoria_ensalada_etiqueta=ttk.Label(frame3, text="Ensalada", font=("Arial", 10))
        categoria_ensalada_etiqueta.grid(column=1, row=4, pady=5, sticky="w")
        self.mod_admision_acompanamiento_dato=tk.StringVar()
        self.admision_acompanamiento_entrada2=ttk.Checkbutton(frame3, variable=self.mod_admision_acompanamiento_dato, onvalue="Si", offvalue="No")
        self.admision_acompanamiento_entrada2.grid(column=2, row=2, pady=5, sticky="e")
        admision_acompanamiento_etiqueta=ttk.Label(frame3, text="Acompañamiento", font=("Arial", 10))
        admision_acompanamiento_etiqueta.grid(column=3, row=2, pady=5, sticky="w")
        self.mod_admision_ensalada_dato=tk.StringVar()
        self.admision_ensalada_entrada2=ttk.Checkbutton(frame3, variable=self.mod_admision_ensalada_dato, onvalue="Si", offvalue="No")
        self.admision_ensalada_entrada2.grid(column=2, row=3, pady=2, sticky="e")
        admision_ensalada_etiqueta=ttk.Label(frame3, text="Ensalada", font=("Arial", 10))
        admision_ensalada_etiqueta.grid(column=3, row=3, pady=2, sticky="w")
        self.mod_nombre_dato=tk.StringVar()
        nombre_dato_entrada=ttk.Entry(frame3, width=40, font=("Arial", 12), textvariable=self.mod_nombre_dato)
        nombre_dato_entrada.grid(column=0, row=5, padx=20, pady=10, ipady=5, columnspan=4)
        self.boton_buscar=ttk.Button(frame3, text="Buscar", width=20, command=lambda: self.MostrarDatos(self.mod_nombre_dato.get()))
        self.boton_buscar.grid(column=0, row=6, padx=5, pady=10, ipady=5, columnspan=4)
        self.boton_modificar=ttk.Button(frame3, text="Modificar", width=20, state="disabled", command=lambda: self.ModificarMenu(self.mod_nombre_dato.get()))
        self.boton_modificar.grid(column=0, row=7, padx=5, pady=(0, 20), ipady=5, columnspan=2, sticky="e")
        self.boton_eliminar=ttk.Button(frame3, text="Eliminar", width=20, state="disabled", command=self.BorrarMenu)
        self.boton_eliminar.grid(column=2, row=7, padx=5, pady=(0, 20), ipady=5, columnspan=2, sticky="w")
        self.mod_admision_acompanamiento_dato.set("No")
        self.mod_admision_ensalada_dato.set("No")

#<-----METODOS DE LA VENTANA DE GESTION----->
    def AgregarMenu(self):
        menu=self.creacion_nombre_dato.get().lower()
        categoria=self.creacion_categoria_dato.get()
        acompanamiento=self.creacion_admision_acompanamiento_dato.get()
        ensalada=self.creacion_admision_ensalada_dato.get()
        repetido=self.Repetido(menu)
        if repetido==0:
            database.AgregarMenu(menu, categoria, acompanamiento, ensalada)
            mb.showinfo("INFORMACIÓN", "Menú creado.")
            self.creacion_nombre_dato.set("")
            self.creacion_categoria_dato.set("Principal")
            self.creacion_admision_acompanamiento_dato.set("No")
            self.creacion_admision_ensalada_dato.set("No")
            self.VerificacionCreacionCategoria(self.creacion_categoria_dato.get())
        else:
            mb.showerror("ERROR", "El artículo ya existe.")
        self.ActualizarListado()
    
    def ActualizarListado(self):
        self.listado_completo=database.BuscarTodos()
        self.SepararTipos()
        self.listado_menu.delete(0, tk.END)
        pos=0
        color=""
        for idmenu, plato, categoria, acompanamiento, ensalada in self.listado_completo:
            if pos%2:
                color="white"
            else:
                color="#D6EAF8"
            fila=plato
            self.listado_menu.insert(tk.END, fila)
            self.listado_menu.itemconfigure(pos, background=color)
            pos+=1
    
    def BorrarMenu(self):
        menu=self.mod_nombre_dato.get()
        datos=self.BuscarMenu(menu)
        if type(datos) is tuple:
            respuesta=mb.askyesno("AVISO", "¿Desea eliminar este menú?")
            if respuesta:
                database.BorrarMenu(menu)
                self.mod_nombre_dato.set("")
                self.mod_categoria_dato.set("")
                self.mod_admision_acompanamiento_dato.set("No")
                self.mod_admision_ensalada_dato.set("No")
        else:
            mb.showerror("ERROR", "El menu no existe.")
        self.ActualizarListado()
        self.MostrarMenuDia()

    def SeleccionCursor(self, evento):
        if len(self.listado_menu.curselection())>0:
            menu=self.listado_menu.get(self.listado_menu.curselection()[0])
            self.nombre_antiguo=menu
            self.MostrarDatos(menu)

    def ModificarMenu(self, menu):
        if menu!="":
            datos=self.BuscarMenu(self.nombre_antiguo)
            idmenu, plato, categoria, acompanamiento, ensalada=datos
            menu_antiguo=plato
            menu_nuevo=menu
            repetido=self.Repetido(menu_nuevo)
            verificar=False
            if menu_nuevo==menu_antiguo:
                verificar=True
            else:
                if repetido<1:
                    verificar=True
            if verificar:
                database.ModificarMenu(menu_nuevo, self.mod_categoria_dato.get(), self.mod_admision_acompanamiento_dato.get(), self.mod_admision_ensalada_dato.get(), menu_antiguo)
                self.nombre_antiguo=menu_nuevo
            else:
                mb.showerror("ERROR", "El artículo ya existe")
            self.ActualizarListado()
            self.MostrarMenuDia()

    def BuscarMenu(self, menu):
        datos=database.BuscarIndividual(menu)
        return datos

    def MostrarDatos(self, menu):
        menu=menu.lower()
        datos=self.BuscarMenu(menu)
        if type(datos) is tuple:
            idmenu, plato, categoria, acompanamiento, ensalada=datos
            self.mod_nombre_dato.set(plato)
            self.mod_categoria_dato.set(categoria)
            self.mod_admision_acompanamiento_dato.set(acompanamiento)
            self.mod_admision_ensalada_dato.set(ensalada)
            self.boton_modificar.configure(state="enabled")
            self.boton_eliminar.configure(state="enabled")
            self.nombre_antiguo=plato
        else:
            self.mod_categoria_dato.set("")
            self.mod_admision_acompanamiento_dato.set("No")
            self.mod_admision_ensalada_dato.set("No")
            self.boton_modificar.configure(state="disabled")
            self.boton_eliminar.configure(state="disabled")
            if datos==None:
                mb.showerror("ERROR", "El menú no existe.")
        self.VerificacionModificacionCategoria(categoria)

    def VerificacionCreacionCategoria(self, categoria):
        if categoria=="Principal":
            self.admision_acompanamiento_entrada1.configure(state="enabled")
            self.admision_ensalada_entrada1.configure(state="enabled")
        else:
            self.creacion_admision_acompanamiento_dato.set("No")
            self.creacion_admision_ensalada_dato.set("No")
            self.admision_acompanamiento_entrada1.configure(state="disabled")
            self.admision_ensalada_entrada1.configure(state="disabled")

    def VerificacionModificacionCategoria(self, categoria):
        if categoria=="Principal":
            self.admision_acompanamiento_entrada2.configure(state="enabled")
            self.admision_ensalada_entrada2.configure(state="enabled")
        else:
            self.mod_admision_acompanamiento_dato.set("No")
            self.mod_admision_ensalada_dato.set("No")
            self.admision_acompanamiento_entrada2.configure(state="disabled")
            self.admision_ensalada_entrada2.configure(state="disabled")

    def Repetido(self, menu):
        similitud=0
        for x in range(len(self.listado_completo)):
            for i in range(len(self.listado_completo[x])):
                if menu==self.listado_completo[x][i]:
                    similitud+=1
        return similitud

#<-----METODOS DE LA VENTANA PRINCIPAL----->
    def SepararTipos(self):
        self.listado_plato_principal=[]
        self.listado_acompanamiento=[]
        self.listado_ensalada=[]
        for x in range(len(self.listado_completo)):
            if self.listado_completo[x][2]=="Principal":
                self.listado_plato_principal.append(self.listado_completo[x])
            elif self.listado_completo[x][2]=="Acompanamiento":
                self.listado_acompanamiento.append(self.listado_completo[x])
            elif self.listado_completo[x][2]=="Ensalada":
                self.listado_ensalada.append(self.listado_completo[x])
    
    def SeleccionarMenuDia(self):
        listado_recientes, listado_antiguos=database.ListaMenuDia()
        print(listado_recientes)
        if len(listado_recientes)>0 and len(listado_antiguos)>0:
            if listado_recientes[0][4]==self.hoy:
                database.BorrarMenuDia(self.hoy)
        platos_disponibles=self.listado_plato_principal
        for x in range(5):
            eleccion_plato=random.randint(0, len(platos_disponibles)-1)
            eleccion_acompanamiento=random.randint(0, len(self.listado_acompanamiento)-1)
            eleccion_ensalada=random.randint(0, len(self.listado_ensalada)-1)
            database.AgregarMenuDia(platos_disponibles[eleccion_plato][0], platos_disponibles[eleccion_plato][1], self.dias_semana[x], self.hoy)
            if self.listado_plato_principal[eleccion_plato][3]=="Si" and self.listado_plato_principal[eleccion_plato][4]=="Si":
                database.AgregarMenuDia(self.listado_acompanamiento[eleccion_acompanamiento][0], self.listado_acompanamiento[eleccion_acompanamiento][1], self.dias_semana[x], self.hoy)
                database.AgregarMenuDia(self.listado_ensalada[eleccion_ensalada][0], self.listado_ensalada[eleccion_ensalada][1], self.dias_semana[x], self.hoy)
            elif self.listado_plato_principal[eleccion_plato][3]=="Si":
                database.AgregarMenuDia(self.listado_acompanamiento[eleccion_acompanamiento][0], self.listado_acompanamiento[eleccion_acompanamiento][1], self.dias_semana[x], self.hoy)
            elif self.listado_plato_principal[eleccion_plato][4]=="Si":
                database.AgregarMenuDia(self.listado_ensalada[eleccion_ensalada][0], self.listado_ensalada[eleccion_ensalada][1], self.dias_semana[x], self.hoy)
            del platos_disponibles[eleccion_plato]
        self.MostrarMenuDia()
        self.boton_generar_nuevo.configure(state="disabled")
        self.boton_refrescar.configure(state="disabled")
        self.ventana.update()
        self.ventana.after(2000, self.DesactivarBoton)
    
    #CAMBIAR LA FORMA DE LA BD PARA QUE MUESTRE EL PRODUCTO ACTUALIZADO (EMPLEAR LA CLAVE FORANEA)
    def MostrarMenuDia(self):
        listado_recientes, listado_antiguos=database.ListaMenuDia()
        for x in range(len(self.dias_contenido)):
            cadena_completa="\n"
            for i in range(len(listado_recientes)):
                if listado_recientes[i][3]==self.dias_semana[x]:
                    plato=""
                    for k in range(len(self.listado_completo)):
                        if listado_recientes[i][1]==self.listado_completo[k][0]:
                            plato=self.listado_completo[k][1]
                    #cadena=cadena+" > "+listado_recientes[i][2]+"\n\n"
                    cadena_completa=cadena_completa+self.FormateoCadena(str("> "+plato))+"\n\n"
            self.dias_contenido[x].configure(text=cadena_completa)
        self.boton_generar_nuevo.configure(state="disabled")
        self.boton_refrescar.configure(state="disabled")
        self.ventana.update()
        self.ventana.after(2000, self.DesactivarBoton)
    
    def FormateoCadena(self, cadena):
        longitud=15
        if len(cadena)>longitud:
            capturar_espacio=0
            pos=longitud
            nuevacadena=""
            while capturar_espacio!=-1:               
                capturar_espacio=cadena[pos:].find(" ")
                if capturar_espacio!=-1:
                    nuevacadena=nuevacadena+cadena[pos-longitud:pos+capturar_espacio]+"\n  "
                else:
                    nuevacadena=nuevacadena+cadena[pos-longitud:]
                pos=pos+longitud+capturar_espacio
            return nuevacadena
        else:
            return cadena

    def DesactivarBoton(self):
        self.boton_generar_nuevo.configure(state="enabled")
        self.boton_refrescar.configure(state="enabled")






if __name__=="__main__":
    iniciar=Menu()



