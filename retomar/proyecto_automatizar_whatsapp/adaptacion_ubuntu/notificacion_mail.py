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
    emisor, receptores=credenciales.Correo()
    receptor=receptores[0]+","+receptores[1]
    cuerpo_mensaje_html=""
    if excepcion=="":
        if len(listado_existentes)>0:
            cuerpo_mensaje_html+=r"<br/>Se han felicitado a los pacientes<br/>"+50*"-"+"<br/>"
            for nombre in listado_existentes:
                cuerpo_mensaje_html+=nombre+r"<br/>"
        if len(listado_inexistentes)>0:
            cuerpo_mensaje_html+=r"<br>No se ha podido felicitar a los pacientes<br/>"+50*"-"+"<br/>"
            for nombre in listado_inexistentes:
                cuerpo_mensaje_html+=nombre+r"<br/>"
        asunto="Felicitaciones enviadas correctamente."
    else:
        cuerpo_mensaje_html=f"Se ha producido el error con código: ({excepcion})"
        asunto="Se produjo un error en el programa felicitaciones"
    CrearYEnviar(emisor, receptor, asunto, cuerpo_mensaje_html)

def ObtenerCredenciales():
    carpeta_usuario=os.path.expanduser("~")
    carpeta_credenciales=os.path.join(carpeta_usuario, ".credenciales")
    if not os.path.exists(carpeta_credenciales):
        os.makedirs(carpeta_credenciales)
    archivo_credenciales=os.path.join(carpeta_credenciales,"credenciales.json")
    almacenar=oauth2client.file.Storage(archivo_credenciales)
    credenciales=almacenar.get()
    if not credenciales or credenciales.invalid:
        carpeta_actual=os.path.dirname(__file__)
        SCOPES = 'https://www.googleapis.com/auth/gmail.send'
        CLIENT_SECRET_FILE = os.path.join(carpeta_actual, "client_secret.json")
        APPLICATION_NAME = 'Gmail API Python Send Email'
        flow=client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent=APPLICATION_NAME
        credenciales=tools.run_flow(flow, almacenar)
    return credenciales

def CrearYEnviar(emisor, receptor, asunto, cuerpo_mensaje_html):
    credenciales=ObtenerCredenciales()
    http=httplib2.Http()
    http=credenciales.authorize(httplib2.Http())
    service=discovery.build("gmail", "v1", http=http)
    mensaje=CrearMensaje(emisor, receptor, asunto, cuerpo_mensaje_html)
    EnviarMensaje(service, "me", mensaje, cuerpo_mensaje_html)

def CrearMensaje(emisor, receptor, asunto, cuerpo_mensaje_html):
    message = MIMEMultipart('alternative')
    message['Subject'] = asunto
    message['From'] = emisor
    message['To'] = receptor
    message.attach(MIMEText(cuerpo_mensaje_html, 'html'))
    raw_message_no_attachment = base64.urlsafe_b64encode(message.as_bytes())
    raw_message_no_attachment = raw_message_no_attachment.decode()
    body  = {'raw': raw_message_no_attachment}
    return body

def EnviarMensaje(service, user_id, mensaje, message_text_html=""):
    try:
        message_sent = (service.users().messages().send(userId=user_id, body=mensaje).execute())
        message_id = message_sent['id']
        print (f'Mensaje enviado \n\n ID mensaje: {message_id}\n\n Mensaje:\n\n {message_text_html}')
    except errors.HttpError as error:
        print (f'Hubo un error al enviar el mensaje: {error}')
