# Generated by Django 3.2 on 2021-08-13 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_service_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='Slug',
            new_name='slug',
        ),
    ]
