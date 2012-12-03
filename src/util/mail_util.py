# -*- coding: utf-8 -*-
'''
Created on 2012-11-14

@author: huangchong
'''
import smtplib
import email.utils
from email.mime.text import MIMEText
from email.Header import Header
# Create the message
msg = MIMEText('测试邮件请删除','plain','utf-8')
msg.set_unixfrom('author')
msg['To'] = email.utils.formataddr(( 'Recipient',
['support@jztec.cn']))
msg['From'] = email.utils.formataddr(( 'Author',
'service@jztec.cn'))
msg['Subject'] = Header('华丽的扯淡啊！！！','utf-8')
server = smtplib.SMTP('smtp.jztec.cn')
try :
    server.ehlo()
# If we can encrypt this session, do it
    if server.has_extn('STARTTLS'):
        server.starttls()
        server.ehlo() # reidentify ourselves over TLS connection
    server.login("service@jztec.cn", "jztec123")   
    server.sendmail('service@jztec.cn',  
    ['huangchong@jztec.cn'],
    msg.as_string())
finally:
    server.quit()