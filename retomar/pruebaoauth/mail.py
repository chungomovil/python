import httplib2
import os
import oauth2client
from oauth2client import client, tools, file
import base64
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors, discovery


def ObtenerCredenciales():
    carpeta_usuario=os.path.expanduser("~")
    carpeta_credenciales=os.path.join(carpeta_usuario, "credenciales")
    if not os.path.exists(carpeta_credenciales):
        os.makedirs(carpeta_credenciales)
    archivo_credenciales=os.path.join(carpeta_credenciales,"credentials.json")
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

def CrearYEnviar(sender, to, subject, message_text_html):
    credenciales=ObtenerCredenciales()
    http=httplib2.Http()
    http=credenciales.authorize(httplib2.Http())
    service=discovery.build("gmail", "v1", http=http)
    mensaje=CrearMensaje(sender, to, subject, message_text_html)
    EnviarMensaje(service, "me", mensaje, message_text_html)

def CrearMensaje(sender, to, subject, message_text_html):
    message = MIMEMultipart('alternative') # needed for both plain & HTML (the MIME type is multipart/alternative)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = to

    #Create the body of the message (a plain-text and an HTML version)
    #message.attach(MIMEText(message_text_plain, 'plain'))
    message.attach(MIMEText(message_text_html, 'html'))

    raw_message_no_attachment = base64.urlsafe_b64encode(message.as_bytes())
    raw_message_no_attachment = raw_message_no_attachment.decode()
    body  = {'raw': raw_message_no_attachment}
    return body

def EnviarMensaje(service, user_id, body, message_text_plain):
    try:
        message_sent = (service.users().messages().send(userId=user_id, body=body).execute())
        message_id = message_sent['id']
        # print(attached_file)
        print (f'Mensaje enviado \n\n ID mensaje: {message_id}\n\n Mensaje:\n\n {message_text_plain}')
        # return body
    except errors.HttpError as error:
        print (f'Hubo un error al enviar el mensaje: {error}')
    
def DatosMensaje():
    to = "correo1@gmail.com"
    sender = "correo2@gmail.com"
    subject = "Prueba"
    message_text_html  = r'Hi<br/>Html <b>hello</b>'
    #message_text_plain = "Hi\nPlain Email"
    CrearYEnviar(sender, to, subject, message_text_html)



if __name__=="__main__":
    DatosMensaje()
