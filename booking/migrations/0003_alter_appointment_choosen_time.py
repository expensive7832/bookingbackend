# Generated by Django 4.2.3 on 2023-07-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='choosen_time',
            field=models.DateTimeField(),
        ),
    ]
