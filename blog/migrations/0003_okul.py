# Generated by Django 3.2.20 on 2023-08-23 12:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_deneyim_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Okul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title1', models.CharField(max_length=120)),
                ('title2', models.TextField(max_length=2000)),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]