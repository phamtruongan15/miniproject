# Generated by Django 5.0.1 on 2024-01-24 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_rename_customer_id_order_customer'),
        ('OrderLine', '0001_initial'),
        ('Product', '0004_product_position'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='OrderLine',
        ),
    ]
