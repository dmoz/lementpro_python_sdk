#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class BaseHttpRequest(object):
    url = None
    params = None
    header = dict()
    request_type = None
    auth_cookies = dict()
    auth_token_bim = None
    files = None
    host = None
