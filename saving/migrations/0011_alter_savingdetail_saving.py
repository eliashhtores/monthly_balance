# Generated by Django 3.2 on 2022-06-23 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saving', '0010_alter_saving_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savingdetail',
            name='saving',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saving_details', to='saving.saving'),
        ),
    ]
