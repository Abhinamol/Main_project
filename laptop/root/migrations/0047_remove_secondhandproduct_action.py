# Generated by Django 4.2.5 on 2024-02-29 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0046_category_secondhandproduct_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secondhandproduct',
            name='action',
        ),
    ]
