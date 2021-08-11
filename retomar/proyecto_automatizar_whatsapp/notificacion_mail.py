import smtplib
from email.mime.text import MIMEText
import credenciales

def EnviarEmail(excepcion, listado_existentes="", listado_inexistentes=""):
    emisor, receptor, passwd=credenciales.Correo()
    cuerpo_mensaje=""
    servidorSMTP=smtplib.SMTP("smtp.gmail.com", 587)
    servidorSMTP.ehlo()
    servidorSMTP.starttls()
    servidorSMTP.login(emisor, passwd)
    if excepcion=="":
        if len(listado_existentes)>0:
            cuerpo_mensaje+="\nSe han felicitado a los pacientes\n"+50*"-"+"\n"
            for nombre in listado_existentes:
                cuerpo_mensaje+=nombre+"\n"
        if len(listado_inexistentes)>0:
            cuerpo_mensaje+="\nNo se ha podido felicitar a los pacientes\n"+50*"-"+"\n"
            for nombre in listado_inexistentes:
                cuerpo_mensaje+=nombre+"\n"
        mensaje=MIMEText(cuerpo_mensaje)
        mensaje["Subject"]="Felicitaciones enviadas correctamente."
    else:
        cuerpo_mensaje=f"Se ha producido el error: ({excepcion})"
        mensaje=MIMEText(cuerpo_mensaje)
        mensaje["Subject"]="Se produjo un error en el programa de felicitaciones."
    mensaje["From"]=emisor
    mensaje["To"]=receptor
    servidorSMTP.sendmail(emisor, receptor, mensaje.as_string())
    servidorSMTP.close()
    print("--> Se ha enviado el resultado por correo electrónico.")
