#Importamos las librerias necesarias
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
    navegador_opciones=webdriver.ChromeOptions()
    #Indicamos la ruta DESTINO de la carpeta donde se almacenarán la cookies de chrome
    navegador_opciones.add_argument("--user-data-dir=C:\\environments\\selenium")
    #Indicamos la ruta de chromedriver
    chromedriver=Service("C:\chromedriver\chromedriver.exe")
    #Indicamos donde esta el ejecutable "chromedriver" (necesario descargarlos para emular la ejecucion de chrome con selenium) y le agregamos la carpeta de las cookies
    navegador=webdriver.Chrome(service=chromedriver, options=navegador_opciones)
    #Url que se instroducirá en el navegador
    navegador.get("https://web.whatsapp.com")
    #Dejamos un margen de tiempo para que se ejecute la accion
    time.sleep(10)
    #Retornamos la sesión del navegador
    return navegador

#Funcion para borrar los campos
def BorrarCampos(navegador):
    #Buscamos los campos por su etiqueta
    campos=navegador.find_elements(By.CLASS_NAME, "Er7QU")
    #Borramos todos ellos
    for x in range(len(campos)):
        campos[x].clear()

#Funcion recursiva para buscar los contactos por su número de teléfono
def BuscarNumero(navegador, telefono, contador=0, sleep=0):
    #Indicamos a python que se usará las variables globales de excepcion y busqueda (de lo contrario no sabrá si es local o global)
    global excepcion
    global busqueda
    #Alboritmo a chequear
    try:
        #Almacenamos el boton de búsqueda en una variable
        #"WebDriverWait" es una funcion de modulo webdriver que pausa la ejecución del programa hasta que no esté disponible el valor que se la ha pasado por la funcion "lambda"
        boton_busqueda=WebDriverWait(navegador, timeout=120, poll_frequency=1).until(lambda valor: valor.find_elements(By.CLASS_NAME, "Er7QU")) #El atributo "timeout" indica el tiempo límite de la pausa, mientras que "pool_frequency"  es la frecuencia en segundos con la que buscará el valor
        #Damos click al botón de búsqueda (es el mismo botón que retroceder)
        boton_busqueda[0].click()
        #Pausamos un tiempo el programa para que el programa procese bien la introduccion de datos entre teléfono y teléfono
        time.sleep(sleep)
        #Almacenamos en una variable la etiqueta del campo para instroducir el número telefónico
        campo=navegador.find_elements(By.CLASS_NAME, "Er7QU") 
        #Escribimos el teléfono en el campo (recordar que al tener un atributo de clase y no id en HTML, pueden haber varios)
        campo[0].send_keys(telefono)
        #Tiempo que se pausará la ejecución (para dar margen a encontrar el teléfono)
        time.sleep(20)
        #Presionamos la tecla "ENTER"
        campo[0].send_keys(Keys.ENTER)
        #Verificamos que el contacto existe
        verificacion=navegador.find_elements(By.CLASS_NAME, "f8jlpxt4")
        #Si existe cambiamos la variable a True
        if len(verificacion)==0:
            busqueda=True
        else:
            #Si es el primer intento de búsqueda lanzamos nuevamente la función para buscarlo SOLO una vez más
            if contador==0:
                BorrarCampos(navegador)
                BuscarNumero(navegador, telefono, 1, 10)
        #Retornamos el resultado (VERSION ANTERIOR)
        #OJO! Recordar que en las funciones recursivas si ponemos los retornos dentro de condiciones hará que retorne "None"
        #return busqueda
    #En caso de no haberse cargado la página
    except Error as mensaje:
        #Generamos el nombre de la excepción y la guardamos en su variable correspondiente
        excepcion=str(type(mensaje).__name__)
        #Retornamos (VERSION ANTERIOR)
        #return "ERROR"

#Funcion para escribir el mensaje
def EscribirMensaje(navegador, paciente):
    time.sleep(5) #Correción a whatsapp web 31 mayo 2022, ya que si no lo pausamos después de encontrar el número de teléfono parece que el DOM de JS tarda en mostrar la etiqueta del campo de texto
    #Buscamos el campo por su etiqueta
    campo=navegador.find_elements(By.CLASS_NAME, "selectable-text")
    #Creamos los mensajes OJO! Recordar que en chromedriver no se pueden poner emojis
    mensaje=f"*¡FELICIDADES {paciente}!*"
    campo[-1].send_keys(mensaje)
    #Esta combinacion  de teclas (SHIFT Izq + ENTER) realiza un salto de línea en WhatsApp Web
    campo[-1].send_keys(Keys.LEFT_SHIFT+Keys.ENTER)
    mensaje="Desde el _'El Médico A Tu Lado'_ le deseamos un *FELIZ* día y mucha *SALUD*."
    campo[-1].send_keys(mensaje)
    campo[-1].send_keys(Keys.LEFT_SHIFT+Keys.ENTER)
    mensaje="Estamos a su disposición."
    campo[-1].send_keys(mensaje)
#    campo[1].send_keys(Keys.ENTER)
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
    #Variable donde se guardará el estado predeterminado de la búsqueda
    busqueda=False
    #Concatenamos el nombre completo
    paciente=nombre+" "+apellidos
    #Buscamos el numero
    BuscarNumero(navegador, numero)
    #Si no se genera excepcion
    if excepcion=="":
        #Si el numero existe
        if busqueda==True:
            #Lo agregamos a la lista de existentes
            listado_existentes.append(paciente)
            #Le enviamos el mensaje
            EscribirMensaje(navegador, nombre)
        #Si no existe
        else:
            if busqueda==False:
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
notificacion_mail.DatosMensaje(excepcion, listado_existentes, listado_inexistentes)
