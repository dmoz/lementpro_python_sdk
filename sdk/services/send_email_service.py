#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

from os.path import basename

from sdk.services.model.email import EmailServer, Message

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


def mail_sender(server_object=EmailServer(), message_object=Message()):

    msg = MIMEMultipart('alternative')
    msg['From'] = server_object.from_email
    # msg['To'] = message_object.to_mail
    msg['To'] = ", ".join(message_object.to_mail)
    msg['Subject'] = message_object.subject

    body = MIMEText(message_object.text, 'html')
    msg.attach(body)

    if message_object.img_path is not None:
        fp = open(message_object.img_path, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', message_object.img_id)
        msg.attach(msgImage)

    if message_object.img_path is not None:
        with open(message_object.img_path, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(message_object.img_path)
            )
        #part['Content-Disposition'] = 'attachment; filename="%s"' % basename(message_object.img_path)
        part['Content-Disposition'] = 'attachment; filename="otkritka.%s"' % basename(message_object.img_path).split('.')[-1]
        msg.attach(part)

    if message_object.cert_path is not None:
        with open(message_object.cert_path, "rb") as cert:
            part = MIMEApplication(
                cert.read(),
                Name=basename(message_object.cert_path)
            )
       #part['Content-Disposition'] = 'attachment; filename="%s"' % basename(message_object.cert_path)
        part['Content-Disposition'] = 'attachment; filename="podarok.%s"' % basename(message_object.cert_path).split('.')[-1]
        msg.attach(part)

    # server = smtplib.SMTP(server_object.server, server_object.port)
    server = smtplib.SMTP_SSL(server_object.server, server_object.port)
    # server.starttls()
    server.login(server_object.from_email, server_object.from_passw)
    mess = msg.as_string()
    server.sendmail(server_object.from_email, message_object.to_mail, mess)
    server.quit()
