# Generated by Django 4.0.3 on 2022-03-03 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('city', models.CharField(max_length=128, verbose_name='Город')),
                ('rate', models.IntegerField(blank=True, null=True, verbose_name='Рейтинг')),
            ],
        ),
    ]