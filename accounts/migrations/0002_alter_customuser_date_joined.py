# Generated by Django 5.2 on 2025-04-18 13:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="date_joined",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
