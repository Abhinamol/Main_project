# Generated by Django 4.2.5 on 2024-03-14 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0066_remove_payment_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='root.secondhandproduct'),
        ),
    ]
