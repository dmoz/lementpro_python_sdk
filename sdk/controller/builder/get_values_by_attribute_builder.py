#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

from sdk.controller.model.base_http_request import BaseHttpRequest
from sdk.controller.model.http_request_type import HttpRequestTypes

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class GetValuesByAttributeBuilder(object):
    def __init__(self):
        self.url = "/Services/ObjectTypes/AttributeListOfValues/GetValuesByAttribute.do"
        self.request_type = HttpRequestTypes.POST

    def build(self, atribut):
        request_params = dict()
        request_params["attributeId"] = atribut
        http_request = BaseHttpRequest()
        http_request.params = request_params
        http_request.url = self.url
        http_request.request_type = self.request_type
        return http_request
