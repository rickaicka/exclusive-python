# Generated by Django 5.1.6 on 2025-03-03 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exclusive_api', '0014_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='products',
        ),
    ]
