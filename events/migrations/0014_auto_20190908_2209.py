# Generated by Django 2.2.5 on 2019-09-08 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20190908_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookevent',
            old_name='booked_seats',
            new_name='book_seats',
        ),
    ]
