#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """
from sdk.controller.model.base_http_request import BaseHttpRequest
from sdk.controller.model.http_request_type import HttpRequestTypes

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class LoginRequestBuilder(object):
    def __init__(self):
        self.url = "/Services/Authentication/Login.do"
        self.request_type = HttpRequestTypes.POST

    def build_login_request(self, username, password, rememberme):
        request_params = dict()
        request_params["loginName"] = username
        request_params["password"] = password
        request_params["rememberme"] = rememberme
        login_http_request = BaseHttpRequest()
        BaseHttpRequest.auth_cookies.clear()
        login_http_request.params = request_params
        login_http_request.url = self.url
        login_http_request.request_type = self.request_type
        return login_http_request
