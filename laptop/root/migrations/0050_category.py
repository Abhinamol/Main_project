# Generated by Django 4.2.5 on 2024-03-01 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0049_remove_secondhandproduct_category_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]