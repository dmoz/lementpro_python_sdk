#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports
from sdk.controller.model.base_http_request import BaseHttpRequest
from sdk.controller.model.http_request_type import HttpRequestTypes

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class CreateFolderRequestBuilder(object):
    def __init__(self):
        self.url = "/Services/Folders/CategoryFolder/Create.do"
        self.request_type = HttpRequestTypes.POST

    def build(self, folder_object, category_id):
        request_params = dict()
        params_value = dict()
        type_folder = dict()
        type_folder["id"] = folder_object.type_id
        # type_folder["text"] = folder_object.type_text
        list_filters = []
        if folder_object.folder_filters is not None:
            for i in folder_object.folder_filters:
                list_filters.append(
                    {"valueAsString": i.value_as_string, "operation": i.operation,
                     "attributeDefId": i.attribute_def_id})
        params_value["name"] = folder_object.name
        params_value["folderFilters"] = list_filters
        params_value["type"] = type_folder
        params_value["showOnlyClosed"] = folder_object.show_only_closed
        params_value["showAllAccessible"] = folder_object.show_all_accessible
        params_value["addClosed"] = folder_object.add_closed
        request_params["values"] = params_value
        request_params["categoryId"] = category_id
        folder_create_http_request = BaseHttpRequest()
        folder_create_http_request.params = request_params
        folder_create_http_request.url = self.url
        folder_create_http_request.request_type = self.request_type
        return folder_create_http_request
