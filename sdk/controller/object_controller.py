#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """
from sdk.controller.builder.create_object_request_builder import \
    CreateObjectRequestBuilder
from sdk.controller.builder.get_action_request_builder import \
    GetActionRequestBuilder
from sdk.controller.builder.get_change_builder import GetChangeBuilder
from sdk.controller.builder.get_default_template_builder import \
    GetDefaultTemplateBuilder
from sdk.controller.builder.get_object_request_builder import \
    GetObjectRequestBuilder
from sdk.controller.builder.get_objects_from_folder_request_builder import \
    GetObjectsFromFolderRequestBuilder
from sdk.controller.builder.get_values_by_attribute_builder import \
    GetValuesByAttributeBuilder
from sdk.controller.sender.http_sender import HttpSender

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class ObjectController(object):
    def get_objects_from_folder(self, id_folder, st_code):
        """/Services/CategoryObject/GetList.do"""
        builder = GetObjectsFromFolderRequestBuilder()
        get_tree_folders_request = builder.build(id_folder)
        response = HttpSender.send_request(get_tree_folders_request)
        assert response.status_code == st_code
        return response.json()

    def get_values_by_attribute(self, atribut, st_code):
        """/Services/ObjectTypes/AttributeListOfValues/GetValuesByAttribute.do"""
        builder = GetValuesByAttributeBuilder()
        get_values_by_attribute_request = builder.build(atribut)
        response = HttpSender.send_request(get_values_by_attribute_request)
        assert response.status_code == st_code
        return response.json()

    def get_object(self, object_id, st_code):
        """/Services/ObjectBase/Get.do"""
        builder = GetObjectRequestBuilder()
        get_object_request = builder.build(object_id)
        response = HttpSender.send_request(get_object_request)
        assert response.status_code == st_code
        return response.json()

    def get_actions_by_id(self, object_id, st_code):
        """/Services/Action/GetList.do"""
        builder = GetActionRequestBuilder()
        get_action_request = builder.build(object_id)
        response = HttpSender.send_request(get_action_request)
        assert response.status_code == st_code
        return response.json()

    def create_object(self, lement_object, st_code):
        """/Services/ObjectBase/Create.do"""
        builder = CreateObjectRequestBuilder()
        create_object_request = builder.build(lement_object)
        response = HttpSender.send_request(create_object_request)
        assert response.status_code == st_code
        return response.json()

    def get_default_template(self, lement_object, st_code):
        """/Services/ObjectsBase/Template/GetDefaultTemplate.do"""
        builder = GetDefaultTemplateBuilder()
        get_template_request = builder.build(lement_object)
        response = HttpSender.send_request(get_template_request)
        assert response.status_code == st_code
        return response.json()

    def get_change_for_period_for_type(self, type_id, from_date, to_date, st_code):
        """/Services/ObjectBase/GetChangedObjects.do"""
        builder = GetChangeBuilder()
        get_change_request = builder.build(type_id, from_date, to_date)
        response = HttpSender.send_request(get_change_request)
        assert response.status_code == st_code
        return response.json()
