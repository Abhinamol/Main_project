# Generated by Django 4.2.5 on 2024-03-14 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0064_remove_payment_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='root.cart'),
        ),
    ]