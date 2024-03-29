# Generated by Django 3.2 on 2022-08-30 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concept', '0002_alter_concept_unique_together'),
        ('finance', '0008_alter_finance_pay_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='finance',
            name='time_frame',
            field=models.CharField(choices=[('First', 1), ('Second', 2)], default='First', max_length=6),
        ),
        migrations.AlterField(
            model_name='finance',
            name='concept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concept.concept'),
        ),
    ]
