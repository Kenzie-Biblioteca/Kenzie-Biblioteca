# Generated by Django 4.2.3 on 2023-07-06 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0004_alter_loan_end_blocked_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='end_blocked_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 10, 18, 9, 29, 297904, tzinfo=datetime.timezone.utc)),
        ),
    ]