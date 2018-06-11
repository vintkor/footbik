# Generated by Django 2.0.5 on 2018-06-11 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20180611_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubimage',
            name='alt_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='clubimage',
            name='alt_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='clubimage',
            name='alt_uk',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='clubimage',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='clubimage',
            name='title_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='clubimage',
            name='title_uk',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='clublesson',
            name='description_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='META Описание'),
        ),
        migrations.AddField(
            model_name='clublesson',
            name='description_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='META Описание'),
        ),
        migrations.AddField(
            model_name='clublesson',
            name='description_uk',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='META Описание'),
        ),
        migrations.AddField(
            model_name='clublesson',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='clublesson',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='clublesson',
            name='title_uk',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='group',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='group',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='group',
            name='title_uk',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
    ]
