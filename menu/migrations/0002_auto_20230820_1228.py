# Generated by Django 3.2.13 on 2023-08-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='chips',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='curd',
            field=models.BooleanField(default=True),
        ),
    ]
