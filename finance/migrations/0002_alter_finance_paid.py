# Generated by Django 3.2 on 2022-08-16 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
