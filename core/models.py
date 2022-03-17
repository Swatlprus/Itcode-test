from django.db import models
from datetime import date

# Размер компании
class TypeCompany(models.Model):

    type = models.CharField('Тип компании', max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = 'Тип компании'
        verbose_name_plural = 'Типы компаний'

    def __str__(self):
        return self.type

# Рейтинг компании
class Company(models.Model):
    name = models.CharField('Название', max_length=128)
    city = models.CharField('Город', max_length=128)
    type = models.ForeignKey('core.TypeCompany', on_delete=models.CASCADE, blank=True, null=True)
    founder = models.CharField('Основатель', max_length=128, blank=True, null=True)
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
