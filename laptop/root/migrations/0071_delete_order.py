# Generated by Django 4.2.5 on 2024-03-27 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0070_delete_purchase'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]