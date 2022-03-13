from django.db import models
from datetime import date

# Основатель компании
class Founder(models.Model):
    name = models.CharField('Основатель', max_length=128)
    bio = models.CharField('Краткая биография', max_length=512, null=True, blank=True)

    class Meta:
        verbose_name = 'Основатель'
        verbose_name_plural = 'Основатели'

    def __str__(self):
        return self.name


# Рейтинг компании
class Company(models.Model):
    founder = models.ForeignKey('core.Founder', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Основатель')
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
