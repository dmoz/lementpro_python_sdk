# lementpro_python_sdk

### Предусловия
* Установить python версии 3.6 
* Установить библиотеки из requirements.txt
```bash
pip3 install -r requirements.txt
```

### Использование на примере создания объекта в LementPro
* Готовый скрипт - create_task.py
* В sdk созданы классы (сервисы) для выполнения различных операций в LementPro - sdk/services и модели обьектов, объединяющие используемые в sdk сущности - sdk/services/model
* Выполните импорты нужных сервисов и моделей
```bash
from sdk.services.auth_service import AuthService
from sdk.services.object_service import ObjectService
from sdk.services.model.lement_object import LementObject
from sdk.services.model.server import Server
from sdk.services.model.user import User
```
* Создайте объекты нужных сервисов
```bash
auth_service = AuthService()
object_service = ObjectService()
```
* Используйте методы сервисов и модели объектов для выполнения задуманного в LementPro
```bash
# подготавливаем обьект площадки и юзера
user = User(username="enalivayko", password="enalivayko")
server = Server(host="https://lementtest.lement.pro")
# авторизуемся, токен будет сохранен в sdk и использован для последующих вызовов
auth_service.login(user=user, server=server)
# подготавливаем обьект для создания
object_for_create = LementObject()
object_for_create.not_all_fields = False
# заполняем поле обьекта LementObject - all_fields_known_id,как словарь с идентификатором атрибута создаваемого объекта LementPro и значением, можно использовать поле обьекта LementObject - all_fields, тогда вместо идентификатора можно писать название атрибута создаваемого объекта LementPro
object_for_create.all_fields_known_id = {"type": 5, "categoryId": 2, "name": "Test","startDate":"2019-06-20T21:34:29.929Z","endDate":"2099-06-21T21:00:00.000Z", "task_status": "b0b19d71-7b6e-46ac-a36f-39dd1f1d4bf1"}
# создаем обьект
object_service.create_object(lement_object=object_for_create)
```



