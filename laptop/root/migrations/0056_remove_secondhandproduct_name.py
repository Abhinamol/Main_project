# Generated by Django 4.2.5 on 2024-03-09 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0055_wishlist_wishlistitem_wishlist_products_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secondhandproduct',
            name='name',
        ),
    ]