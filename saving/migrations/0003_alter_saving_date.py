# Generated by Django 3.2 on 2022-06-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saving', '0002_saving_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saving',
            name='date',
            field=models.DateField(),
        ),
    ]
