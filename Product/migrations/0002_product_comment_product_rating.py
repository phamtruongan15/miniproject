# Generated by Django 5.0.1 on 2024-01-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
