# Generated by Django 4.2.3 on 2023-07-07 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copy',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='copy',
            name='end_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
