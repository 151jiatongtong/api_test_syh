#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib,sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sys.path.append("..")
from config.config import *

def send_email(report_file):
    msg = MIMEMultipart()
    msg.attach(MIMEText(email_body,"plain","utf-8"))
    msg['From'] = smtp_user
    msg['To'] = receiver
    msg['Subject'] = sunject
    #上传的附件
    with open(report_file,"rb") as f:
        att1_body = f.read()

    att1 = MIMEText(att1_body,"base64","utf-8")
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="{}"'.format(report_file)
    #将附件加入到发送的邮件
    msg.attach(att1)

    smtp = smtplib.SMTP_SSL(smtp_server)
    smtp.login(smtp_user,smtp_password)
    smtp.sendmail(smtp_user,receiver,msg.as_string())
    smtp.quit()
    print("发送完成")
