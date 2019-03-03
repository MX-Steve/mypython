"""
from email.mime.text import MIMEText
from email.header import Header
import smtplib
# import getpass

def inet_mail(msg, subject, sender, receivers, server, username, password):
    message = MIMEText(msg, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')
    smtp = smtplib.SMTP()
    smtp.connect(server, port=25)
    # smtp.starttls()    # 如果服务器要求加密，打开注释
    smtp.login(username, password)
    smtp.sendmail(sender, receivers, message.as_string())

if __name__ == '__main__':
    sender = '2513556525@qq.com'
    receivers = ['2513556525@qq.com','dyloughtyvnugj@outlook.com']
    msg = 'python internet mail test'
    subject = 'py邮件测试'
    #passwd = getpass.getpass()
    passwd = 'ojnipwndyqdxdhha'
    inet_mail(msg, subject, sender, receivers, 'smtp.qq.com', sender, passwd)
"""
from email.mime.text import  MIMEText
from email.header import Header
import smtplib

def inet_mail(msg,subject,sender,receivers,server,username,password):
    message = MIMEText(msg, 'plain', 'utf8')
    message["From"] = Header(sender, 'utf8')
    message["To"]  = Header(receivers[0], 'utf8')
    message["Subject"] = Header(subject, 'utf8')
    smtp = smtplib.SMTP()
    smtp.connect(server, port=25)
    smtp.login(username,password)
    smtp.sendmail(sender,receivers,message.as_string())

if __name__ == '__main__':
    sender = "2513556525@qq.com"
    receivers = ["2513556525@qq.com"]
    msg = "hi\r\ni am steve\r\n i want you to visit my hoouse!\r\nsee you!"
    subject="Visiting for my birthday"
    password="ojnipwndyqdxdhha"
    inet_mail(msg,subject,sender,receivers,'smtp.qq.com', sender, password)