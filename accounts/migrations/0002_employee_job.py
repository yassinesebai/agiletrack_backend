# Generated by Django 4.2.1 on 2023-05-19 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agiletrack', '0009_job'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agiletrack.job'),
        ),
    ]
