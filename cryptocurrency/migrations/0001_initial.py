# Generated by Django 2.0.5 on 2018-06-20 16:45

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('code', models.CharField(max_length=7, verbose_name='Код')),
                ('is_active', models.BooleanField(default=False, verbose_name='Является активной')),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюты',
            },
        ),
        migrations.CreateModel(
            name='SystemSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settings', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Настройки системы')),
            ],
            options={
                'verbose_name': 'Системные настройки',
                'verbose_name_plural': 'Системные настройки',
            },
        ),
    ]
