# Generated by Django 4.2.5 on 2023-10-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('root', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=6)),
            ],
        ),
    ]