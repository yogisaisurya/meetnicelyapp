# Generated by Django 3.2.7 on 2021-09-29 04:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0031_alter_post_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 29, 4, 30, 12, 864485, tzinfo=utc)),
        ),
    ]
