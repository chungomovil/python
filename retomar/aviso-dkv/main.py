import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

def AbrirNavegador():
    navegador_opciones=webdriver.ChromeOptions()
    navegador_opciones.add_argument("--user-data-dir=C:\\environments\\selenium")
    chromedriver=Service("C:\chromedriver\chromedriver.exe")
    navegador=webdriver.Chrome(service=chromedriver, options=navegador_opciones)
    return navegador

def Mensaje(navegador, telefonos):
    global notificados
    global no_notificados
    for telefono in telefonos:
        navegador.get(f"https://web.whatsapp.com/send?phone={telefono}&text=*EL MEDICO A TU LADO INFORMA:*%0AAl ser usted asegurado de *DKV* le comunicamos que a partir del 26 de junio será necesario que acuda al centro con su tarjeta sanitaria, debido a que el registro manual quedará deshabilitado.%0AReciba un cordial saludo y perdone las molestias.")
        try:
            boton_busqueda=WebDriverWait(navegador, timeout=20, poll_frequency=5).until(lambda valor: valor.find_elements(By.CLASS_NAME, "_3XKXx"))
            #boton_busqueda[0].click()
            time.sleep(5)
            notificados.append(telefono)
        except:
            no_notificados.append(telefono)
    print("NOTIFICADOS:")
    print(notificados)
    print("NO NOTIFICADOS:")
    print(no_notificados)
    navegador.quit()


def Ruta():
    ruta=os.path.dirname(__file__)+"/pacientes-dkv.csv"
    return ruta

notificados=[]
no_notificados=[]
archivo=open(Ruta())
telefonos=archivo.readlines()
archivo.close()
print(len(telefonos))
navegador=AbrirNavegador()
Mensaje(navegador, telefonos)
