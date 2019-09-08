# Generated by Django 2.2.5 on 2019-09-08 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20190908_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookevent',
            name='email',
            field=models.EmailField(default=1, max_length=70),
            preserve_default=False,
        ),
    ]