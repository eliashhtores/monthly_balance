# Generated by Django 3.2 on 2022-08-31 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0013_alter_finance_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='amount',
            field=models.FloatField(),
        ),
    ]
