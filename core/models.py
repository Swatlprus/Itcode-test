from django.db import models

class Company(models.Model):
    name = models.CharField('Название', max_length=128)
    city = models.CharField('Город', max_length=128)
    rate = models.IntegerField('Рейтинг', blank=True, null=True)

    def __str__(self):
        return self.name

# Create your models here.
