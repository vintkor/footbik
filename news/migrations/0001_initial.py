# Generated by Django 2.0.5 on 2018-06-20 16:45

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('title_uk', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=230, null=True, unique=True)),
                ('meta_keywords', models.CharField(blank=True, max_length=200, null=True, verbose_name='META Ключевые слова')),
                ('meta_keywords_ru', models.CharField(blank=True, max_length=200, null=True, verbose_name='META Ключевые слова')),
                ('meta_keywords_uk', models.CharField(blank=True, max_length=200, null=True, verbose_name='META Ключевые слова')),
                ('meta_keywords_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='META Ключевые слова')),
                ('meta_description', models.CharField(blank=True, max_length=200, null=True, verbose_name='META Описание')),
                ('meta_description_ru', models.CharField(blank=True, max_length=200, null=True, verbose_name='META Описание')),
                ('meta_description_uk', models.CharField(blank=True, max_length=200, null=True, verbose_name='META Описание')),
                ('meta_description_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='META Описание')),
                ('image', models.ImageField(upload_to='images/news/', verbose_name='Изображение')),
                ('excerpt', models.TextField(verbose_name='Анонс')),
                ('excerpt_ru', models.TextField(null=True, verbose_name='Анонс')),
                ('excerpt_uk', models.TextField(null=True, verbose_name='Анонс')),
                ('excerpt_en', models.TextField(null=True, verbose_name='Анонс')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Текст')),
                ('text_uk', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Текст')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Текст')),
                ('created', models.DateTimeField(verbose_name='Дата создания')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='geo.Region')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
