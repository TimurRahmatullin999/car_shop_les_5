# Generated by Django 5.1.2 on 2024-10-11 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carshop', '0002_alter_buyer_options_alter_car_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storage',
            options={'ordering': ['street'], 'verbose_name': 'Склад', 'verbose_name_plural': 'Склад'},
        ),
    ]
