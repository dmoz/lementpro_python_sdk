#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports
from sdk.controller.model.base_http_request import BaseHttpRequest
from sdk.controller.model.http_request_type import HttpRequestTypes

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"

"""
{"objectId":22774,"subject":"",,"addedFileIds":[],"employees":[],"externalEmails":["ev.nalivayko@mail.ru"]}
"""

class SendMessageToExternalUserRequestBuilder(object):
    def __init__(self):
        self.url = "/Services/Action/Create.do"
        self.request_type = HttpRequestTypes.POST

    def build(self, object, external_emails_list, message):
        request_params = dict()
        request_params["objectId"] = object
        request_params["externalEmails"] = external_emails_list
        request_params["message"] = "<span id=\"33138de8-614b-40e7-9196-eb2e7bf28781\" contenteditable=\"false\" class=\"k-button external-email\" data-id=\"{emails}\" value=\"{emails}\"><b>{emails}</b></span>{message}".format(emails=external_emails_list, message=message)
        http_request = BaseHttpRequest()
        http_request.params = request_params
        http_request.url = self.url
        http_request.request_type = self.request_type
        return http_request
