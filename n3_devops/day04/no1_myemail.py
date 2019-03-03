from email.mime.text import  MIMEText
from email.header import Header
import smtplib

message = MIMEText("python text\n",'plain','utf8')
message['From'] = Header('njlihan@tedu.cn','utf8')
message['To'] = Header('2513556525@qq.com','utf8')
message['Subject'] = Header('TEST','utf8')
smtp = smtplib.SMTP('localhost')
sender= "njlihan@tedu.cn"
# receivers = ['2513556525@qq.com','root@localhost']
receivers = ['root@localhost']
smtp.sendmail(sender,receivers,message.as_string())