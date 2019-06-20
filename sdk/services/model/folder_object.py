#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class FolderObject(object):

    def __init__(self, folder_key=None, is_show_as_table=None, name=None, type_id=None, type_text=None,
                 folder_filters=None, parent_id=None, sorting_direction=None, show_all_accessible=None, show_only_closed=None, add_closed=None):
        self.folder_key = folder_key
        self.name = name
        self.type_id = type_id
        self.type_text = type_text
        self.is_show_as_table = is_show_as_table
        self.folder_filters = folder_filters
        self.parent_id = parent_id
        self.sorting_direction = sorting_direction
        self.show_all_accessible = show_all_accessible
        self.show_only_closed = show_only_closed
        self.add_closed = add_closed


class FolderFilter(object):
    def __init__(self, value_as_string=None, operation=None, attribute_def_id=None):
        self.value_as_string = value_as_string
        self.operation = operation
        self.attribute_def_id = attribute_def_id
