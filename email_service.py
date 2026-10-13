# EMAIL SEND
import smtplib
from email.message import EmailMessage
from app.config import sender_email
from app.config import app_password

def send_email(to_email, subject, body): 
    message = EmailMessage()

    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    message.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
       smtp.login(sender_email, app_password)

       smtp.send_message(message)

