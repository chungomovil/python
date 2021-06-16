import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import operaciones

class Aplicacion:

    def __init__(self):
        self.conectar=operaciones.Operaciones()
        self.ventana=tk.Tk()
        self.ventana.title("AUTOMATIZAR CITAS")
        self.FormularioBD()
        self.FormularioEntrada()
        self.ventana.minsize(400, 600)
        self.ventana.mainloop()

    def FormularioBD(self):
        self.labelframe=ttk.Labelframe(self.ventana, text="Credenciales Base de Datos")
        self.labelframe.grid(column=0, row=0, padx=10, pady=10, sticky="w")
        self.titulo1=ttk.Label(self.labelframe, text="Usuario:")
        self.titulo1.grid(column=0, row=0, padx=5, pady=10)
        self.dato1=tk.StringVar()
        self.entrada1=ttk.Entry(self.labelframe, width=20, textvariable=self.dato1)
        self.entrada1.grid(column=1, row=0, padx=5, pady=10)
        self.titulo2=ttk.Label(self.labelframe, text="Clave:")
        self.titulo2.grid(column=0, row=1, padx=5, pady=10)
        self.dato2=tk.StringVar()
        self.entrada2=ttk.Entry(self.labelframe, width=20, textvariable=self.dato2, show="*")
        self.entrada2.grid(column=1, row=1, padx=5, pady=10)

    def FormularioEntrada(self):
        self.Encabezado=ttk.Label(self.ventana, text="AUTOMATIZAR CITAS", anchor="center", foreground="blue", font=("Arial", 20))
        self.Encabezado.grid(column=0, row=1, columnspan=2, padx=200, pady=50, sticky="nswe")
        self.titulo3=ttk.Label(self.ventana, text="Total Adeslas", anchor="center", font=("Arial", 12))
        self.titulo3.grid(column=0, row=2, padx=10, pady=10)
        self.dato3=ttk.Spinbox(self.ventana, from_=0, to=10, state="readonly")
        self.dato3.set(0)
        self.dato3.grid(column=0, row=3, padx=10, pady=10)
        self.titulo4=ttk.Label(self.ventana, text="Total DKV", anchor="center", font=("Arial", 12))
        self.titulo4.grid(column=1, row=2, padx=10, pady=10)
        self.dato4=ttk.Spinbox(self.ventana, from_=0, to=10, state="readonly")
        self.dato4.set(0)
        self.dato4.grid(column=1, row=3, padx=10, pady=10)
        self.confirmar2=ttk.Button(self.ventana, width=20, text="Confirmar", command=self.EnviarDatos)
        self.confirmar2.grid(column=0, row=4, columnspan=2, padx=10, pady=10)
        self.scrolledtext=st.ScrolledText(self.ventana, width=80, height=20)
        self.scrolledtext.grid(column=0, row=5, columnspan=2, padx=10, pady=10)
    
    def ValidarCredenciales(self):
        usuario=self.dato1.get()
        clave=self.dato2.get()
        if usuario=="" or clave=="":
            mb.showerror("ERROR", "Usuario o clave vacio.")
        return (usuario, clave)


    def EnviarDatos(self):
        usuario, clave=self.ValidarCredenciales()
        accesoDB=self.conectar.AbrirConexion(usuario, clave)
        if accesoDB==False:
            mb.showerror("ERROR","Usuario o clave incorrectos.")
        else:
            peticion_adeslas=int(self.dato3.get())
            peticion_dkv=int(self.dato4.get())
            listado=self.conectar.FiltrarSeguro(peticion_adeslas, peticion_dkv, usuario, clave)
            if listado==False:
                mb.showwarning("VALOR INCORRECTO","Algun valor supera la cantidad de pacientes disponibles.")
            else:
                respuesta=mb.askyesno("Informacion",f"Se va a proceder a insertar {len(listado[0])+len(listado[1])} citas.")
                if respuesta==True:
                    self.conectar.Insertar(listado, usuario, clave)
                    self.MostrarInserciones(listado)

    def MostrarInserciones(self, listado):
        self.scrolledtext.delete(1.0, tk.END)
        encabezado=f"{'NUMERO':<10}{'NOMBRE':<50}{'SEGURO':<10}{'CONSULTAS':<10}"
        self.scrolledtext.insert(tk.END, encabezado)
        num=0
        for x in range(len(listado)):
            for y in range(len(listado[x])):
                num+=1
                nombre=listado[x][y][2]
                apellido=str(listado[x][y][3])
                nombre_completo=str(nombre)+" "+str(apellido)
                seguro=str(listado[x][y][4])
                consultas=str(listado[x][y][10])
                fila=f"{num:<10}{nombre_completo:<50}{seguro:<10}{consultas:<10}"
                self.scrolledtext.insert(tk.END, fila)


    
    
iniciar=Aplicacion()