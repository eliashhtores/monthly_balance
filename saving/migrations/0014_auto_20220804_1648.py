# Generated by Django 3.2 on 2022-08-04 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saving', '0013_savingdetail_received'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='savingdetail',
            options={'ordering': ('id',)},
        ),
        migrations.AlterUniqueTogether(
            name='savingdetail',
            unique_together={('saving', 'number', 'date')},
        ),
    ]
