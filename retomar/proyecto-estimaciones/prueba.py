import tkinter as tk
from tkinter import ttk

class prueba:
    
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("prueba")
        self.frame1=ttk.Frame(self.ventana, borderwidth="1", relief="groove")
        self.frame1.grid(column=0, row=0, sticky="we")
        self.etiqueta=ttk.Label(self.frame1, text="ESTO ES UNA PRUEBA DEL BOTON Y TAL TODO LARGO")
        self.etiqueta.grid(column=0, row=0, sticky="we")
        self.frame2=ttk.Frame(self.ventana, borderwidth="1", relief="groove")
        self.frame2.grid(column=0, row=1, sticky="we")
        self.boton=ttk.Button(self.frame2, text="prueba")
        self.boton.grid(column=0, row=0, sticky="we")
        #self.frame1.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(0, weight=1)
        self.ventana.geometry("400x500")
        self.ventana.mainloop()

iniciar=prueba()