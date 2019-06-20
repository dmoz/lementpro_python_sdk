#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports
from sdk.controller.model.base_http_request import BaseHttpRequest
from sdk.controller.model.http_request_type import HttpRequestTypes

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class GetOperationLogRequestBuilder(object):
    def __init__(self):
        self.url = "/Services/Dictionaries/DictionaryRecord/GetList.do"
        self.request_type = HttpRequestTypes.POST

    def build(self, date_from, date_to):
        request_params = dict()
        filter = dict()
        # request_params["take"] = 25
        # request_params["skip"] = 0
        # request_params["page"] = 1
        # request_params["pageSize"] = 25
        filter["startDate"] = date_from
        filter["endDate"] = date_to
        request_params["filter"] = filter
        http_request = BaseHttpRequest()
        http_request.params = request_params
        http_request.url = self.url
        http_request.request_type = self.request_type
        return http_request
