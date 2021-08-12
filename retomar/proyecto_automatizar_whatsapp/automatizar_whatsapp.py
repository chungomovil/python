#Importamos las librerias necesarias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException as Error
import operaciones_db as operaciones
import notificacion_mail
import time

#Funcion para retornar los pacientes de la base de datos
def CargarPacientes():
    listado_pacientes=operaciones.CumplenHoy()
    return listado_pacientes

#Funcion para abrir el navegador con la url de "WhatsApp Web"
def AbrirWhatsApp():
    #Abrimos el modulo de opciones del navegador
    navegador_opciones=Options()
    #Indicamos la ruta DESTINO de la carpeta donde se almacenarán la cookies de chrome
    navegador_opciones.add_argument("--user-data-dir=C:\\environments\\selenium")
    #Indicamos donde esta el ejecutable "chromedriver" (necesario descargarlos para emular la ejecucion de chrome con selenium) y le agregamos la carpeta de las cookies
    navegador=webdriver.Chrome("C:\chromedriver\chromedriver.exe", options=navegador_opciones)
    #Url que se instroducirá en el navegador
    navegador.get("https://web.whatsapp.com/")
    #Dejamos un margen de tiempo para que se ejecute la accion
    time.sleep(10)
    #Retornamos la sesión del navegador
    return navegador

#Funcion para borrar los campos
def BorrarCampos(navegador):
    #Buscamos los campos por su etiqueta
    campos=navegador.find_elements_by_class_name("_13NKt")
    #Borramos todos ellos
    for x in range(len(campos)):
        campos[x].clear()

#Funcion para buscar los contactos por su número de teléfono
def BuscarNumero(navegador, telefono):
    #Indicamos a python que se usará la variable global de excepcion (de lo contrario no sabrá si es local o global)
    global excepcion
    #Alboritmo a chequear
    try:
        #Almacenamos en una variable la etiqueta del campo para instroducir el número telefónico
        #"WebDriverWait" es una funcion de modulo webdriver que pausa la ejecución del programa hasta que no esté disponible el valor que se la ha pasado por la funcion "lambda"
        campo=WebDriverWait(navegador, timeout=120, poll_frequency=1).until(lambda valor: valor.find_elements_by_class_name("_13NKt")) #El atributo "timeout" indica el tiempo límite de la pausa, mientras que "pool_frequency"  es la frecuencia en segundos con la que buscará el valor
        #Escribimos el teléfono en el campo (recordar que al tener un atributo de clase y no id en HTML, pueden haber varios)
        campo[0].send_keys(telefono)
        #Tiempo que se pausará la ejecución (para dar margen a encontrar el teléfono)
        time.sleep(5)
        #Presionamos la tecla "ENTER"
        campo[0].send_keys(Keys.ENTER)
        #Verificamos que el contacto existe
        verificacion=navegador.find_elements_by_class_name("_1JFry")
        if len(verificacion)==0:
            return True
        else:
            return False
    #En caso de no haberse cargado la pagina
    except Error as mensaje:
        #Generamos el nombre de la excepcion y la guardamos en su variable correspondiente
        excepcion=str(type(mensaje).__name__)
        #Retornamos
        return "ERROR"

#Funcion para escribir el mensaje
def EscribirMensaje(navegador, paciente):
    #Buscamos el campo por su etiqueta
    campo=navegador.find_elements_by_class_name("_13NKt")
    #Creamos los mensajes OJO! Recordar que en chromedriver no se pueden poner emojis
    mensaje=f"*¡FELICIDADES {paciente}!*"
    campo[1].send_keys(mensaje)
    #Esta combinacion  de teclas (SHIFT Izq + ENTER) realiza un salto de línea en WhatsApp Web
    campo[1].send_keys(Keys.LEFT_SHIFT+Keys.ENTER)
    mensaje="Desde el _'El Médico A Tu Lado'_ le deseamos un *FELIZ* día y mucha *SALUD*."
    campo[1].send_keys(mensaje)
    campo[1].send_keys(Keys.LEFT_SHIFT+Keys.ENTER)
    mensaje="Estamos a su disposición."
    campo[1].send_keys(mensaje)
    campo[1].send_keys(Keys.ENTER)
    time.sleep(5)

#Funcion para cerrar el navegador
def CerrarNavegador(navegador):
    #Cerramos el navegador
    navegador.quit()
    #NOTA: Es mejor usar la funcion "quit()" que "close()", debido a que la primera elimina los archivos de datos temporales que se puedan haber creado.

#Almacenamos la lista de los pacientes
listado_pacientes=CargarPacientes()
#Creamos dos listas para saber a cuales se felicitaros y cuales no
listado_existentes=[]
listado_inexistentes=[]
#Variable donde se guardará una excepcion. (En caso de haberla)
excepcion=""
#Abrimos el navegador
navegador=AbrirWhatsApp()
#Bucle para cada paciente
for nombre, apellidos, numero in listado_pacientes:
    #Concatenamos el nombre completo
    paciente=nombre+" "+apellidos
    #Buscamos el numero y almacenamos la respuesta
    verificacion=BuscarNumero(navegador, numero)
    #Si no se genera excepcion
    if verificacion!="ERROR":
        #Si el numero existe
        if verificacion==True:
            #Lo agregamos a la lista de existentes
            listado_existentes.append(paciente)
            #Le enviamos el mensaje
#            EscribirMensaje(navegador, nombre)
        #Si no existe
        else:
            #Si retorna False
            if verificacion==False:
                #Lo agregamos a la lista de que no existe
                listado_inexistentes.append(paciente)
        #Borramos los campos para introducir nuevos datos
        BorrarCampos(navegador)
    #Si se genera excepción
    else:
        #Se corta el bucle y sigue el programa
        break

#Cerramos el navegador
CerrarNavegador(navegador)
#Llamamos al modulo que envia por email el resultado
notificacion_mail.EnviarEmail(excepcion, listado_existentes, listado_inexistentes)
