#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports
from sdk.controller.builder.login_request_builder import LoginRequestBuilder
from sdk.controller.model.base_http_request import BaseHttpRequest
from sdk.controller.sender.http_sender import HttpSender

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class SessionController(object):

    def login(self, username, password, rememberme, host, st_code):
        login_request_builder = LoginRequestBuilder()
        login_request = login_request_builder.build_login_request(username, password, rememberme)
        response = HttpSender.send_request(login_request, host)
        assert response.status_code == st_code
        if response.cookies:
            BaseHttpRequest.auth_cookies['auth'] = response.cookies['auth']
            BaseHttpRequest.auth_cookies['host'] = host
        return response.json()
