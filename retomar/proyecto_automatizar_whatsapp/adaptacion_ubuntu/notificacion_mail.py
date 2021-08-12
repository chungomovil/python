#Importamos librerias necesarias
import smtplib
from email.mime.text import MIMEText
import credenciales

#Funcion para enviar por mail el resultado
def EnviarEmail(excepcion, listado_existentes="", listado_inexistentes=""):
    #Cargamos las credenciales desde su modulo
    emisor, receptor, passwd=credenciales.Correo()
    #String para el cuerpo del mensaje
    cuerpo_mensaje=""
    #Abrimos conexion con Gmail
    servidorSMTP=smtplib.SMTP("smtp.gmail.com", 587)
    servidorSMTP.ehlo()
    servidorSMTP.starttls()
    #Hacemos login en la cuenta de correo que enviará el mensaje
    servidorSMTP.login(emisor, passwd)
    #Si no se generó exepción (se terminó de ejecutar sin problemas)
    if excepcion=="":
        #Agregamos al cuerpo del mensaje los que se han felicitado
        if len(listado_existentes)>0:
            cuerpo_mensaje+="\nSe han felicitado a los pacientes\n"+50*"-"+"\n"
            for nombre in listado_existentes:
                cuerpo_mensaje+=nombre+"\n"
        #Agregamos al cuerpo del mensaje los que no se han felicitado
        if len(listado_inexistentes)>0:
            cuerpo_mensaje+="\nNo se ha podido felicitar a los pacientes\n"+50*"-"+"\n"
            for nombre in listado_inexistentes:
                cuerpo_mensaje+=nombre+"\n"
        #Indicamos cual será la variable del cuerpo del mensaje
        mensaje=MIMEText(cuerpo_mensaje)
        #Indicamos el asunto del mensaje
        mensaje["Subject"]="Felicitaciones enviadas correctamente."
    #Si se generó una excepción (no se ejecutó correctamente)
    else:
        #Creamos el cuerpo del mensaje y escribir el nombre de la excepción
        cuerpo_mensaje=f"Se ha producido el error: ({excepcion})"
        #Indicamos la variable del cuerpo del mensaje
        mensaje=MIMEText(cuerpo_mensaje)
        #Indicamos el asunto del mensaje
        mensaje["Subject"]="Se produjo un error en el programa de felicitaciones."
    
    #Especificamos la cuenta de correo del que se enviará el mensaje
    mensaje["From"]=emisor
    #Especificamos la cuenta de correo al que se enviará el mensaje
    mensaje["To"]=f"{receptor[0]}, {receptor[1]}"
    #Lo transformamos en string y lo enviamos
    servidorSMTP.sendmail(emisor, receptor, mensaje.as_string())
    #Cerramos la conexion con gmail
    servidorSMTP.close()
    #Informamos que se ha enviado el correo
    print("--> Se ha enviado el resultado por correo electrónico.")
