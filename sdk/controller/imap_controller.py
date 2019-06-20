#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

import base64
import imaplib
import email

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class MailHelper(object):

    def __init__(self):
        self.mail = imaplib.IMAP4_SSL(lement_config['current-staging']['imap_host'],
                                 lement_config['current-staging']['imap_port'])
        self.mail.login(lement_config['current-staging']['email_login'], lement_config['current-staging']['email_password'])

    def get_message_text_from_unseen_last_message(self):

        self.mail.select("inbox")

        result, data = self.mail.uid('search', None, "(UNSEEN)")
        try:
            latest_email_uid = data[0].split()[-1]
        except IndexError:
            logger.debug("\n")
            logger.debug("WARNING: New messages is not in inbox")

        result, data = self.mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message_instance = email.message_from_bytes(raw_email)

        maintype = email_message_instance.get_content_maintype()
        if maintype == 'multipart':
            for part in email_message_instance.get_payload():
                if part.get_content_maintype() == 'text':
                    return part.get_payload()
        elif maintype == 'text':
            return base64.b64decode(email_message_instance.get_payload()).decode('utf-8')

        self.mail.close()
        self.mail.logout()

    def clear_inbox_folder(self):
        self.mail.select("inbox")
        typ, data = self.mail.search(None, 'ALL')
        for num in data[0].split():
            self.mail.store(num, '+FLAGS', '\\Deleted')
        self.mail.expunge()
        self.mail.close()
        self.mail.logout()
