import tkinter as tk
from tkinter import ttk

class Menu():

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("MENU SEMANAL")
        self.dias_semana=("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
        self.dias_contenido=[]
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
        self.ventana.minsize(800, 600)
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
            dias_encabezado=ttk.Label(frame2, text=self.dias_semana[x], anchor="center", font=("Arial", 16), borderwidth=1, relief="solid")
            dias_encabezado.grid(column=x, row=0, sticky="we")
            dias_contenido=ttk.Label(frame2, text="", font=("Arial", 14), borderwidth=1, relief="solid")
            dias_contenido.grid(column=x, row=3, sticky="we")
            self.dias_contenido.append(dias_contenido)
            frame2.columnconfigure(x, weight=1)
        boton_generar_nuevo=ttk.Button(frame3, text="Generar Nuevo", width=20)
        boton_generar_nuevo.grid(column=0, row=0, ipady=5)
            
    def ContenidoVentanaGestionMenu(self):
        frame1=ttk.Frame(self.frame_gestion_menu)
        frame1.grid(column=0, row=0, padx=20, pady=30)
        frame2=ttk.Frame(self.frame_gestion_menu, borderwidth=1, relief="groove")
        frame2.grid(column=1, row=0, padx=20, pady=30)
        barra_nav=ttk.Scrollbar(frame1, orient=tk.VERTICAL)
        self.listado_menu=tk.Listbox(frame1, width=40, height=30, yscrollcommand=barra_nav.set)
        barra_nav.config(command=self.listado_menu.yview)
        barra_nav.grid(column=1, row=0, sticky="ns")
        self.listado_menu.grid(column=0, row=0)
        titulo=ttk.Label(frame2, text="Gestionar Menú", font=("Arial", 16))
        titulo.grid(column=0, row=0, padx=20, pady=20, columnspan=2)
        self.entrada_dato=tk.StringVar()
        entrada_menu=ttk.Entry(frame2, width=30, font=("Arial", 12))
        entrada_menu.grid(column=0, row=1, padx=20, pady=20, ipady=5, columnspan=2)
        boton_guardar=ttk.Button(frame2, text="Guardar", width=20)
        boton_guardar.grid(column=0, row=2, padx=10, pady=(10, 20), ipady=5)
        boton_eliminar=ttk.Button(frame2, text="Eliminar", width=20)
        boton_eliminar.grid(column=1, row=2, padx=10, pady=(10, 20), ipady=5)






if __name__=="__main__":
    iniciar=Menu()



