from django.db import models
from datetime import date

# Основатель компании
class Founder(models.Model):
    name = models.CharField('Основатель', max_length=128)

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
    staff_count = models.ForeignKey('core.Staff', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Кол-во сотрудников')
    rate = models.IntegerField('Рейтинг', blank=True, null=True)

    class Meta:
        ordering = ['-rate']
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name

# Дата основания компании
class DateFound(models.Model):
    date = models.DateField()
    company = models.ManyToManyField('core.Company')

    class Meta:
        verbose_name = 'Дата основания'
        verbose_name_plural = 'Даты оснований'

    def __str__(self):
        return f'{self.date}'


# Количество сотрудников
class Staff(models.Model):
    count = models.IntegerField('Кол-во сотрудников', blank=True, null=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return str(self.count)