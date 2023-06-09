# Generated by Django 4.2.1 on 2023-05-20 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agiletrack', '0011_project_budget_project_cost_team_project_employees'),
        ('accounts', '0002_employee_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(through='agiletrack.Team', to='agiletrack.project'),
        ),
    ]
