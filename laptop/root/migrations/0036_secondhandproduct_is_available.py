# Generated by Django 4.2.5 on 2024-02-11 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0035_secondhandproduct_brand_secondhandproduct_condition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondhandproduct',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]