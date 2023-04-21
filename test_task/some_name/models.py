from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    number = models.IntegerField(verbose_name='Число')
