from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import operaciones_db as operaciones
import notificacion_mail
import time

def CargarPacientes():
    listado_pacientes=operaciones.CumplenHoy()
    return listado_pacientes

def AbrirNavegador():
    #Para abrir el navegador firefox es distinto a chrome
    #Esta vez indicamos donde estan los datos del perfil del navegador
    navegador_opciones=webdriver.FirefoxProfile("/home/web/.mozilla/firefox/ww091my1.default-release")
    #Al ejecutarlo le pasamos los datos del perfil para que se ejecute con las cookies
    #Ademas necesitaremos el archivo que emula a firefox (geckodriver) que se deberá descargar
    navegador=webdriver.Firefox(firefox_profile=navegador_opciones)
    return navegador

#Funcion para escribir el mensaje y enviarlo
def EscribirMensaje(navegador, paciente):
    #Agregamos las variables globales para que no se creen exclusivas de la funcion
    global listado_existentes
    global listado_inexistentes
    global excepcion
    #Desempaquetamos la tupla de paciente
    nombre, apellido, telefono=paciente
    nombre_completo=nombre+" "+apellido
    #Buscamos la url con el mensaje, estilo php
    navegador.get(f"https://web.whatsapp.com/send?phone={telefono}&text=🥳 *¡FELICIDADES {nombre}!* 🥳%0ADesde el _'El Médico A Tu Lado'_ le deseamos un *FELIZ* día y mucha *SALUD*.%0AEstamos a su disposición.") #%0A es el salto de linea en ASCII
    #Algoritmo a intentar
    try:
        #Esperamos a que este disponible el boton de enviar el Whatsapp Web
        boton_busqueda=WebDriverWait(navegador, timeout=60, poll_frequency=5).until(lambda valor: valor.find_elements(By.CLASS_NAME, "_3XKXx"))
        #boton_busqueda[0].click()
        #Agregamos el nombre a la lista si se envió el mensaje
        listado_existentes.append(nombre_completo)
        #Lo dejamos unos segundos paralizado para que selenium no colapse al intentar cerrar la ventana tan rapido
        time.sleep(5)
    #Creamos la excepcion en caso de no encontar el boton de enviar mensaje
    except:
        #Creamos un filtro por si acaso sea que se caducó la sesión
        localizar_QR=navegador.find_elements(By.CLASS_NAME,"_19vUU")
        if len(localizar_QR)>0:
            excepcion="Sesión caducada."
        #Si no se caducó la sesión probablemente es que el contacto no exista en Whatsapp
        else:
            listado_inexistentes.append(nombre_completo)

#Funcion para cerrar el navegador
def CerrarNavegador(navegador):
    navegador.quit()

#LLamamos a la funcion para abrir el navegador
navegador=AbrirNavegador()
#Llamamos a la funcion que carga los pacientes de la DB
listado_pacientes=CargarPacientes()
#Creamos las listas de pacientes que se usaran luego
listado_existentes=[]
listado_inexistentes=[]
#Creamos la variable donde se almacenara la excepcion de sesion caducada
excepcion=""
#Creamos el bucle para recorrer a cada paciente
for paciente in listado_pacientes:
    #Llamamos a la funcion de escribir mensaje
    EscribirMensaje(navegador, paciente)
    #Si existe la excepcion de sesion caducada rompemos el bucle para no seguir buscando
    if excepcion!="":
        break

#Llamamos a la funcion del cierre del navegador
CerrarNavegador(navegador)
#Llamamos a la funcion de enviar mail y le pasamos los parametros
notificacion_mail.DatosMensaje(excepcion, listado_existentes, listado_inexistentes)
