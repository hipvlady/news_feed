import smtplib
import statics
import main
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# set up the SMTP server
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
MY_ADDRESS = main.secrets['email']
PASSWORD = main.secrets['app_pass']
s.login(MY_ADDRESS, PASSWORD)

# For each contact, send the email:
msg = MIMEMultipart()       # create a message
msg['From'] = MY_ADDRESS
msg['To'] = statics.email
msg['Subject'] = statics.subject

# add in the message body as HTML
msg.attach(MIMEText(main.email_content, 'html'))
