#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

from sdk.controller.model.base_http_request import BaseHttpRequest
from sdk.controller.model.http_request_type import HttpRequestTypes

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class GetAllCategoryRequestBuilder(object):
    def __init__(self):
        self.url = "/Services/Category/GetMenuCategories.do"
        self.request_type = HttpRequestTypes.POST

    def build(self):
        request_params = dict()
        get_all_category_http_request = BaseHttpRequest()
        get_all_category_http_request.params = request_params
        get_all_category_http_request.url = self.url
        get_all_category_http_request.request_type = self.request_type
        return get_all_category_http_request
