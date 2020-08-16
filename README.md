# Тестовое задание
Первую часть задания выполнил в MySql 8.0
* В скрипте Test.sql Содержится скрипт создания базы данных, его наполнение тестовыми данными, и выборка по заданому условию.
* В скрипте Procedure.sql содержится скрипт процедуры, её вызов и в конце отдельно вызов измененой таблицы
***
Вторую часть делал с ипользованием фреймворка Django

Базу ипользовал mysql, настройки для неё надо поместь по во внешнюю деррикторию /venv/my.cnf, но так же в settings.py в закоментированом виде находится база SQlite3
В requirements.txt все используемые доп библиотеки.

Заполнение базы данных происходит в миграции но так же есть скрипт Test_insert.sql, который так же вносит данные в базу
Для запуска проекта надо ввести 
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Задания разбил на 3 страницы в соответсвиве с пунктами, переход на них в меню сайта
***
Дополнительно сделал папку Screenshots в которой заскринил все задания.
***
Используемые инструменты:
* DBeaver
* PyCharm
* Brackets
* SmartGit
