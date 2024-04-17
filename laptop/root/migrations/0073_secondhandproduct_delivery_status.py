# Generated by Django 4.2.5 on 2024-03-27 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0072_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondhandproduct',
            name='delivery_status',
            field=models.CharField(choices=[('shipped', 'Shipped'), ('out_for_delivery', 'Out for Delivery'), ('delivered', 'Delivered')], default='shipped', max_length=20),
        ),
    ]