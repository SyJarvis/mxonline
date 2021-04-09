# -*- coding: UTF-8 -*-
__author__ = 'shangye'
__date__ = '4/9/21 11:30 PM'
from random import Random
from users.models import EmailVerifyRecord
from django.core.mail import send_mail

def random_str(randomlength=8):
    str = ''
    chars = 'AsBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "幕学在线网注册激活链接"
        email_body = "请点击下边的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)

    send_mail(email_title)
def generate_random_str():
