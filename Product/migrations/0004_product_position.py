# Generated by Django 5.0.1 on 2024-01-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_product_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='position',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
