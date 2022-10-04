# Generated by Django 3.2 on 2022-08-16 15:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('concept', '0002_alter_concept_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(auto_now_add=True)),
                ('paid', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('concept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concept', to='concept.concept')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]