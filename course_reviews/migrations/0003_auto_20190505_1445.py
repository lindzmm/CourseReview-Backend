# Generated by Django 2.2 on 2019-05-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_reviews', '0002_auto_20190505_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='credits',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
