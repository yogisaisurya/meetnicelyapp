# Generated by Django 3.2.7 on 2021-09-25 04:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 25, 4, 7, 16, 953562, tzinfo=utc)),
        ),
    ]
