#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports
from sdk.controller.builder.create_folder_request_builder import \
    CreateFolderRequestBuilder
from sdk.controller.builder.get_tree_folder_category_request_builder import \
    GetTreeFolderCategoryRequestBuilder
from sdk.controller.sender.http_sender import HttpSender

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class FolderController(object):

    def get_tree_folders_for_category(self, id_categiry, st_code):
        builder = GetTreeFolderCategoryRequestBuilder()
        get_tree_folders_request = builder.build(id_categiry)
        response = HttpSender.send_request(get_tree_folders_request)
        assert response.status_code == st_code
        return response.json()

    def create_folder(self, folder_object, category_id, st_code):
        builder = CreateFolderRequestBuilder()
        create_folder_request = builder.build(folder_object, category_id)
        response = HttpSender.send_request(create_folder_request)
        assert response.status_code == st_code
        return response.json()

    def remove_folder(self, folder_object, category_id, st_code):
        builder = CreateFolderRequestBuilder()
        create_folder_request = builder.build(folder_object, category_id)
        response = HttpSender.send_request(create_folder_request)
        assert response.status_code == st_code
        return response.json()
