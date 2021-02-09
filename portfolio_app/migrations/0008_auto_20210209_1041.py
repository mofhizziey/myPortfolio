# Generated by Django 3.0.6 on 2021-02-09 10:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0007_auto_20210209_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 10, 41, 9, 907126, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 10, 41, 9, 906058, tzinfo=utc)),
        ),
    ]
