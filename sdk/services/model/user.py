#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class User(object):

    def __init__(self, username=None, password=None, user_ids=None, full_name=None, department_id=None,
                 email=None, is_system_admin=False, rememberme=True):
        self.username = username
        self.password = password
        self.full_name = full_name
        self.rememberme = rememberme
        self.user_ids = user_ids
        self.department_id = department_id
        self.email = email
        self.is_system_admin = is_system_admin
