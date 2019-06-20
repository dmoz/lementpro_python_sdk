#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports
from sdk.controller.dict_controller import DictController

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class Dictionary(object):

    def get_objects_from_dict(self, id_dict, st_code=200):
        """get objects from dict"""
        dict_controller = DictController()
        response = dict_controller.get_objects_from_dict(id_dict, st_code)
        return response
