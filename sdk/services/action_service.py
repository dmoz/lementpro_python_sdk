#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports
from sdk.controller.action_controller import ActionController
from sdk.services.object_service import ObjectService

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class ActionService(object):

    def send_massage_to_external_user(self, object, external_emails_list, message, st_code=200):
        action_controller = ActionController()
        response = action_controller.send_massage_to_external_user(object, external_emails_list, message, st_code)
        return response

    def get_actions_by_id(self, object_id, st_code=200):
        object_service = ObjectService()
        response = object_service.get_actions_by_id(object_id, st_code)
        return response