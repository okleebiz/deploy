# Generated by Django 4.0.4 on 2022-06-02 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_orders_foodlist_ordersfood'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ordersfood',
            new_name='Orderfood',
        ),
    ]
