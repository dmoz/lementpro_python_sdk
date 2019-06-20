#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

import requests
import json

from sdk.controller.session_controller import SessionController

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class AuthService(object):

    host = None

    def login(self, user, server, st_code=200):
        """login with user object and server object"""
        session_controller = SessionController()
        response = session_controller.login(user.username, user.password, user.rememberme, server.host, st_code)
        return response

    def get_auth_token(self, name, password, server):
        """Получение токена авторизации"""
        url = server + "/Services/Authentication/Login.do"
        request_params = dict()
        request_params["loginName"] = name
        request_params["password"] = password
        request_params["rememberme"] = True
        data = json.dumps(request_params)
        headers = dict()
        headers["content-type"] = "application/json; charset=UTF-8"
        headers["Accept-Language"] = "ru-RU"
        response = requests.post(url, data=data, cookies=None, verify=True,
                                 headers=headers)
        if response.cookies:
            return response.cookies['auth']
        else:
            return response.json()
