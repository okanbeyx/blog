# Generated by Django 3.2.20 on 2023-08-23 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deneyim',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
