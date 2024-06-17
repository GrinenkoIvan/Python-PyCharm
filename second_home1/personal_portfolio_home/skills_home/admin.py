from django.contrib import admin
from .models import Skills  # .models т.е папка находится рядом для импорта


admin.site.register(Skills)  # (Skills) - имя класса в models.py
# БД создалось и для работы с картинками переходим в setting.py



