import pyperclip #SI SE PRODUCEN ERRORES --> sudo apt-get install xclip
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
    navegador_opciones=webdriver.FirefoxProfile("/home/web/.mozilla/firefox/ww091my1.default-release")
    #Al ejecutarlo le pasamos los datos del perfil para que se ejecute con las cookies
    #Ademas necesitaremos el archivo que emula a firefox (geckodriver) que se deberá descargar
    navegador=webdriver.Firefox(firefox_profile=navegador_opciones)
    navegador.get("https://web.whatsapp.com/")
    time.sleep(10)
    return navegador

def BorrarCampos(navegador):
    campos=navegador.find_elements(By.CLASS_NAME, "to2l77zo")
    for x in range(len(campos)):
        ActionChains(navegador).move_to_element(campos[x]).click(campos[x]).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()


def BuscarNumero(navegador, telefono, contador=0, sleep=0):
    global excepcion
    global busqueda
    try:
        boton_busqueda=WebDriverWait(navegador, timeout=20, poll_frequency=1).until(lambda valor: valor.find_elements(By.CLASS_NAME, "to2l77zo"))
        boton_busqueda[0].click()
        time.sleep(sleep)
        #Hacerlo con ActionChains, no esta funcionando bien el metodo directo de 'send_keys'
        campo=navegador.find_elements(By.CLASS_NAME, "to2l77zo")
        pyperclip.copy(telefono)
        ActionChains(navegador).move_to_element(campo[0]).click(campo[0]).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(20)
        ActionChains(navegador).move_to_element(campo[0]).click(campo[0]).send_keys(Keys.ENTER).perform()
        verificacion=navegador.find_elements(By.CLASS_NAME, "f8jlpxt4")
        if len(verificacion)==0:
            busqueda=True
        else:
            if contador==0:
                BorrarCampos(navegador)
                BuscarNumero(navegador, telefono, 1, 10)
    except Error as mensaje:
        excepcion=str(type(mensaje).__name__)

def EscribirMensaje(navegador, nombre):
    time.sleep(5)
    campo=navegador.find_elements(By.CLASS_NAME, "selectable-text")
    #Usamos el modulo pyperclip para enviar emojis (básicamente copia el texto en el portapapeles y lo envía), ya que dejó de funcionar el método anterior
    pyperclip.copy(f"🥳 *¡FELICIDADES {nombre}!* 🥳")
    #Empleamos el modulo 'ActionChains' para enviar mensajes
    #Los mensajes los enviamos de forma inversa ya que no empieza a escribir a partir del salto de línea, sino desde el primer espacion en blanco
    ActionChains(navegador).move_to_element(campo[-1]).click(campo[-1]).key_down(Keys.LEFT_SHIFT).key_down(Keys.ENTER).key_up(Keys.LEFT_SHIFT).key_up(Keys.ENTER).send_keys("Estamos a su disposición.").perform()
    ActionChains(navegador).move_to_element(campo[-1]).click(campo[-1]).key_down(Keys.LEFT_SHIFT).key_down(Keys.ENTER).key_up(Keys.LEFT_SHIFT).key_up(Keys.ENTER).send_keys("Desde el _'El Médico A Tu Lado'_ le deseamos un *FELIZ* día y mucha *SALUD*.").perform()
    ActionChains(navegador).move_to_element(campo[-1]).click(campo[-1]).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    ActionChains(navegador).move_to_element(campo[-1]).click(campo[-1]).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    #ANTIGUO METODO, SE DEJO DE USAR YA QUE NO PUDO ESCRIBIR EN EL CAMPO DEL MENSAJE EN NUEVAS VERSIONES DE WHATSAPP WEB EN LINUX (DE MOMENTO)
    """
    #Con geckodriver si se pueden poner emojis
    mensaje=f"🥳 *¡FELICIDADES {nombre}!* 🥳"
    campo[-1].send_keys(mensaje)
    campo[-1].send_keys(Keys.LEFT_SHIFT+Keys.ENTER)
    mensaje="Desde el _'El Médico A Tu Lado'_ le deseamos un *FELIZ* día y mucha *SALUD*."
    campo[-1].send_keys(mensaje)
    campo[-1].send_keys(Keys.LEFT_SHIFT+Keys.ENTER)
    mensaje="Estamos a su disposición."
    campo[-1].send_keys(mensaje)
    campo[-1].send_keys(Keys.ENTER)
    """
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
notificacion_mail.DatosMensaje(excepcion, listado_existentes, listado_inexistentes)
