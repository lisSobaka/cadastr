# Generated by Django 5.0.2 on 2024-02-23 11:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cadastr', models.CharField(max_length=20, verbose_name='Кадастровый номер')),
                ('longitude', models.CharField(max_length=10, verbose_name='Долгота')),
                ('latitude', models.CharField(max_length=10, verbose_name='Широта')),
                ('result', models.BooleanField(verbose_name='Ответ сервера')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата запроса')),
            ],
            options={
                'verbose_name_plural': 'Запросы',
            },
        ),
    ]
