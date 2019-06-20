#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module describes models for email server and sent message"""

# imports

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class EmailServer(object):
    def __init__(self, server=None, port=None, from_email=None, from_passw=None):
        self.server = server
        self.port = port
        self.from_email = from_email
        self.from_passw = from_passw


class Message(object):
    def __init__(self, to_mail=None, text=None, subject=None, img_path=None, img_id=None, file_path=None, cert_path=None, cert_id=None):
        # https://www.textfixer.com/html/compress-html-compression.php
        self.text = text
        self.to_mail = to_mail
        self.subject = subject
        self.img_path = img_path
        self.img_id = img_id
        self.cert_path = cert_path
        self.cert_id = cert_id
        self.file_path = file_path
