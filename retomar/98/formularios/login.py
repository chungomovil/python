#Importamos modulos necesarios
import tkinter as tk
from tkinter import ttk
#Debemos importar los modulos con la ruta del modulo principal, ya que seran llamados desde ahi
import formularios.mensaje as mensaje


#Creamos la clase
class Login:

    #Creamos el metodo constructor
    def __init__(self):
        #Creamos la ventana en modo 'Toplevel' para que se abra en una ventana aislada al proceso de la ventana principal
        #Si lo hacemos de este modo los StringVar NO confundiran a tkinter (NO apareceran vacios) al ser llamados desde el modulo principal
        self.ventana=tk.Toplevel()
        self.ventana.title("Login")
        #Creamos el labelframe y los campos de formulario para login
        self.labelframe=ttk.Labelframe(self.ventana, text="Login")
        self.labelframe.grid(column=0, row=0, padx=10, pady=10)
        self.etiqueta1=ttk.Label(self.labelframe, text="Usuario:")
        self.etiqueta1.grid(column=0, row=0, padx=5, pady=10)
        self.dato1=tk.StringVar()
        self.entrada1=ttk.Entry(self.labelframe, width=25, textvariable=self.dato1)
        self.entrada1.grid(column=1, row=0, padx=5, pady=10)
        self.etiqueta2=ttk.Label(self.labelframe, text="Password:")
        self.etiqueta2.grid(column=0, row=1, padx=5, pady=10)
        self.dato2=tk.StringVar()
        self.entrada2=ttk.Entry(self.labelframe, width=25, textvariable=self.dato2, show="*")
        self.entrada2.grid(column=1, row=1, padx=5, pady=10)
        self.boton=ttk.Button(self.labelframe, text="Ingresar", command=self.Validar)
        self.boton.grid(column=1, row=2, padx=5, pady=10)
        self.ventana.geometry("300x200")
        self.ventana.resizable(False, False)
        self.ventana.mainloop()
    
    #Metodo para validar campos
    def Validar(self):
        #Capturar datos de los 'Entry'
        usuario=self.dato1.get().lower()
        password=self.dato2.get().lower()
        #Si el usuario y la clave son correctos se destruye la ventana
        if usuario=="paco" and password=="paco1234":
            self.ventana.destroy()
        #Si no muestra mensaje
        else:
            mensaje.MostrarError("Credenciales de acceso incorrectas.")

#Creamos la funcion para crear el objeto, recordar que debemos crearlo en una funcion para que no se lance automaticamente
def Mostrar():
    iniciar_login=Login()


