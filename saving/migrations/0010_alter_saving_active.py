# Generated by Django 3.2 on 2022-06-23 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saving', '0009_savingdetail_saving'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saving',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
