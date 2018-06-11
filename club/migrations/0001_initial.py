# Generated by Django 2.0.5 on 2018-06-11 13:08

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
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
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Клуб',
                'verbose_name_plural': 'Клубы',
            },
        ),
        migrations.CreateModel(
            name='ClubAdministrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Администратор клуба',
                'verbose_name_plural': 'Администраторы клубов',
            },
        ),
        migrations.CreateModel(
            name='ClubImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/images/clubs/', verbose_name='Изображение')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок')),
                ('alt', models.CharField(blank=True, max_length=200, null=True)),
                ('sort', models.PositiveSmallIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Изображение клуба',
                'verbose_name_plural': 'Изображения клубов',
                'ordering': ('sort',),
            },
        ),
        migrations.CreateModel(
            name='ClubLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='META Описание')),
                ('is_test', models.BooleanField(default=False, verbose_name='Пробное занятие')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('color', colorfield.fields.ColorField(default='#238a53', max_length=18, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(verbose_name='Начало занятия')),
                ('date_end', models.DateTimeField(verbose_name='Завершение занятия')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.Group')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.ClubLesson')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписания',
            },
        ),
    ]
