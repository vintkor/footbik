# Generated by Django 2.0.5 on 2018-06-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_uk',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_uk',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
    ]
