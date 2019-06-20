#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

from sdk.controller.model.base_http_request import BaseHttpRequest
from sdk.controller.model.http_request_type import HttpRequestTypes

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class CreateObjectRequestBuilder(object):
    def __init__(self):
        self.url = "/Services/ObjectBase/Create.do"
        self.request_type = HttpRequestTypes.POST

    def build(self, lement_object):
        all_fields = lement_object.all_fields
        if all_fields is None or lement_object.not_all_fields is True:
            request_params = dict()
            request_params["canAutoEditParents"] = lement_object.can_auto_edit_parents
            request_params["fileIds"] = lement_object.file_ids
            request_params["parentId"] = lement_object.parent_id
            req_values = dict()
            req_values["controllers"] = lement_object.controllers
            req_values["executors"] = lement_object.executors
            req_values["favorites"] = lement_object.favorites
            req_values["managers"] = lement_object.managers
            req_values["isResolution"] = lement_object.is_resolution
            req_values["members"] = lement_object.members
            req_values["i152"] = lement_object.i152
            req_values["i36111"] = lement_object.i36111
            req_values["i36112"] = lement_object.i36112
            req_values["name"] = lement_object.name
            req_values["startDate"] = lement_object.start_date
            req_values["endDate"] = lement_object.end_date
            if lement_object.type is None:
                req_values["type"] = lement_object.type_id
            else:
                req_values["type"] = lement_object.type
            request_params["values"] = req_values

            create_object_request = BaseHttpRequest()
            create_object_request.params = request_params
            create_object_request.url = self.url
            create_object_request.request_type = self.request_type
            return create_object_request
        else:
            all_fields_keys = list(all_fields)
            request_params = dict()
            if "canAutoEditParents" in all_fields_keys:
                request_params["canAutoEditParents"] = all_fields["canAutoEditParents"]
                all_fields_keys.remove('canAutoEditParents')
            else:
                request_params["canAutoEditParents"] = lement_object.can_auto_edit_parents
            if "fileIds" in all_fields_keys:
                request_params["fileIds"] = all_fields["fileIds"]
                all_fields_keys.remove('fileIds')
            else:
                request_params["fileIds"] = None
            if "parentTask" in all_fields_keys:
                request_params["parentId"] = all_fields["parentTask"]
                # all_fields_keys.remove('parentTask')
            else:
                request_params["parentId"] = None
            req_values = dict()
            for f_key in all_fields_keys:
                req_values[f_key] = all_fields[f_key]
            request_params["values"] = req_values
            create_object_request = BaseHttpRequest()
            create_object_request.params = request_params
            create_object_request.url = self.url
            create_object_request.request_type = self.request_type
            return create_object_request