# Generated by Django 2.0.5 on 2018-06-11 14:42

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_auto_20180611_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clublesson',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=200, null=True, verbose_name='META Описание'),
        ),
        migrations.AlterField(
            model_name='clublesson',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=200, null=True, verbose_name='META Описание'),
        ),
        migrations.AlterField(
            model_name='clublesson',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=200, null=True, verbose_name='META Описание'),
        ),
        migrations.AlterField(
            model_name='clublesson',
            name='description_uk',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=200, null=True, verbose_name='META Описание'),
        ),
    ]
