# Generated by Django 4.2.5 on 2024-02-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0042_remove_secondhandproduct_is_available_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondhandproduct',
            name='action',
            field=models.CharField(choices=[('pending', 'Approval Pending'), ('approved', 'Approved')], default='pending', max_length=20),
        ),
    ]