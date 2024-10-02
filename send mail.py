from email.message import EmailMessage
import ssl
import smtplib

# Email details
email_sender = 'your_email@gmail.com'  # Replace with your email
email_password = 'your_app_password'  # Replace with your app password
email_receiver = 'recipient_email@gmail.com'  # Replace with recipient's email

subject = 'Your Subject Here'
body = '''
Your email body goes here. You can customize this as needed.
'''

# Create the email
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Secure SSL context
context = ssl.create_default_context()

# Send the email using Gmail's SMTP server
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
