# Generated by Django 4.2.1 on 2023-05-31 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_employee_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]