# Generated by Django 4.0.3 on 2022-03-31 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Краткое описание'),
        ),
    ]
