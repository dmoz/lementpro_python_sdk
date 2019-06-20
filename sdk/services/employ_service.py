#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module for work with Employee system category"""

# imports

from sdk.controller.employee_controller import EmployeeController

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class EmployeeService(object):

    def get_employee_detail(self, employ_id, st_code=200):
        """get employ detail"""
        controller = EmployeeController()
        employee_detail = controller.get_employee_detail(employ_id, st_code)
        return employee_detail

    def get_employee_email(self, employ_id):
        """get employ email"""
        employee_detail = self.get_employee_detail(employ_id)
        return employee_detail["email"]

    def get_employee_name(self, employ_id):
        """get employ name"""
        employee_detail = self.get_employee_detail(employ_id)
        return employee_detail["displayName"]

    def get_id_for_name(self, user_name):
        """get id for name"""
        employs = self.get_employs()
        employee_id = None
        for emp in employs:
            if emp["displayName"] == user_name:
                employee_id = emp["employeeId"]
        return employee_id

    def get_employs(self, department=1, include_sub_dep=True, st_code=200):
        """get id for name"""
        controller = EmployeeController()
        employee_id = controller.get_employs(department, include_sub_dep, st_code)
        return employee_id
