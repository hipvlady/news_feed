import smtplib
import statics
import aws
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

secrets = aws.get_secret()


def setup_server():
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()

    MY_ADDRESS = secrets['email']
    PASSWORD = secrets['app_pass']

    try:
        server.login(MY_ADDRESS, PASSWORD)
    except smtplib.SMTPAuthenticationError:
        print("Failed to login")
    else:
        print("Logged in successfully")

    return server, MY_ADDRESS


server, MY_ADDRESS = setup_server()


def send_msg(email_content):
    # create a message
    msg = MIMEMultipart()
    msg['From'] = MY_ADDRESS
    msg['To'] = secrets['receiver']
    msg['Subject'] = statics.subject

    # add in the message body as HTML
    msg.attach(MIMEText(email_content, 'html'))

    # send the message via the server set up earlier.
    try:
        server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")
    else:
        print("Email sent successfully")


# Close the server connection when done
server.quit()
