# Generated by Django 5.1.5 on 2025-02-12 23:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exclusive_api', '0005_alter_product_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsByCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exclusive_api.category', verbose_name='Categoria')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exclusive_api.product', verbose_name='Produto')),
            ],
            options={
                'ordering': ['category', 'product'],
            },
        ),
    ]
