# Code pour envoyer un e-mail
import smtplib
from email.mime.text import MIMEText

def envoyer_email(sujet, message):
    password = "M2iformation07"

    msg = createMessage(sujet, message)

    try:
        sendMail(msg, password)
        print("E-mail envoyé avec succès !")
    except Exception as e:
        print(f"Une erreur est survenu lors de l'envoie du mail : {str(e)}")

def createMessage(sujet, message):
    msg = MIMEText(message)
    msg['Subject'] = sujet
    msg['From'] = "noreply@drinksdistibution.com"
    msg['To'] = "nino.herran@ecole-isitech.fr"
    return msg


def sendMail(msg, password):
    server = smtplib.SMTP('ssl0.ovh.net', 587)
    server.connect('ssl0.ovh.net', 587)
    server.starttls()
    server.login('pythondev@benke.fr', password)
    server.sendmail(msg.as_string())
    server.quit()