from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=120)
    factory = models.CharField(max_length=50)
    Change = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(null=True)
    duration = models.CharField(max_length=30, null=True)
    team = models.CharField(max_length=100, null=True)
    message = models.TextField()
    incident = models.TextField()
    status = models.BooleanField()
    objects = models.Manager()
    class Meta:
        verbose_name = "Форма отправки"
        verbose_name_plural = "Формы отправки"

class User(models.Model):
    name = models.CharField(max_length=120)
    password = models.TextField()
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
