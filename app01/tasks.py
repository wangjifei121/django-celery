from __future__ import absolute_import
import time
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from proj.celery import app

from utils.send_mail import pack_html, send_email


@app.task
def tsend_email():
    url = "http://1000phone.com"
    receiver = '18500327026@163.com'
    content = pack_html(receiver, url)
    send_email(receiver, content)
    print('send email ok!')


@app.task
def add(x, y):
    return x + y
