# Generated by Django 2.2.5 on 2019-09-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20190908_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookevent',
            name='mail',
            field=models.EmailField(blank=True, max_length=70, null=True, unique=True),
        ),
    ]
