from django.db import models


class Skills(models.Model):  # создаём таблицу id создаётся автоматом
    title = models.CharField(max_length=100)  # max кол-во вводимых символов
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='skills_home/images/')  # требуется установка модуль Pillow
    url = models.URLField(blank=True)  # Далее вводим команды по одной для наполнения БД
    # python manage.py makemigrations
    # python manage.py migrate  -  БД создалось
    # запукаем сервис python manage.py runserver
    # в браузере доступен admin, но требуется создать доступ
    # python manage.py createsuperuser
    # придумываем имя пользователя и пароль для этого приложения,адрес.
    # переходим в admin.py зарегестрировать models
