# Generated by Django 4.2.1 on 2023-06-07 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agiletrack', '0012_alter_task_end_date_alter_task_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='cost',
        ),
    ]