# Generated by Django 3.2 on 2022-08-23 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_auto_20220816_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finance',
            name='active',
        ),
    ]