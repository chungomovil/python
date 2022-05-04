#Importamos librerias necesarias
import httplib2
import os
import oauth2client
from oauth2client import client, tools, file
import base64
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors, discovery
import credenciales

def DatosMensaje(excepcion, listado_existentes="", listado_inexistentes=""):
    #Importamos las cuentas de correo que se utilizarán
    emisor, receptores=credenciales.Correo()
    #Descomprimimos la lista para manejar mejor la cadena de caracteres
    receptor=receptores[0]+","+receptores[1]
    cuerpo_mensaje_html=""
    #Si no se generó excepción (se terminó de ejecutar sin problemas)
    if excepcion=="":
        #Agregamos al cuerpo del mensaje los que se han felicitado
        if len(listado_existentes)>0:
            cuerpo_mensaje_html+=r"<br/>Se han felicitado a los pacientes<br/>"+50*"-"+"<br/>" #La 'r' significa cadena en formato raw
            for nombre in listado_existentes:
                cuerpo_mensaje_html+=nombre+r"<br/>"
        #Agregamos al cuerpo del mensaje los que no se han felicitado
        if len(listado_inexistentes)>0:
            cuerpo_mensaje_html+=r"<br>No se ha podido felicitar a los pacientes<br/>"+50*"-"+"<br/>"
            for nombre in listado_inexistentes:
                cuerpo_mensaje_html+=nombre+r"<br/>"
        asunto="Felicitaciones enviadas correctamente."
    #Si se generó excepsión (terminó de ejecutarse con algún problema)
    else:
        cuerpo_mensaje_html=f"Se ha producido el error con código: ({excepcion})"
        asunto="Se produjo un error en el programa felicitaciones"
    #Enviamos todos los datos a la siguiente función
    CrearYEnviar(emisor, receptor, asunto, cuerpo_mensaje_html)

#Función para obtener las credenciales Oauth
def ObtenerCredenciales():
    #Vamos a la carpeta "home" del usuario
    carpeta_usuario=os.path.expanduser("~")
    #Buscamos la carpeta "credenciales"
    carpeta_credenciales=os.path.join(carpeta_usuario, ".credenciales")
    #Si no existe la carpeta, la creamos
    if not os.path.exists(carpeta_credenciales):
        os.makedirs(carpeta_credenciales)
    #Buscamos el archivo de las credenciales
    archivo_credenciales=os.path.join(carpeta_credenciales,"credenciales.json")
    #Indicamos donde están las credenciales al servicio Oauth
    almacenar=oauth2client.file.Storage(archivo_credenciales)
    #Capturamos las credenciales
    credenciales=almacenar.get()
    #Si no existe el archivo o son invalidas
    if not credenciales or credenciales.invalid:
        #Indicamos la ruta del archivo python actual para que encuentre bien el archivo principal de credenciales
        carpeta_actual=os.path.dirname(__file__)
        #La url de la API que usará para enviar el correo
        SCOPES = 'https://www.googleapis.com/auth/gmail.send'
        #Indicamos donde está el archivo de las credenciales
        CLIENT_SECRET_FILE = os.path.join(carpeta_actual, "client_secret.json")
        #Nombre de la aplicacion
        APPLICATION_NAME = 'Gmail API Python Send Email'
        #Iniciamos el agente de autentificacion de Oauth
        flow=client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent=APPLICATION_NAME
        credenciales=tools.run_flow(flow, almacenar)
    #Retornamos las credenciales
    return credenciales

#Función para conectar con la API de Gmail
def CrearYEnviar(emisor, receptor, asunto, cuerpo_mensaje_html):
    #Capturamos las credenciales
    credenciales=ObtenerCredenciales()
    #Conectamos con la API de Gmail
    http=httplib2.Http()
    http=credenciales.authorize(httplib2.Http())
    service=discovery.build("gmail", "v1", http=http)
    #Llalamos a las funciones que crearán y enviarán el mensaje
    mensaje=CrearMensaje(emisor, receptor, asunto, cuerpo_mensaje_html)
    EnviarMensaje(service, "me", mensaje, cuerpo_mensaje_html)

#Función para crear el mensaje
def CrearMensaje(emisor, receptor, asunto, cuerpo_mensaje_html):
    #Creamos las partes del correo
    mensaje = MIMEMultipart('alternative') # Necesario para crear mensajes en plano y html (en texto plano no se está usando en este programa)
    mensaje['Subject'] = asunto
    mensaje['From'] = emisor
    mensaje['To'] = receptor
    mensaje.attach(MIMEText(cuerpo_mensaje_html, 'html'))
    #Codificamos el contenido
    raw_mensaje = base64.urlsafe_b64encode(mensaje.as_bytes())
    raw_mensaje = raw_mensaje.decode()
    cuerpo  = {'raw': raw_mensaje}
    #Retornamos cuerpo del mensaje
    return cuerpo

#Función para enviar el mensaje
def EnviarMensaje(service, user_id, mensaje, message_text_html=""):
    #Algoritmo a intentar
    try:
        #Enviamos el mensaje
        message_sent = (service.users().messages().send(userId=user_id, body=mensaje).execute())
        #Obtenemos el id del mensaje enviado
        message_id = message_sent['id']
        #Mostramos por pantalla el mensaje enviado
        print (f'Mensaje enviado \n\n ID mensaje: {message_id}\n\n Mensaje:\n\n {message_text_html}')
    #Si hay un error lo imprime
    except errors.HttpError as error:
        print (f'Hubo un error al enviar el mensaje: {error}')

