# Generated by Django 4.2.3 on 2023-07-11 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_alter_loan_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 15, 14, 34, 20, 839633, tzinfo=datetime.timezone.utc)),
        ),
    ]