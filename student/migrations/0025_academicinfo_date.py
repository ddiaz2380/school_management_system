# Generated by Django 3.0.2 on 2020-01-16 09:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0024_remove_academicinfo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicinfo',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
