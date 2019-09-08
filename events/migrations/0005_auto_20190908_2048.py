# Generated by Django 2.2.5 on 2019-09-08 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190908_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='seats',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True),
        ),
    ]
