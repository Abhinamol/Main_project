# Generated by Django 4.2.5 on 2024-03-01 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0048_alter_secondhandproduct_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secondhandproduct',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]