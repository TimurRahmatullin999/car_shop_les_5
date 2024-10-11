# Generated by Django 5.1.2 on 2024-10-11 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyer',
            options={'ordering': ['name'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['title'], 'verbose_name': 'Машина', 'verbose_name_plural': 'Машины'},
        ),
        migrations.AlterModelOptions(
            name='historyorder',
            options={'ordering': ['date_make_order'], 'verbose_name': 'Дата заказа', 'verbose_name_plural': 'Даты заказов'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['id_order'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='owner',
            options={'ordering': ['name'], 'verbose_name': 'Владелец', 'verbose_name_plural': 'Владельцы'},
        ),
        migrations.AlterModelOptions(
            name='storage',
            options={'ordering': ['street'], 'verbose_name': 'Улица', 'verbose_name_plural': 'Улицы'},
        ),
    ]