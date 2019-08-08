from email.mime.text import MIMEText
from email.header import Header
import smtplib 
import getpass

def send_mail(host,passwd,sender,receivers,msg,subject):
    msg=MIMEText(body,'plain','utf8')
    msg['From']=Header(sender,'utf8')
    msg['To']=Header(receivers[0],'utf8')
    msg['Subject']=Header(subject,'utf8')
    smtp=smtplib.SMTP()
    smtp.connect(host,25)
    # smtp.starttls()腾讯要使用这种安全连接
    smtp.login(sender,passwd)
    smtp.sendmail(sender,receivers,msg.as_bytes())

if __name__=="__main__":
    sender='daneiyunzhijia@163.com'
    receivers=['daneiyunzhijia@163.com']
    server='smtp.163.com'
    # 此处编写授权码
    passwd=getpass.getpass()
    body='Hello from python'
    subject='py must mail'
    send_mail(server,passwd,sender,receivers,body,subject)
