# Generated by Django 4.2.5 on 2024-03-14 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0062_delete_productexchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='purchase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='root.purchase'),
        ),
    ]