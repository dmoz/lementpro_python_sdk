#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports
from sdk.controller.builder.get_objects_from_dict_request_builder import \
    GetObjectsFromDictRequestBuilder
from sdk.controller.sender.http_sender import HttpSender

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class DictController(object):

    def get_objects_from_dict(self, id_dict, st_code):
        builder = GetObjectsFromDictRequestBuilder()
        get_tree_folders_request = builder.build(id_dict)
        response = HttpSender.send_request(get_tree_folders_request)
        assert response.status_code == st_code
        return response.json()
