# Generated by Django 3.2 on 2022-08-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0009_auto_20220830_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='time_frame',
            field=models.CharField(blank=True, choices=[('First', 1), ('Second', 2)], max_length=6, null=True),
        ),
    ]
