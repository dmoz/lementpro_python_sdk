#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class LementObject(object):
    def __init__(self, all_fields_known_id=None, not_all_fields=True, category_id=None, type=None, parent_object_ids=list(), can_auto_edit_parents=True, file_ids=None, parent_id=None, controllers=None, executors=None, favorites=None, managers=None, is_resolution=None, members=None, i152=None, i36111=None, i36112=None, name=None, start_date=None, end_date=None, type_id=None, all_fields=None):
        self.can_auto_edit_parents = can_auto_edit_parents
        self.file_ids = file_ids
        self.parent_id = parent_id
        self.parent_object_ids = parent_object_ids
        self.controllers = controllers
        self.executors = executors
        self.favorites = favorites
        self.managers = managers
        self.is_resolution = is_resolution
        self.members = members
        self.i152 = i152
        self.i36111 = i36111
        self.i36112 = i36112
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.type_id = type_id
        self.type = type
        self.all_fields = all_fields
        self.all_fields_known_id = all_fields_known_id
        self.category_id = category_id
        self.not_all_fields = not_all_fields
