# Generated by Django 4.2.3 on 2023-07-10 20:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0007_alter_loan_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 20, 58, 53, 756669, tzinfo=datetime.timezone.utc)),
        ),
    ]
