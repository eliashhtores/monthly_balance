# Generated by Django 3.2 on 2022-08-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0011_alter_finance_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='paid',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
