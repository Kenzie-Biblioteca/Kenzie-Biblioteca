# Generated by Django 4.2.3 on 2023-07-10 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0008_alter_loan_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 20, 59, 49, 962196, tzinfo=datetime.timezone.utc)),
        ),
    ]
