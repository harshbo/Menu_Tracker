# Generated by Django 3.2.13 on 2023-08-23 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20230822_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='lunch',
            name='chapati',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Supper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rice', models.CharField(max_length=500)),
                ('curries', models.CharField(max_length=500)),
                ('dal', models.CharField(max_length=500)),
                ('chips', models.BooleanField(default=True)),
                ('curd', models.BooleanField(default=True)),
                ('chapati', models.BooleanField(default=True)),
                ('pickle', models.CharField(max_length=500)),
                ('dessert', models.CharField(max_length=400)),
                ('special', models.CharField(max_length=500)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.day')),
            ],
        ),
        migrations.CreateModel(
            name='Snacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snack', models.CharField(max_length=500)),
                ('milk', models.BooleanField(default=True)),
                ('var', models.CharField(max_length=500)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.day')),
            ],
        ),
        migrations.CreateModel(
            name='BreakFast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiffen', models.CharField(max_length=500)),
                ('eggs', models.BooleanField(default=True)),
                ('raagi', models.BooleanField(default=True)),
                ('juice', models.BooleanField(default=True)),
                ('oats', models.BooleanField(default=True)),
                ('milk', models.BooleanField(default=True)),
                ('var', models.CharField(max_length=500)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.day')),
            ],
        ),
    ]
