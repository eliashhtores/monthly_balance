# Generated by Django 3.2 on 2022-08-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saving', '0012_alter_savingdetail_saving'),
    ]

    operations = [
        migrations.AddField(
            model_name='savingdetail',
            name='received',
            field=models.BooleanField(default=False),
        ),
    ]
