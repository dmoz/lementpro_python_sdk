#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports
from sdk.controller.builder.send_message_to_external_user_r_builder import \
    SendMessageToExternalUserRequestBuilder
from sdk.controller.sender.http_sender import HttpSender

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class ActionController(object):
    def send_massage_to_external_user(self, object, external_emails_list, message, st_code):
        """/Services/Action/Create.do"""
        builder = SendMessageToExternalUserRequestBuilder()
        get_tree_folders_request = builder.build(object, external_emails_list, message)
        response = HttpSender.send_request(get_tree_folders_request)
        assert response.status_code == st_code
        return response.json()
