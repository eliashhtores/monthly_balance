# Generated by Django 3.2 on 2022-08-16 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_alter_finance_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='finance',
            name='due_date',
            field=models.DateField(),
        ),
    ]