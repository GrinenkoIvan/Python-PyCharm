from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # при удалении пользователя все его задачи удоляться
    # models.PROTECT - запрещает удолять пользователя пока у него открыты задачи
    # models.SET_NULL - задачи остануться в БД,
    # models.

    def __str__(self):
        return self.title