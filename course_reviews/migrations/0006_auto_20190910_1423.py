# Generated by Django 2.2 on 2019-09-10 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_reviews', '0005_auto_20190910_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_posted',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 9, 10, 14, 23, 43, 781991)),
        ),
    ]
