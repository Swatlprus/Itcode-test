from django.db import models

class Post(models.Model):
    namePost = models.CharField('Название статьи', max_length=255)
    datetime = models.DateField('Дата публикации')
    description = models.CharField('Краткое описание', max_length=255, null=True)
    content = models.TextField('Текст статьи', max_length=7000)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.namePost