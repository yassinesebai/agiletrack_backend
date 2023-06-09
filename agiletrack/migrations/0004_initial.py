# Generated by Django 4.2.1 on 2023-05-19 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agiletrack', '0003_remove_employee_tasks_remove_task_employees_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=250)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('estimated_end_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('estimated_duration', models.IntegerField()),
                ('duration', models.IntegerField(null=True)),
            ],
        ),
    ]
