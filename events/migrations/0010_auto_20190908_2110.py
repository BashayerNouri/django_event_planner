# Generated by Django 2.2.5 on 2019-09-08 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20190908_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookevent',
            old_name='mail',
            new_name='email',
        ),
    ]
