# Generated by Django 4.2.5 on 2024-03-09 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0058_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondhandproduct',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='root.category'),
        ),
    ]