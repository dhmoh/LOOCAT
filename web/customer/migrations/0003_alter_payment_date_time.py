# Generated by Django 4.0.4 on 2022-06-06 06:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_enter_detect_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 6, 15, 27, 59, 95522)),
        ),
    ]