#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

from sdk.controller.model.base_http_request import BaseHttpRequest
from sdk.controller.model.http_request_type import HttpRequestTypes

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class GetDefaultTemplateBuilder(object):
    def __init__(self):
        self.url = "/Services/ObjectsBase/Template/GetDefaultTemplate.do"
        self.request_type = HttpRequestTypes.POST

    def build(self, lement_object):
        if lement_object.all_fields_known_id is None:
            all_fields = lement_object.all_fields
        else:
            all_fields = lement_object.all_fields_known_id
        if all_fields is None or lement_object.not_all_fields is True:
            request_params = dict()
            request_params["categoryId"] = lement_object.category_id
            request_params["typeId"] = lement_object.type_id
            request_params["parentObjectIds"] = lement_object.parent_object_ids
            get_all_category_http_request = BaseHttpRequest()
            get_all_category_http_request.params = request_params
            get_all_category_http_request.url = self.url
            get_all_category_http_request.request_type = self.request_type
            return get_all_category_http_request
        else:
            request_params = dict()
            request_params["categoryId"] = all_fields["categoryId"]
            request_params["typeId"] = all_fields["type"]
            parents = list()
            try:
                parents.append(all_fields["parentTask"])
            except:
                parents.append(None)
            request_params["parentObjectIds"] = parents
            get_all_category_http_request = BaseHttpRequest()
            get_all_category_http_request.params = request_params
            get_all_category_http_request.url = self.url
            get_all_category_http_request.request_type = self.request_type
            return get_all_category_http_request
