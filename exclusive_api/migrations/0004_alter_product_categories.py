# Generated by Django 5.1.5 on 2025-02-12 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exclusive_api', '0003_alter_product_categories_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='exclusive_api.category', verbose_name='Categorias'),
        ),
    ]
