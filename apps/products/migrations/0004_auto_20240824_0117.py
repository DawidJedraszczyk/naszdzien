# Generated by Django 3.2.1 on 2024-08-23 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20240824_0116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='featues',
            new_name='features',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='featues',
            new_name='features',
        ),
    ]
