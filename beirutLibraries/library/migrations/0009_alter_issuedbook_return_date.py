# Generated by Django 3.2.9 on 2021-12-01 07:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_issuedbook_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 16, 9, 4, 50, 814587)),
        ),
    ]