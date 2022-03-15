from django.db import models
from datetime import date


# Рейтинг компании
class Company(models.Model):
    founder = models.CharField('Основатель', max_length=128, blank=True, null=True)
    name = models.CharField('Название', max_length=128)
    city = models.CharField('Город', max_length=128)
    date = models.DateField(blank=True, null=True)
    staff_count = models.IntegerField('Кол-во сотрудников', blank=True, null=True)
    rate = models.IntegerField('Рейтинг', blank=True, null=True)
    description = models.CharField('Описание компании', max_length=256, blank=True, null=True)

    class Meta:
        ordering = ['-rate']
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name
