#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """


import re

from sdk.controller.folder_controller import FolderController

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class FolderService(object):

    def return_tree_folders_for_category(self, id_categiry, st_code=200):
        """get list with all category objects in dict"""
        folder_controller = FolderController()
        response = folder_controller.get_tree_folders_for_category(id_categiry, st_code)
        return response

    def find_id_by_name(self, tree_folders, name, issystem=False):
        """ get id folder with name and property issystem from tree folders"""
        result = None
        for item in tree_folders:
            if item["isSystem"] == issystem and item['text'] == name:
                id_string = item["folderKey"]
                result = re.search(r'\d+', id_string)
        return result[0]

    def create_folder(self, folder_object, category_id, st_code=200):
        folder_controller = FolderController()
        response = folder_controller.create_folder(folder_object, category_id, st_code)
        id_folder = response["folderKey"].split('"id":')[1].split(',', maxsplit=1)[0]
        return id_folder

    def remove_folder(self, folder_id):
        folder_controller = FolderController()
        response = folder_controller.remove_folder(folder_id)
        return response
