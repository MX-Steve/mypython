from email.mime.text import MIMEText
from email.header import Header
import smtplib
# import getpass

def send_mail(text,sender,receivers,subject,host,passwd):
    message = MIMEText(text, 'plain', 'utf8')
    message['From']=Header(sender,'utf8')
    message['To']=Header(receivers[0],'utf8')
    message['Subject'] = Header(subject, 'utf8')

    smpt = smtplib.SMTP()
    smpt.connect(host)
    smpt.login(sender,passwd)
    smpt.sendmail(sender,receivers,message.as_bytes())

if __name__ == '__main__':
    passwd = 'haiweqdesvnfdhig'
    send_mail("text py ...\r\n",'2513556525@qq.com',['2513556525@qq.com'],'python test','smtp.qq.com',passwd)