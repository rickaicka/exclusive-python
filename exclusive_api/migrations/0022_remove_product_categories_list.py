# Generated by Django 5.1.6 on 2025-03-28 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exclusive_api', '0021_product_categories_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories_list',
        ),
    ]
