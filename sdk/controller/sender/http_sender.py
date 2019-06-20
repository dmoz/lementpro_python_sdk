#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

import requests
import json
import inspect

from sdk.controller.model.base_http_request import BaseHttpRequest
from sdk.controller.model.http_request_type import HttpRequestTypes
from sdk.services.model.notifications import NotificationBuffer
from sdk.tools.logger import logger

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class HttpSender(object):

    @staticmethod
    def send_request(http_request, host=None):
        if host is None:
            app_url = BaseHttpRequest.auth_cookies['host']
        else:
            app_url = host
        log_text = "START HttpSender class METHOD - {}".format(inspect.stack()[0][3])
        logger.debug(log_text)
        url = app_url + http_request.url
        params_post = json.dumps(http_request.params)
        params_get = dict()
        if http_request.params:
            params_get = http_request.params
        headers = dict()
        headers["content-type"] = "application/json; charset=UTF-8"
        headers["Accept-Language"] = "ru-RU"
        if http_request.request_type == HttpRequestTypes.POST:
            logger.debug('\n\n$$REQUEST START$$ \nurl: {} \nheaders: {} \ncookies: {} \nparams: {} \n$$REQUEST STOP$$ \n'.format(url, headers, BaseHttpRequest.auth_cookies, params_post))
            response = requests.post(url, data=params_post, cookies=BaseHttpRequest.auth_cookies, verify=True,headers=headers)
            NotificationBuffer.resp_message = '\n\n$$RESPONSE START$$ \n{} \n{} \n{} \n$$RESPONSE STOP$$ \n'.format(response.url, '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()), response.text)
            logger.debug(NotificationBuffer.resp_message)
        elif http_request.request_type == HttpRequestTypes.GET:
            logger.debug('\n\n{} \nurl: {} \nheaders: {} \ncookies: {} \nparams: {} \n{} \n'.format(
                '-----------REQUEST start-----------', url, headers, BaseHttpRequest.auth_cookies, params_get,
                '-----------REQUEST stop-----------'))
            response = requests.get(url, params=params_get, cookies=BaseHttpRequest.auth_cookies, verify=True)
            NotificationBuffer.resp_message = '\n\n{} \n{} \n{} \n{} \n{} \n'.format('-----------RESPONSE start-----------', response.url,'\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()), response.text,"-----------RESPONSE stop--------------")
            logger.debug(NotificationBuffer.resp_message)
        return response
