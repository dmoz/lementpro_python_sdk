#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports
from sdk.controller.builder.get_employee_detail_request_builder import \
    GetEmployeeDetailRequestBuilder
from sdk.controller.builder.get_id_for_name_builder import GetListEmploysBuilder
from sdk.controller.sender.http_sender import HttpSender

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class EmployeeController(object):

    def get_employee_detail(self, employ_id, st_code):
        builder = GetEmployeeDetailRequestBuilder()
        get_tree_folders_request = builder.build(employ_id)
        response = HttpSender.send_request(get_tree_folders_request)
        assert response.status_code == st_code
        return response.json()

    def get_employs(self, department, include_sub_dep, st_code):
        builder = GetListEmploysBuilder()
        get_id_request = builder.build(department, include_sub_dep)
        response = HttpSender.send_request(get_id_request)
        assert response.status_code == st_code
        return response.json()
