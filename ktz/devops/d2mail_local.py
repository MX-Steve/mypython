from email.mime.text import MIMEText
from email.header import Header
import smtplib 

# 邮件正文(纯文本形式)
message=MIMEText('python email test','plain','utf-8')
# 邮件头部信息：发件人，收件人，主题
message['From']=Header('root','utf8')
message['To']=Header('bob','utf8')
message['Subject']=Header('python test','utf8')

# 发送邮件
smtp = smtplib.SMTP('localhost')
sender='root'
receivers=['root','bob']
smtp.sendmail(sender,receivers,message.as_bytes())
