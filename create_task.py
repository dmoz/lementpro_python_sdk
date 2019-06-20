#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sdk.services.auth_service import AuthService
from sdk.services.object_service import ObjectService
from sdk.services.model.lement_object import LementObject
from sdk.services.model.server import Server
from sdk.services.model.user import User

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


auth_service = AuthService()
object_service = ObjectService()

user = User(username="enalivayko", password="31455761Wc")
server = Server(host="https://sodislab.lement.pro")

auth_service.login(user=user, server=server)

object_for_create = LementObject()
object_for_create.not_all_fields = False
object_for_create.all_fields_known_id \
    = {"type": 5, "categoryId": 2, "name": "Test",
       "startDate": "2019-06-20T21:34:29.929Z",
       "endDate": "2099-06-21T21:00:00.000Z",
       "task_status": "b0b19d71-7b6e-46ac-a36f-39dd1f1d4bf1"}

object_service.create_object(lement_object=object_for_create)
