# Generated by Django 3.0.2 on 2020-01-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0022_auto_20200116_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
