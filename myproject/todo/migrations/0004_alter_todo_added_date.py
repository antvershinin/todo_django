# Generated by Django 4.2.2 on 2023-06-14 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 14, 14, 57, 7, 300896)),
        ),
    ]
