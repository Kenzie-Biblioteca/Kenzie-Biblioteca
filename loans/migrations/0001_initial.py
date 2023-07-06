# Generated by Django 4.2.3 on 2023-07-06 17:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('copys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocked_date', models.DateTimeField(auto_now_add=True)),
                ('end_blocked_date', models.DateField(default=datetime.datetime(2023, 7, 10, 17, 0, 29, 626574, tzinfo=datetime.timezone.utc))),
                ('copy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='loans', to='copys.copy')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
