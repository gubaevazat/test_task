

# test_task
Демонстрационная версия доступна по адресу `http://158.160.80.8/api/`.

Админка по адресу `http://158.160.80.8/admin/`,
логин: `admin`
пароль `test123@`
В админке реализована фильтрация и отображение полей, можно добавлять и удалять любые ресурсы.
Примечание: ресурс 'группы' из 'пользователи и группы' не используется.

Документация по адресу `http://158.160.80.8/api/docs/`
Примечание: комментарии к эндпоинтам будут ниже.

Проект размещен на сервере yandex-cloud, ОС-Ubuntu 20.04 в контейнерах **docker** с использованием **docker compose** для сборки контейнеров. Проект размещен в трех контейнерах:

 1. nginx - веб сервер
 2. db_postgress - база данных
 3. backend - апи
 Так же присутствуют два тома для media и static. Переменные окружения в файле .env на сервере.

Проект написан на **django rest framework** с использованием библиотек **djoser, simple-jwt** для регистрации и аутентификации по JWT-токену.


## Использованные технологии

 - Django 4
 - Django rest framework
 - Docker & docker compose
 - Python
 - Nginx
 - Postgress

## Эндпоинты и возможности
Все эндпоинты описаны в документации, ниже комментарии к некоторым.
Без авторизации доступны GET запросы а ресурсам assets, assets_in_work и регистрация пользователя.
Для тестирования апи использовался Postman, для авторизации нужно выбрать Bearer Token и скопировать полученный токен из поля "access".

**Авторизации и регистрации**
Регистрация пользователя, метод POST, email не обязателен, метод POST. Доступен список пользователей и информация о пользователе (добавить к запросу id пользователя из базы данных) , метод GET. Остальные эндпоинты сгенерированы библиотекой djoser (в схеме апи детально не разбирался оставил как есть).

    /api/auth/users/

Информация о текущем пользователе и его активах в работе, метод GET (в документации есть схема ответа):

    /api/auth/users/me/
Примечание: остальные методы для эндпоинта /users/me/ не используются.

Смена пароля:

    /api/auth/users/set_password/

Адреса для создания и обновления JWT-токенов согласно документации. Остальные эндпоинты не используются,  доступ к неиспользуемым адресам djoser по умолчанию (в реальном проекте можно ограничить).

**Assets-Активы**
Согласно документации. Реализована пагинация, по умолчанию 5 записей, можно изменять передавая в запросе limit=количество записей. Фильтр по названию актива, параметр name=подстрока не зависит от регистра.

**Assets in work - активы в работе**
Согласно документации. Актив можно взять работу присвоив ему статус (To Do, In progress, Complete) и указав номер актива в базе, даты проставляются автоматически. Пользователь добавляется текущий. Нельзя присвоить активу статус To Do и In Progress, если он уже присутствует с таким статусом. Присутствует пагинация, по умолчанию 5 записей, можно изменять передавая в запросе limit=количество записей. Реализованы фильтры по дате и статусу см. документацию. Формат даты 2023-08-29 15:00, даты со значением null не фильтруются.
Дополнительные ограничения доступа не реализованы, авторизованные пользователи могут совершать любые действия.

Автор: Губаев Азат. E-mail: gubaevazat@gmail.com
