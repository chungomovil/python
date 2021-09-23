from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException as Error
import operaciones_db as operaciones
import notificacion_mail
import time

def CargarPacientes():
    listado_pacientes=operaciones.CumplenHoy()
    return listado_pacientes

def AbrirWhatsApp():
    #Para abrir el navegador firefox es distinto a chrome
    #Esta vez indicamos donde estan los datos del perfil del navegador
    navegador_opciones=webdriver.FirefoxProfile("/home/web/.mozilla/firefox/u87cl4gq.default-1628594799771")
    #Al ejecutarlo le pasamos los datos del perfil para que se ejecute con las cookies
    #Ademas necesitaremos el archivo que emula a firefox (geckodriver) que se deberá descargar
    navegador=webdriver.Firefox(firefox_profile=navegador_opciones)
    navegador.get("https://web.whatsapp.com/")
    time.sleep(10)
    return navegador

def BorrarCampos(navegador):
    campos=navegador.find_elements_by_class_name("_13NKt")
    for x in range(len(campos)):
        campos[x].clear()

def BuscarNumero(navegador, telefono, contador=0, sleep=0):
    global excepcion
    global busqueda
    try:
        boton_busqueda=WebDriverWait(navegador, timeout=120, poll_frequency=1).until(lambda valor: valor.find_elements_by_class_name("_28-cz"))
        boton_busqueda[0].click()
        time.sleep(sleep)
        campo=navegador.find_elements_by_class_name("_13NKt")
        campo[0].send_keys(telefono)
        time.sleep(20)
        campo[0].send_keys(Keys.ENTER)
        verificacion=navegador.find_elements_by_class_name("_1JFry")
        if len(verificacion)==0:
            busqueda=True
        else:
            if contador==0:
                BuscarNumero(navegador, telefono, 1, 10)
    except Error as mensaje:
        excepcion=str(type(mensaje).__name__)

def EscribirMensaje(navegador, nombre):
    campo=navegador.find_elements_by_class_name("_13NKt")
    #Con geckodriver si se pueden poner emojis
    mensaje=f"🥳 *¡FELICIDADES {nombre}!* 🥳"
    campo[1].send_keys(mensaje)
    campo[1].send_keys(Keys.LEFT_SHIFT+Keys.ENTER)
    mensaje="Desde el _'El Médico A Tu Lado'_ le deseamos un *FELIZ* día y mucha *SALUD*."
    campo[1].send_keys(mensaje)
    campo[1].send_keys(Keys.LEFT_SHIFT+Keys.ENTER)
    mensaje="Estamos a su disposición."
    campo[1].send_keys(mensaje)
    campo[1].send_keys(Keys.ENTER)
    time.sleep(10)

def CerrarNavegador(navegador):
    navegador.quit()

listado_pacientes=CargarPacientes()
listado_existentes=[]
listado_inexistentes=[]
excepcion=""
navegador=AbrirWhatsApp()
for nombre, apellidos, numero in listado_pacientes:
    busqueda=False
    paciente=nombre+" "+apellidos
    BuscarNumero(navegador, numero)
    if excepcion=="":
        if busqueda==True:
            listado_existentes.append(paciente)
            EscribirMensaje(navegador, nombre)
        else:
            if busqueda==False:
                listado_inexistentes.append(paciente)
        BorrarCampos(navegador)
    else:
        break

CerrarNavegador(navegador)
notificacion_mail.EnviarEmail(excepcion, listado_existentes, listado_inexistentes)
