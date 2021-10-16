
## Ecommerce shop built with Django REST framework
### This project supports the following functions:
- filtration,
- pagination,
- search,
- authorization,
- authentication using JWT,
- authentication with djoser,
- auto-documenting using swagger.
   
 To this ecommerce shop has been added CORS


[![Build Status](https://app.travis-ci.com/Igor-Kuz/drfshop.svg?branch=master)](https://app.travis-ci.com/Igor-Kuz/drfshop)

### Инструменты разработки
 
**Стек:**

 - Python >= 3.7

- Django >= 3

- requests >= 2.23.0

- sqlite3


## Установка и запуск

##### 1) Открыть терминал или консоль и перейти в нужную Вам директорию

##### 2) Клонировать репозиторий и поставить звездочку)

    git clone https://github.com/Igor-Kuz/drfshop.git

##### 3) Создать виртуальное окружение

    python -m venv venv
    
##### 3) Активировать виртуальное окружение


##### 4 ) Устанавливить зависимости:

    pip install -r reqirements.txt

##### 5) Выполнить миграции

##### 6) Запустить сервер

    python manage.py runserver

Не забудьте создать директорию media, куда будут сохраняться изображения для товара
