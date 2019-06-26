#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports

from sdk.controller.object_controller import ObjectController
from sdk.services.model.lement_object import LementObject
from sdk.tools.logger import logger

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class ObjectService(object):

    def get_actions_by_id(self, object_id, st_code=200):
        """return actions for object by id
              Parameters
              ----------
              object_id : int
                  format number
              st_code : int
                  format number
        """
        object_controller = ObjectController()
        response = object_controller.get_actions_by_id(object_id, st_code)
        return response

    def get_objects_from_folder(self, id_folder, st_code=200):
        """return objects from folder by folder id
              Parameters
              ----------
              id_folder : int
                  format number
              st_code : int
                  format number
        """
        object_controller = ObjectController()
        response = object_controller.get_objects_from_folder(id_folder, st_code)
        return response

    def get_list_id_from_folder_objects(self, objects_from_folder):
        """return list ids objets from folder objects
              Parameters
              ----------
              objects_from_folder : json, dict
        """
        list_id = list()
        for items in objects_from_folder['items']:
            list_id.append(items["id"])
        return list_id

    def get_object_by_id(self, object_id, st_code=200):
        """return objects by id
              Parameters
              ----------
              object_id : int
                  format number
              st_code : int
                  format number
        """
        object_controller = ObjectController()
        response = object_controller.get_object(object_id, st_code)
        return response

    def check_fill_requred_fields(self, lement_object):
        """return result of the check fill requred fields
              Parameters
              ----------
              lement_object : LementObject
        """
        res = False
        if lement_object.all_fields_known_id is not None:
            key_field = list(lement_object.all_fields_known_id)
            default_template = self.get_default_template(
                lement_object=lement_object)
            requred_fields = self.get_requred_known_id_fields_from_def_template(default_template)
            for i in requred_fields:
                if i in key_field and lement_object.all_fields_known_id[i] != "":
                    res = True
                else:
                    res = False
        else:
            key_field = list(lement_object.all_fields)
            default_template = self.get_default_template(lement_object=lement_object)
            requred_fields = self.get_requred_fields_from_def_template(default_template)
            for i in requred_fields:
                if i in key_field and lement_object.all_fields[i] != "":
                    res = True
                else:
                    res = False
        return res

    def get_requred_fields_from_def_template(self, default_template):
        """return requred fields names from template
               Parameters
               ----------
               default_template : json,dict
         """
        req_key = list()
        for i in default_template['attributes']:
            if i['isRequired'] is True:
                req_key.append(i['field'])
        return req_key

    def get_requred_known_id_fields_from_def_template(self, default_template):
        """return requred fields known_ids from template
                  Parameters
                  ----------
                  default_template : json,dict
        """
        req_key = list()
        for i in default_template['attributes']:
            if i['isRequired'] is True:
                req_key.append(i['knownId'])
        return req_key

    def get_default_template(self, lement_object, st_code=200):
        """return default template for type
              Parameters
              ----------
              lement_object : LementObject
                  fill type and category id for LementObject
              st_code : int
                  format number
        """
        object_controller = ObjectController()
        default_template = object_controller.get_default_template(lement_object, st_code)
        return default_template

    def create_object(self, lement_object, st_code=200):
        """return result for create object
              Parameters
              ----------
              lement_object : LementObject
              st_code : int
                  format number
        """
        response = None
        if lement_object.all_fields is None and lement_object.all_fields_known_id is None:
            object_controller = ObjectController()
            response = object_controller.create_object(lement_object, st_code)
        else:
            if lement_object.all_fields_known_id is None:
                lement_object.all_fields = self.change_fields_name_on_id(lement_object.all_fields)
            else:
                lement_object.all_fields = self.change_fields_known_id_on_id(lement_object.all_fields_known_id)
            check_requred_fields = self.check_fill_requred_fields(lement_object=lement_object)

            if check_requred_fields is True:
                object_controller = ObjectController()
                response = object_controller.create_object(lement_object,
                                                           st_code)
            else:
                logger.error("Обязательные поля не заполнены")
                response = "Не создано. Обязательные поля не заполнены"

        return response

    def change_fields_name_on_id(self, all_fields):
        """return dict with ids fields and value by names fields and values fields
              Parameters
              ----------
              all_fields : dict
                format names field and values
        """
        key_field = list(all_fields)
        new_all_fields = dict()
        if "Тип" in key_field and "Категория" in key_field and all_fields["Тип"] and all_fields["Категория"]:
            for key in key_field:
                if key == 'Категория':
                    new_all_fields['categoryId'] = all_fields[key]
                else:
                    field_id = self.get_id_field_on_name(name=key, type_id=all_fields["Тип"], category_id=all_fields["Категория"])
                    new_all_fields[field_id] = all_fields[key]
        else:
            logger.error("Не задан 'Тип' обьекта и/или 'Категория'")
        return new_all_fields

    def change_fields_known_id_on_id(self, all_fields):
        """return dict with ids fields and value by known_ids fields and values fields
              Parameters
              ----------
              all_fields : dict
                format known_id fields and values
        """
        key_field = list(all_fields)
        new_all_fields = dict()
        if "type" in key_field and "categoryId" in key_field and all_fields["type"] and all_fields["categoryId"]:
            for key in key_field:
                if key == 'categoryId':
                    new_all_fields['categoryId'] = all_fields[key]
                else:
                    field_id = self.get_id_field_on_known_id(name=key, type_id=all_fields["type"], category_id=all_fields["categoryId"])
                    new_all_fields[field_id] = all_fields[key]
        else:
            logger.error("Не задан 'Тип' обьекта и/или 'Категория'")
        return new_all_fields

    def get_brithday(self, employ):
        """get brithday for user by id user in employee custom category"""
        field_brithday = None
        object_user = self.get_object_by_id(employ)
        meta = object_user["metadata"]
        object_values = object_user["object"]["values"]
        for item in meta:
            if item["knownId"] == "Дата_рождения":
                field_brithday = 'i' + str(item['id'])
        return object_values[field_brithday]

    def get_appeal_form(self, employ):
        field_appeal_form = None
        object_user = self.get_object_by_id(employ)
        meta = object_user["metadata"]
        object_values = object_user["object"]["values"]
        for item in meta:
            if item["knownId"] == "Обращение":
                field_appeal_form = 'i' + str(item['id'])
        return object_values[field_appeal_form]["value"]

    def get_need_report_value(self, employ):
        """get need report value for user by id user
         in employee custom category"""
        field_need_report = None
        object_user = self.get_object_by_id(employ)
        meta = object_user["metadata"]
        object_values = object_user["object"]["values"]
        for item in meta:
            if item["knownId"] == "Отчетность":
                field_need_report = 'i' + str(item['id'])
        try:
            return object_values[field_need_report]["value"]
        except:
            return object_values[field_need_report]

    def get_employ_full_name(self, employ):
        """get get_employ_full_name for user by id user
         in employee custom category"""
        object_user = self.get_object_by_id(employ)
        object_values = object_user["object"]["values"]
        return object_values["name"]


    def get_employ_id(self, employ):
        """get employs id for employ"""
        field_employ = None
        object_user = self.get_object_by_id(employ)
        meta = object_user["metadata"]
        object_values = object_user["object"]["values"]
        for item in meta:
            if item["knownId"] == "ФИО_сотрудника":
                field_employ = 'i' + str(item['id'])
        return object_values[field_employ]["id"]

    def get_employ_congr_text(self, employ):
        """get employs congr text in employee custom category"""
        field_brithday = None
        object_user = self.get_object_by_id(employ)
        meta = object_user["metadata"]
        object_values = object_user["object"]["values"]
        for item in meta:
            if item["displayName"] == "Поздравление":
                field_brithday = 'i' + str(item['id'])
        return object_values[field_brithday]

    def get_employee_name(self, employ):
        """get employ name in employee custom category"""
        object_user = self.get_object_by_id(employ)
        object_values = object_user["object"]["values"]
        fio = object_values['name']
        name = fio.split()
        # return name[1]
        return name

    def get_id_field_on_name(self, name, type_id, category_id, parent_object_ids=list()):
        result = None
        lement_object = LementObject()
        lement_object.category_id = category_id
        lement_object.type_id = type_id
        lement_object.parent_object_ids = parent_object_ids
        lement_object.not_all_fields = True
        template = self.get_default_template(lement_object)
        for i in template['attributes']:
            if i['name'] == name:
                result = i['field']
        return result

    def get_id_field_on_known_id(self, name, type_id, category_id, parent_object_ids=list()):
        result = None
        lement_object = LementObject()
        lement_object.category_id = category_id
        lement_object.type_id = type_id
        lement_object.parent_object_ids = parent_object_ids
        lement_object.not_all_fields = True
        template = self.get_default_template(lement_object)
        for i in template['attributes']:
            if i['knownId'] == name:
                result = i['field']
        return result

    def get_id_atribut_on_name(self, name, type_id, category_id, parent_object_ids=list()):
        result = None
        lement_object = LementObject()
        lement_object.category_id = category_id
        lement_object.type_id = type_id
        lement_object.parent_object_ids = parent_object_ids
        lement_object.not_all_fields = True
        template = self.get_default_template(lement_object)
        for i in template['attributes']:
            if i['name'] == name:
                result = i['attrId']
        return result

    def get_id_values_by_attribute(self, value_name, atribut):
        values = self.get_values_by_attribute(atribut=atribut)
        result = None
        for i in values:
            if i["value"] == value_name:
                result = i["id"]
        return result

    def get_values_by_attribute(self, atribut, st_code=200):
        """return values for attribute with change list
               Parameters
               ----------
               atribut : int
                    atribut id
               st_code : int
                   format number
         """
        object_controller = ObjectController()
        values = object_controller.get_values_by_attribute(atribut, st_code)
        return values

    def get_change_for_period_for_type(self, type_id, from_date, to_date, st_code=200):
        """return changed objects for period for type
            Parameters
            ----------
            type_id : int
                format number
            from_date : str
                format '2019-06-30'.
            to_date: str
                format '2019-06-30'.
        """
        object_controller = ObjectController()
        change = object_controller.get_change_for_period_for_type(type_id, from_date, to_date, st_code)
        return change
