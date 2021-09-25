# drfshop
REST API for ecommerce shop based on Django REST framework

Репозиторий API интернет-магазина на Django REST framework

Открыть терминал или консоль и перейти в нужную Вам директорию

Если Вы используете https, то выполнить команду: git clone https://github.com/Igor-Kuz/drfshop.git

Прописать следующие команды:


python3 -m venv ДиректорияВиртуального окружения
source ДиректорияВиртуальногоОкружения/scipts/activate
Перейти в директорию shop

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate


Запустить сервер - python manage.py runserver

Не забудьте создать директорию media, куда будут сохраняться изображения для товара
