import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')


subject = "Test email from Python"
body = "This is a test email sent from a Python script using smtplib and email.mime.text."
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = SENDER_EMAIL
msg['To'] = RECIPIENT_EMAIL

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
    server.close()
    
    
    print('Email sent successfully')
except Exception as e:
    print(f'Something went wrong... {e}')
