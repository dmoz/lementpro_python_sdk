#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This module is """

# imports
import datetime
import re

from sdk.controller.operation_log_controller import OperationLogController
from sdk.services.auth_service import AuthService
from sdk.services.folder_service import FolderService
from sdk.services.model.folder_object import FolderObject, FolderFilter
from sdk.services.object_service import ObjectService

__author__ = 'Evgeny Nalivayko'
__email__ = "nalivayko.ev@gmail.com"


class OperationLogService(object):

    def get_operations(self, date_from, date_to, st_code=200):
        """get employ operation"""
        controller = OperationLogController()
        employee_operation = controller.get_operations(date_from, date_to, st_code)
        return employee_operation

    def get_closed_tasks(self, empl, data):
        closed_tasks = list()
        for i in data:
            if i["employeeId"] == empl:
                for obj in i["objects"]:
                    for chang in obj["changes"]:
                        if chang["changeType"] == "TaskClosed":
                            ct = dict()
                            ct["id"] = obj["objectId"]
                            ct["name"] = obj["objectName"]
                            closed_tasks.append(ct)
        return closed_tasks

    def get_tasks(self, date_from=None, date_to=None, add_closed=True):
        folder_object = FolderObject()
        folder_object.name = "Все задачи 777"
        folder_object.type_id = 2
        folder_object.add_closed = add_closed
        folder_object.show_all_accessible = True
        folder_object.show_only_closed = False

        if date_from is not None and date_to is not None:
            filtets = list()

            folder_filter1 = FolderFilter()
            folder_filter1.attribute_def_id = 30701
            folder_filter1.operation = 6
            folder_filter1.value_as_string = date_from.isoformat()

            folder_filter2 = FolderFilter()
            folder_filter2.attribute_def_id = 30701
            folder_filter2.operation = 4
            folder_filter2.value_as_string = date_to.isoformat()

            filtets.append(folder_filter1)
            filtets.append(folder_filter2)

            folder_object.folder_filters = filtets

        id_category_task = 2

        folder_servive = FolderService()
        folder_tasks = folder_servive.create_folder(folder_object, id_category_task)

        # получить объекты папки
        object_service = ObjectService()
        get_objects_from_folder = object_service.get_objects_from_folder(folder_tasks)

        tasks_ids = list()
        for item in get_objects_from_folder["items"]:
            tasks_ids.append(item["id"])

        # удалить папку

        return tasks_ids

    def get_docs(self, date_from, date_to, add_closed=True):
        pass

    def parse(self, data_template, tasks, docs, date_to, date_from):
        object_service = ObjectService()
        # для каждой задачи
        for t in tasks:
            # получаем задачу
            t_date = object_service.get_object_by_id(object_id=t)
            eml_closed_id = 000
            t_date_name = None
            t_date_url = None

            # Проверяем закрыта ли задача в указанный период
            last_modified_date_str = re.search(r'\((.*?)\)', t_date['object']['values']['lastModifiedDate'])
            last_modified_date_str = last_modified_date_str[1]
            last_modified_date_t = int(last_modified_date_str[0:-3])
            if last_modified_date_t < 0:
                last_modified_date_t = datetime.datetime(1970, 1,
                                                       1) + datetime.timedelta(
                    seconds=last_modified_date_t)
            else:
                last_modified_date_t = datetime.datetime.utcfromtimestamp(
                    last_modified_date_t)

            # print("SRAVNI")
            # print(last_modified_date)
            # print(date_from.isoformat())

            if t_date["object"]["isClosed"] == True and last_modified_date_t.isoformat() >= date_from.isoformat() and last_modified_date_t.isoformat() <= date_to.isoformat():
                # если да, то определяем кто закрыл
                # возвращаем сообщения по задаче /Services/Action/GetList.do
                actions_for_task = object_service.get_actions_by_id(object_id=t)
                if actions_for_task[0]["message"] == '<span>Объект изменен:</span><br /><span>Задача завершена</span><br />':
                    eml_closed_id = actions_for_task[0]["author"]["id"]
                    t_date_name = t_date["object"]["values"]["name"]
                    t_date_url = t_date["object"]["objectUrl"]
                else:
                    print("Нужно обработать случай - последнее сообщение закрытой задачи не 'Задача завершена'")

            ### Для каждого пользователя которому требуется отчет
            for empl in list(data_template):
                ### проверяем есть ли закрывший в списке data_template
                if empl == str(eml_closed_id) and t_date_name is not None and t_date_url is not None:
                    #### если есть, добавляем ему в список "closed_task" название и ссылку на задачу
                    text = t_date_name + " / " + t_date_url
                    data_template[str(empl)]["closed_task"].append(text)


            # Собираем реплики пользователей из всех задачь за период
            # возвращаем сообщения по задаче /Services/Action/GetList.do
            actions_for_task = object_service.get_actions_by_id(object_id=t)
            for task_action in actions_for_task:
                # входит ли реплика в исследуемый временной период ?
                last_modified_date_str = re.search(r'\((.*?)\)', task_action['lastModifiedDate'])
                last_modified_date_str = last_modified_date_str[1]
                last_modified_date = int(last_modified_date_str[0:-3])
                if last_modified_date < 0:
                    last_modified_date = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=last_modified_date)
                else:
                    last_modified_date = datetime.datetime.utcfromtimestamp(last_modified_date)

                if last_modified_date.isoformat() >= date_from.isoformat() and last_modified_date.isoformat() <= date_to.isoformat():

                    author_action = task_action["author"]["id"]
                    message_action = task_action["message"]
                    t_date_name = t_date["object"]["values"]["name"]
                    t_date_url = t_date["object"]["objectUrl"]
                    for empl in list(data_template):
                        # проверяем есть ли автор реплики в списке data_template
                        if empl == str(author_action):
                            text = "{} - {}".format(last_modified_date,
                                                    message_action)
                            # если автор реплики есть, проверяем есть ли задача в словаре actions_in_tasks
                            task_names = list(data_template[str(empl)]["actions_in_tasks"])
                            if t_date_name in task_names:
                                data_template[str(empl)]["actions_in_tasks"][t_date_name].append(text)
                            else:
                                data_template[str(empl)]["actions_in_tasks"][t_date_name] = list()
                                data_template[str(empl)]["actions_in_tasks"][
                                    t_date_name].append(text)
        return data_template

    def get_agreed_not_agreed_docs(self, empl, data):
        docs = list()
        for i in data:
            if i["employeeId"] == empl:
                for obj in i["objects"]:
                    for change in obj["changes"]:
                        if change["changeType"] == "SuccessSignaturing" or change["changeType"] == "SuccessApproving" or change["changeType"] == "ApprovingDeclined" or change["changeType"] == "SignaturingDeclined":
                            doc = dict()
                            doc["id"] = obj["objectId"]
                            doc["name"] = obj["objectName"]
                            doc["comment"] = change["commentText"]
                            docs.append(doc)
        return docs

    def get_actions_in_tasks(self, empl, data):
        actions_tasks = list()
        for i in data:
            if i["employeeId"] == empl:
                for obj in i["objects"]:
                    purpos_object = dict()
                    comments = list()
                    purpos_object["id"] = obj["objectId"]
                    purpos_object["name"] = obj["objectName"]
                    for chang in obj["changes"]:
                        if chang["changeType"] == "CommentAdded":
                            com_text = chang["commentText"]
                            comments.append(com_text)
                    if comments:
                        purpos_object["comments"] = comments
                        actions_tasks.append(purpos_object)
        return actions_tasks

    def get_actions_in_docs(self, empl, data):
        actions_docs = list()
        for i in data:
            if i["employeeId"] == empl:
                for obj in i["objects"]:
                    purpos_object = dict()
                    comments = list()
                    purpos_object["id"] = obj["objectId"]
                    purpos_object["name"] = obj["objectName"]
                    for chang in obj["changes"]:
                        if chang["changeType"] == "CommentAdded":
                            com_text = chang["commentText"]
                            comments.append(com_text)
                    if comments:
                        purpos_object["comments"] = comments
                        actions_docs.append(purpos_object)
        return actions_docs
