#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

from sdk.controller.category_controller import CategoryController

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class CategoryService(object):

    def get_all_categoty(self, st_code=200):
        """get list with all category objects in dict"""
        category_controller = CategoryController()
        response = category_controller.get_all_categoty(st_code)
        return response

    def find_id_by_name(self, all_category, name, is_route=False):
        """get id category from list all category"""
        result = None
        if is_route is True:
            for item in all_category:
                if item["text"] == "Задача с маршрутом":
                    for itemm in item["items"]:
                        if itemm["text"] == name:
                            result = itemm["id"]
        else:
            for item in all_category:
                if item["text"] == name:
                    result = item["id"]
            if result is None:
                name_s = name.split("/")
                len_name = len(name_s)
                for oo in all_category:
                    if oo['name'] == name_s[1]:
                        next_find = oo
                ha = 2
                while len_name > 3:
                    for itt in next_find['items']:
                        if itt['name'] == name_s[ha]:
                            next_find = itt
                    len_name = len_name - 1
                    ha = ha + 1
                if next_find['items']:
                    for pp in next_find['items']:
                        if pp['name'] == name_s[-1]:
                            result = pp['id']
                else:
                    result = next_find['id']
        return result

    def get_all_types_for_category(self, id_category, st_code=200):
        """get all types for category"""
        category_controller = CategoryController()
        response = category_controller.get_all_types_for_category(id_category, st_code)
        return response
