# Generated by Django 4.1.4 on 2022-12-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_rename_task_head_task_title_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
