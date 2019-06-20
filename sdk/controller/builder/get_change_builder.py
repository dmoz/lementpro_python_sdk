#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports
from sdk.controller.model.base_http_request import BaseHttpRequest
from sdk.controller.model.http_request_type import HttpRequestTypes

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class GetChangeBuilder(object):
    def __init__(self):
        self.url = "/Services/ObjectBase/GetChangedObjects.do"
        self.request_type = HttpRequestTypes.POST

    def build(self,  type_id, from_date, to_date):
        request_params = dict()
        request_params["rootObjectTypeId"] = type_id
        request_params["fromDate"] = from_date
        request_params["toDate"] = to_date
        http_request = BaseHttpRequest()
        http_request.params = request_params
        http_request.url = self.url
        http_request.request_type = self.request_type
        return http_request
