# Generated by Django 4.2.5 on 2023-11-23 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0025_remove_booking_new_address_booking_new_city_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]