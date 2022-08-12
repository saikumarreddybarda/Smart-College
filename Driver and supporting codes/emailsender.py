import datetime as dt
import time
import smtplib
import socket
dic={'leelaMam':{'9:40':'it-a','10:40':'it-b'},'chayaMam':{'9:40':'cse-b','10:40':'it-a'}}
def send_email(message,email):
    email_user = 'saikumarreddybarda@gmail.com'
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    socket.getaddrinfo('localhost',8080)
    server.starttls()
    server.login(email_user, 'sai@1041')
    #sending mail
    server.sendmail(email_user, 'bhardasaikumarreddy04@gmail.com',message)
    server.quit()
def at940():
    send_time = dt.datetime(2022,4,30,12,15,0)#year,month,day,hour,minute,sec
    time.sleep(abs(send_time.timestamp() - time.time()))
    #for leelaMam
    temp=dic['leelaMam']['9:40']
    message="You have Class of "+temp+" at 9_40"
    send_email(message,'leela@gmail.com')
    # for chayaMam
    temp = dic['chayaMam']['9:40']
    message = "You have Class of " + temp + " at 9_40"
   # send_email(message,'chaya@gmail.com')
    print('email sent')
def at1040():
    send_time = dt.datetime(2022,4,30,10,40,0)#year,month,day,hour,minute,sec
    time.sleep(send_time.timestamp() - time.time())
    #for leelaMam
    temp=dic['leelaMam']['10:40']
    message="You have Class of "+temp+" at 10_40"
    send_email(message,'leela@gmail.com')
    # for chayaMam
    temp = dic['chayaMam']['10:40']
    message = "You have Class of " + temp + " at 10_40"
    send_email(message,'chaya@gmail.com')
    print('email sent')

#calling the funtion
at940()