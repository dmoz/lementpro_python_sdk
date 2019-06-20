#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports
from sdk.controller.model.base_http_request import BaseHttpRequest
from sdk.controller.model.http_request_type import HttpRequestTypes

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class GetObjectsFromFolderRequestBuilder(object):
    def __init__(self):
        self.url = "/Services/CategoryObject/GetList.do"
        self.request_type = HttpRequestTypes.POST

    def build(self, id_folder):
        request_params = dict()
        # request_params["take"] = 50
        # request_params["skip"] = 0
        # request_params["page"] = 1
        # request_params["pageSize"] = 50
        # request_params["substr"] = ''
        # request_params["includeLastAction"] = False
        # request_params["selectedObjectId"] = ''
        # request_params["isShowAsTable"] = True
        request_params["folderKey"] = '{"id": ' + str(id_folder) + ', "subKeys": []}'
        # request_params["folderKey"] = '{\"id\":' + id_folder + ',\"subKeys\":[]}'
        http_request = BaseHttpRequest()
        http_request.params = request_params
        http_request.url = self.url
        http_request.request_type = self.request_type
        return http_request
