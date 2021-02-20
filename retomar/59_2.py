"""
Ingresar el nombre de usuario y clave en controles de tipo Entry. Si se ingresa las cadena (usuario: juan, clave="abc123") luego mostrar en el título de la ventana el mensaje "Correcto" en caso contrario mostrar el mensaje "Incorrecto".
Para mostrar '*' cuando se ingresa la clave debemos pasar en el parámetro 'show' el caracter a mostrar:
"""

import tkinter as tk

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("LOGIN")
        self.etiqueta1=tk.Label(self.ventana, text="Usuario:")
        self.etiqueta1.grid(column=0, row=0)
        self.usuario=tk.StringVar()
        self.campo1=tk.Entry(self.ventana, width="20", textvariable=self.usuario)
        self.campo1.grid(column=0, row=1)
        self.etiqueta2=tk.Label(self.ventana, text="Password:")
        self.etiqueta2.grid(column=0, row=2)
        self.password=tk.StringVar()
        self.campo2=tk.Entry(self.ventana, width="20", textvariable=self.password, show="*")
        self.campo2.grid(column=0, row=3)
        self.boton1=tk.Button(self.ventana, text="Entrar", command=self.validar)
        self.boton1.grid(column=0, row=4)
        self.etiqueta3=tk.Label(self.ventana, foreground="red")
        self.etiqueta3.grid(column=0, row=5)
        self.ventana.minsize(300, 200)
        self.ventana.mainloop()
    
    #Recoge los datos introducidos y verifica si los datos son correctos, posteriormente se escribe en el label
    def validar(self):
        usuario=str(self.usuario.get()).lower()
        password=str(self.password.get()) #Por motivos de seguridad no tiene sentido pasar la password a lower
        if usuario=="juan" and password=="abc123":
            self.etiqueta3.configure(text="Credenciales validadas correctamente.")
        else:
            self.etiqueta3.configure(text="Credenciales erroneas.")
    
iniciar=Aplicacion()
