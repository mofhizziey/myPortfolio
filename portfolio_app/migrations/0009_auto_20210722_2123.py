# Generated by Django 3.0.6 on 2021-07-22 21:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0008_auto_20210209_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 22, 21, 23, 43, 75504, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 22, 21, 23, 43, 62040, tzinfo=utc)),
        ),
    ]
