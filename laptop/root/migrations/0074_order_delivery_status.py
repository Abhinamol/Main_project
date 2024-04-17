# Generated by Django 4.2.5 on 2024-03-30 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0073_secondhandproduct_delivery_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(choices=[('SH', 'Shipped'), ('OFD', 'Out for Delivery'), ('DEL', 'Delivered')], default='SH', max_length=3),
        ),
    ]