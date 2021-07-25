import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st



class Calculadora():

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Calculadora de Estimaciones")
        self.listabotones=[]
        self.texto=""
        self.framesuperior=ttk.Frame(self.ventana, borderwidth="2", relief="groove")
        self.framesuperior.grid(column=0, row=0, columnspan=4, padx=40, pady=(40, 0), sticky="we")
        self.framesuperior.columnconfigure(0, weight=1)
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
        self.CrearBotonesDigitos()
        self.CrearBotonesFechas()
        self.CrearBotonesAcciones()
        self.CrearBotonesPorcentaje()
        self.CrearVisorSuperior()
        self.CrearVisorResultado()
        self.visorresultado.tag_config("encabezado", foreground="blue")
        self.encabezadoresultado=f"{'SOLO DIAS':<20}{'SOLO HORAS':<20}{'SOLO MINUTOS'}\n"
        self.visorresultado.delete("1.0", tk.END)
        self.visorresultado.insert(tk.END, self.encabezadoresultado, "encabezado")
        self.ventana.geometry("600x700")
        self.ventana.mainloop()

    def CrearBotonesDigitos(self):
        pos=9
        for x in range(3):
            for y in range (2, -1,-1):
                boton=ttk.Button(self.framebotonesdigitos, text=str(pos), command=lambda numero=pos: self.NumerosPulsados(numero))
                boton.grid(column=y, row=x, ipady=25)
                self.listabotones.append(boton)
                pos-=1
        boton=ttk.Button(self.framebotonesdigitos, text="0", command=lambda numero=pos: self.NumerosPulsados(numero))
        boton.grid(column=0, row=4, columnspan=3, ipady=25, sticky="we")
        self.listabotones.append(boton)

    def CrearBotonesFechas(self):
        encabezadofecha=ttk.Label(self.framebotonesfechas, text="FORMATO")
        encabezadofecha.grid(column=0, row=0, padx=10, pady=15)
        self.botondia=ttk.Button(self.framebotonesfechas, text="DIAS", command=lambda: self.FormatoPulsado("D"))
        self.botondia.grid(column=0, row=1, padx=10, pady=15, ipady=5)
        self.botonhora=ttk.Button(self.framebotonesfechas, text="HORAS", command=lambda: self.FormatoPulsado("H"))
        self.botonhora.grid(column=0, row=2, padx=10, pady=15, ipady=5)
        self.botonminuto=ttk.Button(self.framebotonesfechas, text="MINUTOS", command=lambda: self.FormatoPulsado("M"))
        self.botonminuto.grid(column=0, row=3, padx=10, pady=15, ipady=5)
    
    def CrearBotonesAcciones(self):
        self.botonsumar=ttk.Button(self.framebotonsumar, text="+", command=self.SumarPulsado)
        self.botonsumar.grid(column=0, row=0, sticky="ns")
        self.botonreset=ttk.Button(self.framebotonesacciones, text="C", command=self.Borrar)
        self.botonreset.grid(column=0, row=0, sticky="ns")
        self.botoncorregir=ttk.Button(self.framebotonesacciones, text="<", command=self.Retroceder)
        self.botoncorregir.grid(column=0, row=1, sticky="ns")
        self.botonresultado=ttk.Button(self.framebotonesacciones, text="=", command=self.MostrarResultado)
        self.botonresultado.grid(column=0, row=2, sticky="ns")

    def CrearBotonesPorcentaje(self):
        encabezado=ttk.Label(self.frameporcentaje, text="Gestion de Proyecto (%)", anchor="w")
        encabezado.grid(column=0, row=0, padx=10, pady=(5, 0), sticky="we")
        self.porcentaje=ttk.Spinbox(self.frameporcentaje, from_=0, to=20, state="readonly")
        self.porcentaje.set("10")
        self.porcentaje.grid(column=0, row=1, padx=10, pady=(0, 5))


    def CrearVisorSuperior(self):
        self.visorsuperior=ttk.Label(self.framesuperior, text="", background="white", anchor="e", font=("Arial", 12), wraplength=550)
        self.visorsuperior.grid(column=0, row=0, ipady=10, sticky="we")
    
    def CrearVisorResultado(self):
        titulo=ttk.Label(self.frameresultado, text="RESULTADO", anchor="center", font=("Arial", 18))
        titulo.grid(column=0, row=0, padx=20, pady=10, sticky="we")
        self.visorresultado=st.ScrolledText(self.frameresultado, width=58, height=10)
        self.visorresultado.grid(column=0, row=1, padx=20, pady=10)

    def NumerosPulsados(self, numero):
        self.visorsuperior.configure(text=self.RetornarTexto(numero))
        
    def FormatoPulsado(self, formato):
        self.visorsuperior.configure(text=self.RetornarTexto(formato))
    
    def SumarPulsado(self):
        self.visorsuperior.configure(text=self.RetornarTexto("+"))
    
    def Retroceder(self):
        self.texto=self.texto[:-1]
        self.visorsuperior.configure(text=self.RetornarTexto())

    def Borrar(self):
        self.texto=""
        self.visorsuperior.configure(text=self.texto, foreground="black")
        self.visorresultado.configure(state="normal")
        self.visorresultado.delete("1.0", tk.END)
        self.visorresultado.insert(tk.END, self.encabezadoresultado)
        self.BloquearTeclas("enabled")

    def SumarEnDias(self):
        suma_total=0
        suma=""
        for x in range(len(self.texto)):
            try:
                numero=int(self.texto[x])
                suma=suma+str(numero)
            except ValueError:
                if len(suma)>0:
                    suma=int(suma)
                    if self.texto[x]=="H":
                        suma=suma/8
                    elif self.texto[x]=="M":
                        suma=suma/480
                    suma_total=suma_total+suma
                    suma=""
        return round(suma_total, 1)
    
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

    def SumaInteligente(self, minutos):
        porcentaje=int(self.porcentaje.get())
        suma_total=minutos
        dias=suma_total//480
        suma_total=suma_total-(dias*480)
        horas=suma_total//60
        suma_total=suma_total-(horas*60)
        minutos=suma_total
        return (dias, horas, minutos)

    def MostrarResultado(self):
        if len(self.texto)>0:
            ultimo=len(self.texto)-1
            if ord(str(self.texto[ultimo]))==68 or ord(str(self.texto[ultimo]))==72 or ord(str(self.texto[ultimo]))==77:
                porcentaje=int(self.porcentaje.get())
                solodias=self.SumarEnDias()
                solohoras=self.SumarEnHoras()
                solominutos=self.SumarEnMinutos()
                porcentaje_final=(solominutos//100)*porcentaje
                porcentaje_programacion=solominutos-porcentaje_final
                dias, horas, minutos=self.SumaInteligente(solominutos)
                porcentaje_dias, porcentaje_horas, porcentaje_minutos=self.SumaInteligente(porcentaje_final)
                programacion_dias, programacion_horas, programacion_minutos=self.SumaInteligente(porcentaje_programacion)
                texto=f"{str(solodias)+' Dias':<20}{str(solohoras)+' Horas':<20}{str(solominutos)+' Minutos'}\n"
                encabezado_suma_inteligente=f"\n\n\nSUMA SIMPLIFICADA: "
                encabezado_porcentaje_inteligente=f"\nGESTION DE PROYECTO ({porcentaje}%): "
                encabezado_programacion_inteligente=f"\nPROGRAMACION: "
                texto_suma_inteligente=f"{dias} Dias, {horas} Horas y {minutos} Minutos"
                texto_porcentaje_inteligente=f"{porcentaje_dias} Dias, {porcentaje_horas} Horas y {porcentaje_minutos} Minutos"
                texto_programacion_inteligente=f"{programacion_dias} Dias, {programacion_horas} Horas y {programacion_minutos} Minutos"
                self.visorresultado.configure(state="normal")
                self.visorresultado.delete("1.0", tk.END)
                self.visorresultado.insert(tk.END, self.encabezadoresultado, "encabezado")
                self.visorresultado.insert(tk.END, texto)
                self.visorresultado.insert(tk.END, encabezado_suma_inteligente, "encabezado")
                self.visorresultado.insert(tk.END, texto_suma_inteligente)
                self.visorresultado.insert(tk.END, encabezado_porcentaje_inteligente, "encabezado")
                self.visorresultado.insert(tk.END, texto_porcentaje_inteligente)
                self.visorresultado.insert(tk.END, encabezado_programacion_inteligente, "encabezado")
                self.visorresultado.insert(tk.END, texto_programacion_inteligente)
                self.visorresultado.configure(state="disabled")
            else:
                self.texto="ERROR"
                self.visorsuperior.configure(text=self.texto, foreground="red")
                self.BloquearTeclas("disabled")

    def ControlTexto(self, caracter):
        caracter=str(caracter)
        if len(self.texto)>0:
            anterior=len(self.texto)-1
            if ord(str(self.texto[anterior]))>=48 and ord(str(self.texto[anterior]))<=57:
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

    def RetornarTexto(self, caracter=""):
        texto_convertido=""
        if caracter!="":
            if self.ControlTexto(caracter):
                self.texto+=str(caracter)
        for x in range(len(self.texto)):
            if self.texto[x]=="D":
                texto_convertido=texto_convertido+" Dias"
            elif self.texto[x]=="H":
                texto_convertido=texto_convertido+" Horas"
            elif self.texto[x]=="M":
                texto_convertido=texto_convertido+" Minutos"
            elif self.texto[x]=="+":
                texto_convertido=texto_convertido+" + "
            else:
                texto_convertido=texto_convertido+str(self.texto[x])
        return texto_convertido
    
    def BloquearTeclas(self, estado):
        for x in range(len(self.listabotones)):
            self.listabotones[x].configure(state=estado)
        self.botondia.configure(state=estado)
        self.botonhora.configure(state=estado)
        self.botonminuto.configure(state=estado)
        self.botonsumar.configure(state=estado)
        self.botoncorregir.configure(state=estado)
        self.botonresultado.configure(state=estado)



    """def CapturarDigitosPulsados(self, numero):
        condicion=False
        try:
            anterior=self.pulsados[len(self.pulsados)-1]
            if anterior!="D" and anterior!="H" and anterior!="M":
                condicion=True
            else:
                condicion=False
        except IndexError:
            condicion=True
        finally:
            if condicion==True:
                self.pulsados.append(numero)
                self.visorsuperior.configure(text=self.RetornarTexto())
                #print(self.pulsados)

    def EtiquetaFormato(self, etiqueta):
        anterior=self.pulsados[len(self.pulsados)-1]
        if anterior!="D" and anterior!="H" and anterior!="M" and anterior!="+":
            self.pulsados.append(etiqueta)
            self.visorsuperior.configure(text=self.RetornarTexto())
    
    def EtiquetaSuma(self):
        anterior=self.pulsados[len(self.pulsados)-1]
        if anterior=="D" or anterior=="H" or anterior=="M":
            self.pulsados.append("+")
            self.visorsuperior.configure(text=self.RetornarTexto())

    def SepararDias(self):
        pos_x=0
        print(self.pulsados)
        while pos_x<len(self.pulsados):
            if self.pulsados[pos_x]=="D" or self.pulsados[pos_x]=="H" or self.pulsados[pos_x]=="M":
                pos_y=pos_x-1
                etiqueta=self.pulsados[pos_x]
                while self.pulsados[pos_y]!="+":
                    if etiqueta=="D":
                        self.dias.append(self.pulsados[pos_y])
                    pos_y-=1
            pos_x+=1
        print(self.dias)"""

                



if __name__=="__main__":
    iniciar=Calculadora()




