# Generated by Django 4.0.3 on 2022-03-16 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_typecompany_company_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typecompany',
            options={'verbose_name': 'Тип компании', 'verbose_name_plural': 'Типы компаний'},
        ),
        migrations.AlterField(
            model_name='typecompany',
            name='type',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Тип компании'),
        ),
    ]
