#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports
from sdk.controller.builder.get_operation_request_builder import \
    GetOperationLogRequestBuilder
from sdk.controller.sender.http_sender import HttpSender

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class OperationLogController(object):
    def get_operations(self, date_from, date_to, st_code):
        builder = GetOperationLogRequestBuilder()
        get_operations_request = builder.build(date_from, date_to)
        response = HttpSender.send_request(get_operations_request)
        assert response.status_code == st_code
        return response.json()
