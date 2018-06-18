# Generated by Django 2.0.5 on 2018-06-18 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_cart_is_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
                ('value', models.ManyToManyField(to='shop.Value', verbose_name='Набор значений')),
            ],
            options={
                'verbose_name': 'Параметр товара',
                'verbose_name_plural': 'Параметры товара',
            },
        ),
    ]