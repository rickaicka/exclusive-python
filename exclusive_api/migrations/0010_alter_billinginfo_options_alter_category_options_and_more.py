# Generated by Django 5.1.6 on 2025-02-13 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exclusive_api', '0009_alter_billinginfo_options_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='billinginfo',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='paymentinfo',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]
