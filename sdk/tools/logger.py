#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

import logging
import sys
from logging.handlers import RotatingFileHandler

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


# create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# create file handler and set level to debug
# file_handler = logging.FileHandler("test_run_log.log")
file_handler = RotatingFileHandler("robots_log.log", mode='a', maxBytes=5*1024*1024, backupCount=2, encoding=None,
                                   delay=0)
file_handler.setLevel(logging.DEBUG)
# create console handler and set level to debug
cmd_handler = logging.StreamHandler(sys.stdout)
cmd_handler.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s")
# add formatter to file_handler and cmd_handler
file_handler.setFormatter(formatter)
cmd_handler.setFormatter(formatter)
# add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(cmd_handler)
