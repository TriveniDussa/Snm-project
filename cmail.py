#this file shouldn't name with email 
#smtpt lib=>Simple Mail Transfer Protocol =data transfer b\w one mail server to another
#ftp=>file tranfer
#networking protocals
app_password="kbbm juax qoic miuv"
import smtplib
from email.message import EmailMessage #class which is used to defail mail format(camel case)
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465) #ssl=security socket layout
    server.login('trivenidussa@gmail.com',app_password)
    msg=EmailMessage()
    msg['FROM']='trivenidussa@gmail.com'
    msg['SUBJECT']=subject
    msg['TO']=to
    msg.set_content(body)
    server.send_message(msg)
    server.close()

#cmail--- it is void--no return statement