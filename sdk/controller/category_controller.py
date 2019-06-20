#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports
from sdk.controller.builder.get_all_category_request_builder import \
    GetAllCategoryRequestBuilder
from sdk.controller.builder.get_all_types_request_builder import \
    GetAllTypesRequestBuilder
from sdk.controller.sender.http_sender import HttpSender

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class CategoryController(object):

    def get_all_categoty(self, st_code):
        get_all_categoty_request_builder = GetAllCategoryRequestBuilder()
        get_all_categoty_request = get_all_categoty_request_builder.build()
        response = HttpSender.send_request(get_all_categoty_request)
        assert response.status_code == st_code
        return response.json()

    def get_all_types_for_category(self, id_category, st_code):
        get_all_types_request_builder = GetAllTypesRequestBuilder()
        get_all_types_request = get_all_types_request_builder.build(id_category)
        response = HttpSender.send_request(get_all_types_request)
        assert response.status_code == st_code
        return response.json()
