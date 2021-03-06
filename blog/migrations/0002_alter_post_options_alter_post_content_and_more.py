# Generated by Django 4.0.3 on 2022-03-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=7000, verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='post',
            name='namePost',
            field=models.CharField(max_length=255, verbose_name='Название статьи'),
        ),
    ]
