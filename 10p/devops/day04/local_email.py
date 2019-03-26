from email.mime.text import MIMEText
from email.header import Header
import smtplib

message = MIMEText('Python test email', 'plain', 'utf8')
message['From']=Header('root@localhost','utf8')
message['To']=Header('bob@localhost','utf8')
message['Subject'] = Header('py email', 'utf8')

sender="root@localhost"
receivers=['2513556525@qq.com','bob@localhost']
smpt = smtplib.SMTP('localhost')
smpt.sendmail(sender,receivers,message.as_bytes())