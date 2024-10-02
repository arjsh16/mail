
from email.message import EmailMessage
import ssl
import smtplib
from details import *

email_sender=Mydetails.sender_email
email_password=Mydetails.sender_pwd
email_reciever=str(input("Reciever email address:\n"))

subject=input("Subject:\n")
body=input("Body:\n")

em=EmailMessage()

em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context=ssl.create_default_context()
#smtp:simple mail transfer protocol
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())
