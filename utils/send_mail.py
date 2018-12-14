#!/usr/bin/env python
# -*- coding:utf-8 -*-
# written by diyuhuan
# 发送邮件(wd_email_check123账号用于内部测试使用，不要用于其他用途)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import datetime

sender = '18516987026@163.com'
subject = u'邮箱验证'
smtpserver = 'smtp.163.com'
username = '18516987026@163.com'
password = 'wangfei121'
mail_postfix = "163.com"


def send_email(receiver, content):
    try:
        me = username + "<" + username + "@" + mail_postfix + ">"
        msg = MIMEText(content, 'html', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        return True
    except Exception as e:
        print('send_email has error with : ' + str(e))
        return False


def pack_html(receiver, url):
    html_content = u"<html><div>尊敬的用户<font color='#0066FF'>%s</font> 您好！</div><br>" \
                   "<div>感谢您关注我们的平台 ，我们将为您提供最贴心的服务，祝您购物愉快。</div><br>" \
                   "<div>点击以下链接，即可完成邮箱安全验证：</div><br>" \
                   "<div><a href='%s'>%s</a></div><br>" \
                   "<div>为保障您的帐号安全，请在24小时内点击该链接; </div><br>" \
                   "<div>若您没有申请过验证邮箱 ，请您忽略此邮件，由此给您带来的不便请谅解。%s</div>" \
                   "</html>" % (receiver, url, url,datetime.datetime.today())
    html_content = html_content
    return html_content


if __name__ == "__main__":
    url = "http://1000phone.com"
    receiver = '18500327026@163.com'
    content = pack_html(receiver, url)
    # content = 'this is email content. at %s.' % int(time.time())
    send_email(receiver, content)


"""
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

with open('a.jpg', 'rb')as f:
    img_data = f.read()

# msg = MIMEText('afsdfasdfasdf', 'plain', 'utf-8')
subject = "python邮件测试"  # 主题
msg = MIMEMultipart('related')
content = MIMEText('<html><body>< img src="cid:imageid" alt="imageid"></body></html>', 'html', 'utf-8')  # 正文
# msg = MIMEText(content)
msg.attach(content)
img = MIMEImage(img_data)
img.add_header('Content-ID', 'imageid')
msg.attach(img)
msg['From'] = formataddr(["辉", 'yonghui686868@163.com'])
msg['To'] = formataddr(["凯", 'm15103235465@163.com'])
msg['Subject'] = "有故障单了"

server = smtplib.SMTP("smtp.163.com", 25)
server.login("yonghui686868@163.com", "密码")
server.sendmail('yonghui686868@163.com', ['m15103235465@163.com', ], msg.as_string())
server.quit()
"""